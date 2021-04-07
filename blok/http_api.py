from flask import Blueprint, Response, current_app

from blok.helpers import get_json_response, get_neighbour_chains, get_request_data
from blok.node_server import Block

api = Blueprint("blockchain_api", __name__)


@api.route("/create_transaction/", methods=["POST"])
def create_transaction() -> Response:
    transaction_data = get_request_data()
    block_index = current_app.blockchain.create_new_transaction(**transaction_data)
    response_data = {
        "message": "Transaction has been completed successfully.",
        "block_index": block_index,
    }
    return get_json_response(response_data, 201)


@api.route("/mine/", methods=["GET"])
def mine() -> Response:
    block = current_app.blockchain.mine_block(current_app.node_address)
    response_data = {
        "message": "The new block has been mined successfully.",
        "block_data": block,
    }
    return get_json_response(response_data, 200)


@api.route("/chain/", methods=["GET"])
def get_chain() -> Response:
    response_data = {
        "chain": current_app.blockchain.serialized_chain,
    }
    return get_json_response(response_data, 200)


@api.route("/register_node/", methods=["POST"])
def register_node() -> Response:
    node_data = get_request_data()
    current_app.blockchain.create_node(node_data.get("address"))
    response_data = {
        "message": "New node has been added.",
        "node_count": len(current_app.blockchain.nodes),
        "nodes": sorted(current_app.blockchain.nodes),
    }
    return get_json_response(response_data, 201)


@api.route("/sync_chain/", methods=["GET"])
def sync_chain() -> Response:
    chains = get_neighbour_chains()
    longest_chain = max(chains, key=len) if chains else []
    if len(current_app.blockchain.chain) < len(longest_chain):
        current_app.blockchain.chain = [
            Block.get_instance(block_data) for block_data in longest_chain
        ]
    response_data = {"chain": current_app.blockchain.serialized_chain}
    return get_json_response(response_data, 200)
