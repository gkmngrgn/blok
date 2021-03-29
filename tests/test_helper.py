import requests

test_url = "http://0.0.0.0:8080"


def get_url(prefix: str) -> str:
    return f"{test_url}{prefix}"


def send_get_request(url_prefix: str) -> requests.Response:
    url = get_url(url_prefix)
    return requests.get(url)
