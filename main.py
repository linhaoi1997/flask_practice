import logging
import os
import sys

import api.utils.responses as resp
from api.models.users import User
from api.utils.responses import response_with
from flask_jwt_extended import JWTManager
from flask import Flask
from api.config.config import *
from api.utils.database import db
from api.routes.authors import author_routes
from api.routes.books import book_routes
from api.routes.users import user_routes

app = Flask(__name__)
jwt = JWTManager(app)
app.register_blueprint(author_routes, url_prefix='/api/authors')
app.register_blueprint(book_routes, url_prefix='/api/books')
app.register_blueprint(user_routes, url_prefix='/api/users')


@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.id


@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return User.query.filter_by(id=identity).one_or_none()


@app.after_request
def add_header(response):
    return response


@app.errorhandler(400)
def bad_request(e):
    logging.error(e)
    return response_with(resp.BAD_REQUEST_400)


@app.errorhandler(500)
def server_error(e):
    logging.error(e)
    return response_with(resp.SERVER_ERROR_500)


@app.errorhandler(404)
def not_found(e):
    logging.error(e)
    return response_with(resp.SERVER_ERROR_404)


if os.environ.get('WORK_ENV') == 'PROD':
    app_config = ProductionConfig
elif os.environ.get('WORK_ENV') == 'TEST':
    app_config = TestingConfig
else:
    app_config = DevelopmentConfig

app.config.from_object(app_config)

db.init_app(app)
with app.app_context():
    # db.drop_all()
    db.create_all()

logging.basicConfig(
    stream=sys.stdout,
    format='%(asctime)s|%(levelname)s|%(filename)s:%(lineno)s|%(message)s',
    level=logging.DEBUG)
