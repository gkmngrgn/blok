import json
import typing

import flask

from blok.http_server import get_app


class ServerForTest(object):
    def __init__(self, port: int):
        self.app = get_app()
        self.app.config["SERVER_NAME"] = f"0.0.0.0:{port}"
        self.app.config["TESTING"] = True

    def get_url(self, endpoint: str) -> str:
        with self.app.app_context():
            url = flask.url_for(endpoint)
        return url

    def send_get_request(self, endpoint: str) -> flask.Response:
        with self.app.test_client() as client:
            response = client.get(self.get_url(endpoint))
        return response

    def send_post_request(
        self, endpoint: str, data: typing.Dict[str, typing.Any]
    ) -> flask.Response:
        with self.app.test_client() as client:
            response = client.post(
                self.get_url(endpoint),
                data=json.dumps(data),
                content_type="application/json",
            )
        return response
