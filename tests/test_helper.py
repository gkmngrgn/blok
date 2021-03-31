import typing

import flask

from blok.http_server import app

app.config["SERVER_NAME"] = "0.0.0.0:8080"
app.config["TESTING"] = True


def get_url(endpoint: str) -> str:
    with app.app_context():
        url = flask.url_for(endpoint)
    return url


def send_get_request(endpoint: str) -> flask.Response:
    with app.test_client() as client:
        response = client.get(get_url(endpoint))
    return response


def send_post_request(
    endpoint: str, data: typing.Dict[str, typing.Any]
) -> flask.Response:
    with app.test_client() as client:
        response = client.post(get_url(endpoint), data=data)
    return response
