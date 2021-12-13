import pytest
import requests

base_url = "http://192.168.1.191:5000/"

author_url = base_url + "api/authors/"
user_url = base_url + "api/users/"


@pytest.fixture(scope="session", autouse=True)
def data():
    var = {"username": "admin", "password": "flask"}
    r = requests.post(user_url, json=var)
    var = {"username": "lin", "password": "hao"}
    r = requests.post(user_url, json=var)
