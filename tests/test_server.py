from .test_helper import send_get_request


def test_first_chain_data():
    response = send_get_request("/chain/")
    assert response.status_code == 200

    response_data = response.json()
    chain = response_data.get("chain", [])
    assert len(chain) == 1

    block = chain[0]
    assert block["index"] == 0
    assert block["previous_hash"] == "0"
    assert block["proof"] == 0
    assert block["transactions"] == []


def test_first_mining():
    response = send_get_request("/mine/")
    assert response.status_code == 200

    response_data = response.json()
    import ipdb; ipdb.set_trace()
    previous_hash = response_data["block_data"]["block_hash"]
