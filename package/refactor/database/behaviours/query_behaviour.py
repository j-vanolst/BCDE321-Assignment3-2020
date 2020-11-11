from abc import ABCMeta, abstractmethod

import mysql.connector
import sqlite3


class QueryBehaviour(metaclass=ABCMeta):
    @abstractmethod
    def query(self, ref, sql):
        raise NotImplementedError


class SqliteQuery(QueryBehaviour):
    def query(self, ref, sql):
        ref.connect()
        try:
            ref.db.execute(sql)
            ref.db.commit()

        except Exception:
            return False

        return True


class MySQLQuery(QueryBehaviour):
    def query(self, ref, sql):
        ref.connect()

        try:
            cursor = ref.db.cursor()
            cursor.execute(sql)
            ref.db.commit()
            cursor.close()
            ref.db.close()

        except Exception:
            return False

        return True
