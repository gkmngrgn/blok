from .test_helper import send_get_request, server_required


@server_required
def test_first_chain_data():
    response = send_get_request("chain")
    assert response.status_code == 200

    response_data = response.json()
    chain = response_data.get("chain", [])
    assert len(chain) >= 1  # at least there should be a block in the chain.

    block = chain[0]
    assert block["index"] == 0
    assert block["previous_hash"] == "0"
    assert block["proof"] == 0
    assert block["transactions"] == []


@server_required
def test_mining():
    response = send_get_request("mine")
    assert response.status_code == 200

    response_data = response.json()
    previous_hash = response_data["block_data"]["block_hash"]

    response = send_get_request("/mine/")
    assert response.status_code == 200

    response_data = response.json()
    assert previous_hash == response_data["block_data"]["previous_hash"]
