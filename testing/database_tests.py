import unittest
from os import remove

# Import Database Model 
from BCDE321_Assignment3_2020.database.sqlitedb import SqliteDB

class TestDatabast(unittest.TestCase):
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
        expected =  (1, 'test/', 1, 2, 3, 4)
        self.assertEqual(result, expected)
    
    def test_database_fetch_fail(self):
        sql = "incorrect fetch"
        result = self.database.fetch(sql)
        self.assertFalse(result)

    def test_database_str(self):
        result = str(self.database)
        expected = 'Database: unittest.db Address: None Username: None Password: None'
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main(verbosity=2)