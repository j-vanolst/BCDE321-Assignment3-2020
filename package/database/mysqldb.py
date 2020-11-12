import mysql.connector

from .database import Database


class MySQLDB(Database):
    def __init__(self, database, address, username, password):
        super().__init__(database, address, username, password)

    def connect(self):
        self.db = mysql.connector.connect(
            host=self.address,
            user=self.username,
            password=self.password,
            database=self.database,
        )

        return True

    def query(self, sql):
        self.connect()
        try:
            cursor = self.db.cursor()
            cursor.execute(sql)
            self.db.commit()
            cursor.close()
            self.db.close()

        except Exception:
            return False

        return True

    def fetch(self, sql):
        self.connect()

        results = []

        try:
            cursor = self.db.cursor()
            cursor.execute(sql)

            for result in cursor.fetchall():
                results.append(result)

            cursor.close()
            self.db.close()

        except Exception:
            return False

        return results

    def setup(self):
        try:
            self.connect()

        except Exception:
            return False

        sql = (
            "create table if not exists analysis "
            "(id integer primary key auto_increment, path varchar(100), "
            "fileCount integer, classCount integer, attributeCount integer, "
            "methodCount integer)"
        )
        if self.db:
            cursor = self.db.cursor()
            cursor.execute(sql)
            self.db.commit()
            cursor.close()
            self.db.close()

        return True
