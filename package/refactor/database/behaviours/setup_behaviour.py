from abc import ABCMeta, abstractmethod

import mysql.connector
import sqlite3


class SetupBehaviour(metaclass=ABCMeta):
    @abstractmethod
    def setup(self, ref):
        raise NotImplementedError


class SqliteSetup(SetupBehaviour):
    def setup(self, ref):
        sql = (
            "create table if not exists analysis"
            "(id integer primary key autoincrement,"
            "path varchar(100),"
            "fileCount integer,"
            "classCount integer,"
            "attributeCount integer,"
            "methodCount integer)"
        )
        success = ref.query(sql)

        return success


class MySQLSetup(SetupBehaviour):
    def setup(self, ref):
        sql = "create table if not exists analysis "\
            "(id integer primary key auto_increment, path varchar(100), "\
            "fileCount integer, classCount integer, attributeCount integer, "\
            "methodCount integer)"
        # if ref.connect():
        #     try:
        #         cursor = ref.db.cursor()
        #         cursor.execute(sql)
        #         ref.db.commit()
        #         cursor.close()
        #         ref.db.close()
        #     except Exception:
        #         return False

        #     return True

        # return False
        success = ref.query(sql)

        return success
