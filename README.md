# BLOK

A simple Blockchain implementation written in Python. I took advantage of [this source](https://www.gauravvjn.com/building-a-simple-blockchain-in-python-part-2/).

## Stacks

- Poetry
- Pytest
- Pyright
- Flask
- Black
- Isort

## Installation

After you installed [poetry](https://python-poetry.org/docs/#installation), just type `poetry install`.

To run unit tests:

```shell
$ poetry run pytest
```

To run the blockchain server:

```shell
$ poetry run python -m blok.main --debug=true
```
