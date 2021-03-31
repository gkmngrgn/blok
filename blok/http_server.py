from uuid import uuid4

from flask import Flask, Response

from blok.helpers import get_json_response, get_request_data
from blok.node_server import BlockChain

app = Flask(__name__)
blockchain = BlockChain()
node_address = uuid4().hex


@app.route("/create_transaction/", methods=["POST"])
def create_transaction() -> Response:
    transaction_data = get_request_data()
    block_index = blockchain.create_new_transaction(**transaction_data)
    response_data = {
        "message": "Transaction has been completed successfully.",
        "block_index": block_index,
    }
    return get_json_response(response_data)


@app.route("/mine/", methods=["GET"])
def mine() -> Response:
    block = blockchain.mine_block(node_address)
    response_data = {
        "message": "The new block has been mined successfully.",
        "block_data": block,
    }
    return get_json_response(response_data)


@app.route("/chain/", methods=["GET"])
def chain():
    response_data = {
        "chain": blockchain.serialized_chain,
    }
    return get_json_response(response_data)
