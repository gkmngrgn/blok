import functools

import flask
import pytest
import requests

from blok.http_server import app

app.config["SERVER_NAME"] = "0.0.0.0:8080"


def send_get_request(endpoint: str) -> requests.Response:
    with app.app_context():
        url = flask.url_for(endpoint)
    return requests.get(url)


def server_required(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        is_server_up = True

        try:
            response = send_get_request("ping")
        except requests.exceptions.ConnectionError:
            is_server_up = False
        else:
            is_server_up = response.status_code == 200

        if is_server_up is False:
            return pytest.skip("http server is not active. skipping...")

        return func(*args, **kwargs)

    return wrapper
