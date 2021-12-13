from api.models.users import UserSchema
from api.utils.database import db
from marshmallow_sqlalchemy import SQLAlchemySchema
from marshmallow import fields
from api.models.books import BookSchema


class Author(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    created = db.relationship("User")
    books = db.relationship('Book', backref='Author',
                            cascade="all, delete-orphan")

    def __init__(self, first_name, last_name, created_by, books=None):
        self.first_name = first_name
        self.last_name = last_name
        self.books = books or []
        self.created_by = created_by

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self


class AuthorSchema(SQLAlchemySchema):
    class Meta(SQLAlchemySchema.Meta):
        model = Author
        sqla_session = db.session
        load_instance = True

    id = fields.Number(dump_only=True)
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    created_by = fields.Integer(required=True)
    created = fields.Nested(UserSchema, only=['username'])
    books = fields.Nested(BookSchema, many=True,
                          only=['title', 'year', 'id'])
