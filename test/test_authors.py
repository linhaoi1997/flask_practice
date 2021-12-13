import requests

base_url = "http://127.0.0.1:5001/"

author_url = base_url + "api/authors/"
user_url = base_url + "api/users/"


class Client:

    def __init__(self, username, password):
        self.headers = self.login(username, password)

    def post(self, url, **kwargs):
        return requests.post(url, headers=self.headers, **kwargs).json()

    def get(self, url, **kwargs):
        return requests.get(url, headers=self.headers, **kwargs).json()

    def put(self, url, **kwargs):
        return requests.put(url, headers=self.headers, **kwargs).json()

    def patch(self, url, **kwargs):
        return requests.patch(url, headers=self.headers, **kwargs).json()

    @classmethod
    def login(cls, username, password):
        var = {"username": username, "password": password}
        r = requests.post(user_url + "login", json=var)
        token = r.json()["access_token"]
        return {"Authorization": "Bearer " + token}


def test_get_authors():
    r = Client("admin", "flask").get(author_url)
    print(r)
    r = Client("lin", "hao").get(author_url)
    print(r)


def test_get_author():
    r = Client("admin", "flask").get(author_url + "1")
    print(r)
    r = Client("lin", "hao").get(author_url + "2")
    print(r)
    r = Client("lin", "hao").get(author_url + "1")
    print(r)


def test_post_authors():
    var = {"first_name": "nani", "last_name": "lelele"}
    r = Client("admin", "flask").post(author_url, json=var)
    print(r)


def test_post_authors2():
    var = {"first_name": "ceshi2", "last_name": "ceshi2"}
    r = Client("lin", "hao").post(author_url, json=var)
    print(r)
