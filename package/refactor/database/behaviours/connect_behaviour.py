from abc import ABCMeta, abstractmethod

import mysql.connector
import sqlite3


class ConnectBehaviour(metaclass=ABCMeta):
    @abstractmethod
    def connect(self):
        pass


class SqliteConnect(ConnectBehaviour):
    def connect(self, ref):
        ref.db = sqlite3.connect(ref.database)
