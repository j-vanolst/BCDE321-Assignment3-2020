import unittest

from package.cli import Menu

# Import Builders
from package.refactor.menu.menu_director import MenuDirector
from package.refactor.menu.sqlite_menu_builder import SqliteMenuBuilder
from package.refactor.menu.mysql_menu_builder import MySQLMenuBuilder

# Import Database (Before Refactor)
from package.database.mysqldb import MySQLDB


class TestSqliteCli(unittest.TestCase):
    def setUp(self):
        if after_refactor == 1:
            builder = SqliteMenuBuilder()
            director = MenuDirector(builder)
            director.build_menu()
            self.cli = builder.get_menu()
        else:
            self.cli = Menu()

    def tearDown(self):
        self.cli = None

    def test_cli_has_grapher(self):
        result = False
        if self.cli.grapher:
            result = True
        self.assertTrue(result)

    def test_cli_has_database(self):
        result = False
        if self.cli.db:
            result = True
        self.assertTrue(result)

    def test_cli_has_analyser(self):
        result = False
        if self.cli.analyser:
            result = True
        self.assertTrue(result)


class TestMysqlCli(unittest.TestCase):
    def setUp(self):
        if after_refactor == 1:
            builder = MySQLMenuBuilder()
            director = MenuDirector(builder)
            director.build_menu()
            self.cli = builder.get_menu()
        else:
            self.cli = Menu()
            test_database = MySQLDB('bcde321_assignment',
                                    '127.0.0.1', 'root', 'password')
            self.cli.db = test_database

    def tearDown(self):
        self.cli = None

    def test_cli_has_grapher(self):
        result = False
        if self.cli.grapher:
            result = True
        self.assertTrue(result)

    def test_cli_has_database(self):
        result = False
        if self.cli.db:
            result = True
        self.assertTrue(result)

    def test_cli_has_analyser(self):
        result = False
        if self.cli.analyser:
            result = True
        self.assertTrue(result)


if __name__ == '__main__':
    after_refactor = int(
        input('Run refactored version of tests? 1=yes 0=no: '))
    unittest.main(verbosity=2)
