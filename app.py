from flask import Flask, abort
from macko.utils.config_handler import config_handle
from macko.utils.error_handler import error_handle
from macko.utils.register_blueprint_handler import register_blueprint_handle


app = Flask(__name__)

config_handle(app)
error_handle(app)
register_blueprint_handle(app)


if __name__ == '__main__':
    app.run('0.0.0.0',8080)