from flask import render_template
from macko.repository.simple_repository import SimpleRepository

simple_repository = SimpleRepository()


def test():
    return 'test'


def test_db():
    return simple_repository.find_all()


def test_template():
    return render_template('index.html')
