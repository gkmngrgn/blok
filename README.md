# BLOK

A simple Blockchain implementation written in Python. I took advantage of [this article](https://www.gauravvjn.com/building-a-simple-blockchain-in-python-part-2/).

## Installation

```shell
$ pip install poetry
$ poetry install
```

To run unit tests:

```shell
$ poetry run pytest
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
