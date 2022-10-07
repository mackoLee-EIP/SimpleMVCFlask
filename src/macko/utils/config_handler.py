from os import environ
from macko.config.dev import DevConfig
from macko.config.product import ProductConfig
from macko.config import test

configs = test.get_test_config()

def config_handle(app):
    def set_database_config(config):
        configs['DATABASE'] = config.DATABASE

    def set_config(config):
        app.config.from_object(config)
        set_database_config(config)

    env = environ.get('ENV', 'DEV')
    env = env.upper()
    Config = {
        'DEV': DevConfig,
        'PRODUCT': ProductConfig
    }
    set_config(Config[env])


def get_database_config(key):
    return configs['DATABASE'][key]