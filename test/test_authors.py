import requests
import pytest

base_url = "http://192.168.1.191:5000/"

author_url = base_url + "api/authors/"
user_url = base_url + "api/users/"


@pytest.fixture()
def headers():
    var = {"username": "admin", "password": "flask"}
    r = requests.post(user_url + "login", json=var)
    token = r.json()["access_token"]
    return {"Authorization": "Bearer " + token}


def test_get_authors(headers):
    r = requests.get(author_url, headers=headers)
    print(r.json())


def test_post_authors():
    var = {"first_name": "lin", "last_name": "hao"}
    r = requests.post(author_url, json=var)
    print(r.json())


def test_create_user():
    var = {"username": "admin", "password": "flask"}
    r = requests.post(user_url, json=var)
    print(r.json())


def test_login():
    var = {"username": "admin", "password": "flask"}
    r = requests.post(user_url + "login", json=var)
    print(r.json())
