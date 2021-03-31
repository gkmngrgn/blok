import flask

from blok.http_server import app

app.config["SERVER_NAME"] = "0.0.0.0:8080"
app.config["TESTING"] = True


def send_get_request(endpoint: str) -> flask.Response:
    with app.app_context():
        url = flask.url_for(endpoint)
    with app.test_client() as client:
        response = client.get(url)
    return response
