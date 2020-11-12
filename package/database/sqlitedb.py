import sqlite3

from .database import Database


class SqliteDB(Database):
    def __init__(self, database):
        super().__init__(database)

    def connect(self):
        try:
            self.db = sqlite3.connect(self.database)
        except Exception:
            return False
        return True

    def query(self, sql: str):
        self.connect()
        try:
            self.db.execute(sql)
            self.db.commit()

        except Exception:
            return False

        return True

    def fetch(self, sql: str):
        self.connect()

        results = []

        try:
            cursor = self.db.execute(sql)

            for result in cursor:
                results.append(result)

        except Exception:
            return False

        self.db.close()
        return results

    def setup(self):
        sql = (
            "create table if not exists analysis"
            "(id integer primary key autoincrement,"
            "path varchar(100),"
            "fileCount integer,"
            "classCount integer,"
            "attributeCount integer,"
            "methodCount integer)"
        )
        return self.query(sql)
