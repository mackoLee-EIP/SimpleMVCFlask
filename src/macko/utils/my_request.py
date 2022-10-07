from flask import request


def get_query():
    result = request.args
    if len(result):
        return result
    return {}


def get_params():
    if request.is_json:
        return request.get_json()
    result = request.form
    if len(result):
        return result
    return {}
