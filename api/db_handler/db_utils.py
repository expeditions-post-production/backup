import sqlite3
from api.configs_reader import DATABASE_ROOT


class Database:
    def __init__(self):
        self.__connection = sqlite3.connect(DATABASE_ROOT)

    def commit(self):
        self.__connection.commit()

    def execute(self, q, arg=None):
        cur = self.__connection.cursor()
        if arg:
            cur.execute(q, arg)
        else:
            cur.execute(q)
        res = cur.fetchall()
        cur.close()
        return res
