from macko.config.common import Config


class DevConfig(Config):
    DEBUG = True
    DATABASE = {
        "dbname": "postgres",
        "user": "postgres",
        "password": "ekfrElaorzh",
        "host": "localhost",
        "port": "5432"
    }
