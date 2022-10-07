from macko.repository.postgres import Postgres


class SimpleRepository(Postgres):
    table = 'simple'
