import typing

import flask

from .test_helper import ServerForTest


def get_chain(server: flask.Flask) -> typing.Dict[str, typing.Any]:
    response = server.send_get_request("blockchain_api.get_chain")
    assert response.status_code == 200

    chain = response.json.get("chain", [])
    assert len(chain) >= 1  # at least there should be a block in the chain.
    return chain


def test_first_chain_data():
    server = ServerForTest(port=8000)
    block = get_chain(server)[0]
    assert block["index"] == 0
    assert block["previous_hash"] == "0"
    assert block["proof"] == 0
    assert block["transactions"] == []


def test_mining():
    server = ServerForTest(port=8001)
    response = server.send_get_request("blockchain_api.mine")
    assert response.status_code == 200

    previous_hash = response.json["block_data"]["block_hash"]
    response = server.send_get_request("blockchain_api.mine")
    assert response.status_code == 200
    assert previous_hash == response.json["block_data"]["previous_hash"]


def test_create_transaction():
    server = ServerForTest(port=8002)

    # create new transaction
    last_block = get_chain(server)[-1]
    request_data = {
        "sender": "addr1",
        "recipient": "addr2",
        "amount": 3,
    }
    response = server.send_post_request(
        "blockchain_api.create_transaction", data=request_data
    )
    assert response.status_code == 201
    assert response.json == {
        "block_index": last_block["index"] + 1,
        "message": "Transaction has been completed successfully.",
    }

    # mine a new block
    response = server.send_get_request("blockchain_api.mine")
    assert response.status_code == 200

    transaction_data = response.json["block_data"]["transactions"]
    expected_data = [
        {"amount": 3, "recipient": "addr2", "sender": "addr1"},
        {"amount": 1, "recipient": server.app.node_address, "sender": "0"},
    ]
    assert transaction_data == expected_data

    # check the latest block
    last_block = get_chain(server)[-1]
    assert last_block["transactions"] == expected_data


def test_register_node():
    server1 = ServerForTest(port=8001)
    # server2 = ServerForTest(port=8002)

    request_data = {"address": "https://0.0.0.0:8002"}
    response = server1.send_post_request(
        "blockchain_api.register_node", data=request_data
    )
    assert response.status_code == 201
    assert response.json == {
        "message": "New node has been added.",
        "node_count": 1,
        "nodes": ["https://0.0.0.0:8002"],
    }
