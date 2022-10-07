from flask import Blueprint
from macko.service import simple_service

blueprint = Blueprint('app', __name__, url_prefix='/simple')


@blueprint.route('/test')
def test():
    return simple_service.test()


@blueprint.route('/test_db')
def test_db():
    return simple_service.test_db()


@blueprint.route('/template')
def test_template():
    return simple_service.test_template()