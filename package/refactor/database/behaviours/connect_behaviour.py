from abc import ABCMeta, abstractmethod

import mysql.connector
import sqlite3


class ConnectBehaviour(metaclass=ABCMeta):
    @abstractmethod
    def connect(self, ref):
        raise NotImplementedError


class SqliteConnect(ConnectBehaviour):
    def connect(self, ref):
        try:
            ref.db = sqlite3.connect(ref.database)
        except Exception:
            return False

        return True


class MySQLConnect(ConnectBehaviour):
    def connect(self, ref):
        if ref.db:
            ref.db.close()
        try:
            ref.db = mysql.connector.connect(
                host=ref.address,
                user=ref.username,
                password=ref.password,
                database=ref.database,
            )
        except Exception:
            return False

        return True
