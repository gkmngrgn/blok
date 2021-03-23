import typing
from flask import Response, jsonify, request

JsonData = typing.Dict[str, typing.Any]


def get_json_response(data: JsonData) -> Response:
    import ipdb

    ipdb.set_trace()
    return jsonify(data)  # type: ignore


def get_request_data() -> JsonData:
    import ipdb

    ipdb.set_trace()
    return request.get_json()  # type: ignore
