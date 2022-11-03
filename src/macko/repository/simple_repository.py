from macko.repository.postgres import Postgres


class SimpleRepository(Postgres):
    table = 'simple'

    def find_all_by_id(self):
        pass