from abc import ABCMeta, abstractmethod

import mysql.connector
import sqlite3


class SetupBehaviour(metaclass=ABCMeta):
    @abstractmethod
    def setup(self):
        pass


class SqliteSetup(SetupBehaviour):
    def setup(self, ref):
        sql = 'create table if not exists analysis' \
              '(id integer primary key autoincrement,' \
              'path varchar(100),' \
              'fileCount integer,' \
              'classCount integer,' \
              'attributeCount integer,' \
              'methodCount integer)'
        ref.query(sql)
