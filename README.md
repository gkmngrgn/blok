# BLOK

A simple Blockchain implementation written in Python.

```ascii
     ┌─────────────────────────────-─────────┐
     │  BLOCKCHAIN                           │
     ├───────────────────────────────-───────┤
┌────┤► chain: List[BLOCK]                   │
│    │                                       │
│    │  new_transactions: List[TRANSACTION] ◄├───────────────────────┐
│    │                                       │                       │
│    │  nodes: List[ADDRESS]                ◄├────┐                  │
│    └───────────────────────────────────────┘    │                  │
│                                                 │                  │
│    ┌───────────────────────────────────┐   ┌────┴──────────────┐   │
└────┤  BLOCK                            │   │  ADDRESS: String  │   │
     ├───────────────────────────────────┤   └───────────────────┘   │
     │  index: Integer                   │                           │
     │                                   │   ┌─────────────────────┐ │
     │  proof: Integer                   │ ┌─┤  TRANSACTION        ├─┘
     │                                   │ │ ├─────────────────────┤
     │  previous_hash: String            │ │ │  sender: String     │
     │                                   │ │ │                     │
     │  transactions: List[TRANSACTION] ◄├─┘ │  recipient: String  │
     └───────────────────────────────────┘   │                     │
                                             │  amount: Integer    │
                                             └─────────────────────┘
```

## Installation

```shell
$ pip install poetry
$ poetry install
```

To run unit tests:

```shell
$ poetry run coverage run -m pytest
$ poetry run coverage report -m
```

To run the blockchain server:

```shell
$ poetry run python -m blok.main --debug=true
```

## Code Quality

```shell
$ poetry run pre-commit install
$ poetry run pre-commit run --all-files
```

## Sources

The best source for me was the blockchain course series in [Coursera](https://www.coursera.org/specializations/blockchain).

I took advantage of [this article](https://www.gauravvjn.com/building-a-simple-blockchain-in-python-part-2/).
