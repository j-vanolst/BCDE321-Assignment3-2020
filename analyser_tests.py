import unittest

from package.cli import Menu

# Imports for type checking
from package.database.mysqldb import MySQLDB
from package.database.sqlitedb import SqliteDB
from package.graph.grapher import Grapher
from package.model.analyser import JSAnalyser

class TestSqliteCli(unittest.TestCase):
    def setUp(self):
        self.cli = Menu()

    def tearDown(self):
        self.cli = None

    def test_cli_has_grapher(self):
        result = type(self.cli.grapher)
        expected = type(Grapher())
        self.assertEqual(result, expected)
    
    def test_cli_has_sqlite_database(self):
        result = type(self.cli.db)
        expected = type(SqliteDB('unittest.db'))
        self.assertEqual(result, expected)
    
    def test_cli_has_js_analyser(self):
        result = type(self.cli.analyser)
        expected = type(JSAnalyser())
        self.assertEqual(result, expected)

class TestMysqlCli(unittest.TestCase):
    def setUp(self):
        self.cli = Menu()
        test_database = MySQLDB('bcde321_assignment', '127.0.0.1', 'root', 'password')
        self.cli.db = test_database

    def tearDown(self):
        self.cli = None

    def test_cli_has_grapher(self):
        result = type(self.cli.grapher)
        expected = type(Grapher())
        self.assertEqual(result, expected)

    def test_cli_has_mysql_database(self):
        result = type(self.cli.db)
        expected = type(MySQLDB('', '', '', ''))  
        self.assertEqual(result, expected)

    def test_cli_has_js_analyser(self):
        result = type(self.cli.analyser)
        expected = type(JSAnalyser())
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main(verbosity=2)