from abc import ABCMeta, abstractmethod

import mysql.connector
import sqlite3


class QueryBehaviour(metaclass=ABCMeta):
    @abstractmethod
    def query(self, sql):
        pass


class SqliteQuery(QueryBehaviour):
    def query(self, ref, sql):
        ref.connect()
        try:
            ref.db.execute(sql)
            ref.db.commit()

        except Exception:
            return False

        return True
