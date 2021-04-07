import typing

import requests
from flask import Response, current_app, jsonify, request, url_for

SerializedData = typing.Dict[str, typing.Any]
SerializedList = typing.List[SerializedData]


def get_json_response(data: SerializedData, status_code: int = 200) -> Response:
    return jsonify(data), status_code  # type: ignore


def get_request_data() -> SerializedData:
    return request.get_json() or {}  # type: ignore


def get_neighbour_chains() -> typing.List[SerializedList]:
    chains = []

    for node_url in current_app.blockchain.nodes:
        response = requests.get(
            f"{node_url}{url_for('blockchain_api.get_chain')}"
        ).json()
        chains.append(response["chain"])

    return chains
