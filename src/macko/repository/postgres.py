import psycopg2
from macko.utils.config_handler import get_database_config

class Postgres:
    table = None
    conn = None

    def __init__(self):
        self.info = {
            "dbname": get_database_config("dbname"),
            "user": get_database_config("user"),
            "password": get_database_config("password"),
            "host": get_database_config("host"),
            "port": get_database_config("port")
        }

    def save(self):
        pass

    def find_all(self):
        cur = self.execute_sql(f"select * from {self.table}")
        return cur.fetchall()

    def execute_sql(self, sql):
        self.connect()
        cur = self.conn.cursor()
        cur.execute(sql)
        self.close()
        return cur

    def connect(self):
        self.conn=psycopg2.connect(**self.info)

    def close(self):
        self.conn.close

if __name__ == "__main__":
    post = Postgres()
    post.table = 'simple'
    print(post.find_all())