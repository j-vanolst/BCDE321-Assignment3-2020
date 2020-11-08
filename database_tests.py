import unittest
from os import remove

# Import Database Model
from package.database.sqlitedb import SqliteDB
from package.database.mysqldb import MySQLDB


class TestSqliteDatabase(unittest.TestCase):
    def setUp(self):
        self.database = SqliteDB('unittest.db')

    def tearDown(self):
        self.database = None
        try:
            remove('unittest.db')
        except:
            print('Nothing to remove')

    def test_database_setup(self):
        result = self.database.setup()
        self.assertTrue(result)

    def test_database_connect(self):
        result = self.database.connect()
        self.assertTrue(result)

    def test_database_query_fail(self):
        sql = "incorrect query"
        result = self.database.query(sql)
        self.assertFalse(result)

    def test_database_insert(self):
        self.database.setup()
        sql = "insert into analysis (path, fileCount, classCount, attributeCount, methodCount) values ('test/', 1, 2, 3, 4)"
        result = self.database.query(sql)
        self.assertTrue(result)

    def test_database_fetch(self):
        self.database.setup()
        sql = "insert into analysis (path, fileCount, classCount, attributeCount, methodCount) values ('test/', 1, 2, 3, 4)"
        self.database.query(sql)
        sql = "select * from analysis where path = 'test/'"
        result = self.database.fetch(sql)[0]
        expected = (1, 'test/', 1, 2, 3, 4)
        self.assertEqual(result, expected)

    def test_database_fetch_fail(self):
        sql = "incorrect fetch"
        result = self.database.fetch(sql)
        self.assertFalse(result)

    def test_database_str(self):
        result = str(self.database)
        expected = 'Database: unittest.db Address: None Username: None Password: None'
        self.assertEqual(result, expected)


class TestMySQLDatabase(unittest.TestCase):
    def setUp(self):
        self.database = MySQLDB('bcde321_assignment',
                                '127.0.0.1', 'root', 'password')

    def tearDown(self):
        self.database = None

    def test_database_connect(self):
        result = self.database.connect()
        self.assertTrue(result)

    def test_database_setup(self):
        result = self.database.setup()
        self.assertTrue(result)

    def test_database_setup_fail(self):
        self.database.password = 'incorrect'
        result = self.database.setup()
        self.assertFalse(result)

    def test_database_query_fail(self):
        sql = "incorrect query"
        result = self.database.query(sql)
        self.assertFalse(result)

    def test_database_insert(self):
        sql = "insert into analysis (path, fileCount, classCount, attributeCount, methodCount) values ('test/', 1, 2, 3, 4)"
        result = self.database.query(sql)
        self.assertTrue(result)

    def test_database_fetch_fail(self):
        sql = "incorrect fetch"
        result = self.database.fetch(sql)
        self.assertFalse(result)

    def test_database_fetch(self):
        delete_sql = "delete * from analysis"
        self.database.query(delete_sql)
        insert_sql = "insert into analysis (path, fileCount, classCount, attributeCount, methodCount) values ('test/', 1, 2, 3, 4)"
        self.database.query(insert_sql)
        fetch_sql = "select * from analysis where path = 'test/'"
        result = self.database.fetch(fetch_sql)[0]
        expected = (1, 'test/', 1, 2, 3, 4)
        self.assertEqual(result, expected)

    def test_database_str(self):
        result = str(self.database)
        expected = 'Database: bcde321_assignment Address: 127.0.0.1 Username: root Password: password'
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)
