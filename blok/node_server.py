import hashlib
import time
import typing
from dataclasses import dataclass

from blok.helpers import SerializedData


@dataclass
class Transaction:
    sender: str
    recipient: str
    amount: int

    @classmethod
    def get_instance(cls, data: SerializedData) -> "Transaction":
        return cls(**data)

    @property
    def serialized_data(self) -> SerializedData:
        return vars(self)


@dataclass
class Block:
    index: int
    proof: int
    previous_hash: str
    transactions: typing.List[Transaction]
    timestamp: float = time.time()

    @classmethod
    def get_instance(cls, data: SerializedData) -> "Block":
        block = cls(
            index=data["index"],
            proof=data["proof"],
            previous_hash=data["previous_hash"],
            transactions=[
                Transaction.get_instance(transaction)
                for transaction in data["transactions"]
            ],
            timestamp=data["timestamp"],
        )
        return block

    @property
    def block_hash(self) -> str:
        transactions = [
            transaction.serialized_data for transaction in self.transactions
        ]
        block_string = f"{self.index}{self.proof}{self.previous_hash}{transactions}{self.timestamp}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    @property
    def serialized_data(self) -> SerializedData:
        data = vars(self)
        data["block_hash"] = self.block_hash
        return data


class BlockChain:
    def __init__(self) -> None:
        self.chain: typing.List[Block] = []
        self.new_transactions: typing.List[Transaction] = []
        self.nodes: typing.Set[str] = set()
        self.create_genesis_block()

    def create_genesis_block(self) -> None:
        first_hash = hashlib.sha256("GOEDEV".encode()).hexdigest()
        self.create_new_block(proof=0, previous_hash=first_hash)

    def create_new_block(self, proof: int, previous_hash: str) -> Block:
        block = Block(
            index=len(self.chain),
            proof=proof,
            previous_hash=previous_hash,
            transactions=self.new_transactions,
        )
        self.new_transactions = []
        self.chain.append(block)
        return block

    def create_new_transaction(self, sender: str, recipient: str, amount: int) -> int:
        self.new_transactions.append(
            Transaction(sender=sender, recipient=recipient, amount=amount)
        )
        return self.last_block.index + 1

    def create_node(self, address: str) -> bool:
        self.nodes.add(address)
        return True

    @staticmethod
    def create_proof_of_work(previous_proof: int) -> int:
        proof: int = previous_proof + 1
        while (proof + previous_proof) % 7 != 0:
            proof += 1
        return proof

    def mine_block(self, miner_address: str) -> SerializedData:
        self.create_new_transaction(sender="0", recipient=miner_address, amount=1)
        last_block = self.last_block
        last_proof = last_block.proof
        proof = self.create_proof_of_work(last_proof)
        last_hash = last_block.block_hash
        block = self.create_new_block(proof, last_hash)
        return block.serialized_data

    @property
    def last_block(self) -> Block:
        return self.chain[-1]

    @property
    def serialized_chain(self) -> typing.List[SerializedData]:
        return [block.serialized_data for block in self.chain]
