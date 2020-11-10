from abc import ABCMeta, abstractmethod

import mysql.connector
import sqlite3


class FetchBehaviour(metaclass=ABCMeta):
    @abstractmethod
    def fetch(self, ref, sql):
        pass


class SqliteFetch(FetchBehaviour):
    def fetch(self, ref, sql):
        ref.connect()

        results = []

        try:
            cursor = ref.db.execute(sql)

            for result in cursor:
                results.append(result)

        except Exception:
            return False

        cursor.close()
        ref.db.close()

        return results


class MySQLFetch(FetchBehaviour):
    def fetch(self, ref, sql):
        ref.connect()

        results = []

        try:
            cursor = ref.db.cursor()
            cursor.execute(sql)

            for result in cursor.fetchall():
                results.append(result)

            cursor.close()
            ref.db.close()

        except Exception:
            return False

        return results
