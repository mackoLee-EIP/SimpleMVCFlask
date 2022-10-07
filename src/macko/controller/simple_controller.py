from flask import Blueprint
from macko.service import simple_service
from macko.utils import my_request
blueprint = Blueprint('app', __name__, url_prefix='/simple')


@blueprint.get('/test')
def test():
    query = my_request.get_query()
    return simple_service.test(query)


@blueprint.route('/test', methods=["POST"])
def post_test():
    params = my_request.get_params()
    return simple_service.test(params)


@blueprint.route('/test_db')
def test_db():
    return simple_service.test_db()


@blueprint.route('/template')
def test_template():
    return simple_service.test_template()