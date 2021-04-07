from blok.node_server import BlockChain


def test_blockchain():
    blockchain = BlockChain()
    assert len(blockchain.chain) == 1

    last_block = blockchain.last_block
    assert last_block.index == 0
    assert last_block.proof == 0
    assert (
        last_block.previous_hash
        == "d90a95445a5f5ca918dbeb66be74e8004054a5b627ed3fb807f2b8adae4ad03e"
    )
    assert len(last_block.transactions) == 0

    last_proof = last_block.proof
    last_hash = last_block.block_hash

    proof = blockchain.create_proof_of_work(last_proof)
    blockchain.create_new_transaction(sender="0", recipient="address_x", amount=1)

    new_block = blockchain.create_new_block(proof=proof, previous_hash=last_hash)
    assert new_block.index == 1
    assert new_block.proof == 7
    assert new_block.previous_hash != last_block.previous_hash
    assert new_block.previous_hash == last_block.block_hash
    assert len(new_block.transactions) == 1
