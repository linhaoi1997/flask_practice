import pytest
import requests

base_url = "http://127.0.0.1:5001/"

author_url = base_url + "api/authors/"
user_url = base_url + "api/users/"


@pytest.fixture(scope="session", autouse=True)
def data():
    var = {"username": "admin", "password": "flask"}
    r = requests.post(user_url, json=var)
    var = {"username": "lin", "password": "hao"}
    r = requests.post(user_url, json=var)
