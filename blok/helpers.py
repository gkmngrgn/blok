import typing

from flask import Response, jsonify, request

SerializedData = typing.Dict[str, typing.Any]


def get_json_response(data: SerializedData) -> Response:
    return jsonify(data)  # type: ignore


def get_request_data() -> SerializedData:
    return request.get_json() or {}  # type: ignore
