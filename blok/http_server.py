from uuid import uuid4

import flask

from blok.http_api import api
from blok.node_server import BlockChain


def get_app() -> flask.Flask:
    app = flask.Flask(__name__)
    app.blockchain = BlockChain()
    app.node_address = uuid4().hex
    app.register_blueprint(api)
    return app
