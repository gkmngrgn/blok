from .test_helper import send_get_request, send_post_request


def get_chain():
    response = send_get_request("chain")
    assert response.status_code == 200

    chain = response.json.get("chain", [])
    assert len(chain) >= 1  # at least there should be a block in the chain.
    return chain


def test_first_chain_data():
    block = get_chain()[0]
    assert block["index"] == 0
    assert block["previous_hash"] == "0"
    assert block["proof"] == 0
    assert block["transactions"] == []


def test_mining():
    response = send_get_request("mine")
    assert response.status_code == 200

    previous_hash = response.json["block_data"]["block_hash"]
    response = send_get_request("mine")
    assert response.status_code == 200
    assert previous_hash == response.json["block_data"]["previous_hash"]


def test_create_transaction():
    last_block = get_chain()[-1]
    request_data = {
        "sender": "addr1",
        "recipient": "addr2",
        "amount": 3,
    }
    response = send_post_request("create_transaction", data=request_data)
    assert response.status_code == 200
    assert response.json == {
        "block_index": last_block["index"] + 1,
        "message": "Transaction has been completed successfully.",
    }
