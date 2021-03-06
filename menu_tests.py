import unittest
from os import remove


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
        try:
            remove("unittest.db")
        except Exception:
            print("Nothing to remove")

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

    def test_menu_add_record(self):
        result = self.cli.do_add_record("package/sample-es6/src/js")
        self.assertTrue(result)

    def test_menu_get_record(self):
        self.cli.do_add_record("package/sample-es6/src/js")
        result = self.cli.do_get_record("package/sample-es6/src/js")
        expected = [("package/sample-es6/src/js", 4, 3, 2, 6)]
        self.assertEqual(result, expected)

    def test_menu_get_record_no_results(self):
        result = self.cli.do_get_record("empty path")
        expected = []
        self.assertEqual(result, expected)

    def test_menu_delete_record(self):
        self.cli.do_add_record("package/sample-es6/src/js")
        result = self.cli.do_delete_record("package/sample-es6/src/js")
        self.assertTrue(result)

    def test_menu_list_records(self):
        self.cli.do_add_record("package/sample-es6/src/js")
        result = self.cli.do_list_records("")
        expected = [("package/sample-es6/src/js",)]
        self.assertEqual(result, expected)

    def test_menu_list_records_no_results(self):
        result = self.cli.do_list_records("")
        expected = []
        self.assertEqual(result, expected)

    def test_menu_analyse(self):
        result = self.cli.do_analyse("package/sample-es6/src/js")
        self.assertTrue(result)

    def test_menu_draw_class_diagram(self):
        result = self.cli.do_draw_class_diagram("package/sample-es6/src/js")
        self.assertTrue(result)

    def test_menu_draw_class_diagram_empty(self):
        result = self.cli.do_draw_class_diagram("empty path")
        self.assertTrue(result)

    def test_menu_quit(self):
        result = self.cli.do_quit("")
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
            test_database = MySQLDB(
                "bcde321_assignment", "127.0.0.1", "root", "password"
            )
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


if __name__ == "__main__":
    after_refactor = int(
        input("Run refactored version of tests? 1=yes 0=no: ")
    )
    if after_refactor == 1:
        # Import Builders
        from package.refactor.menu.menu_director import MenuDirector
        from package.refactor.menu.sqlite_menu_builder import SqliteMenuBuilder
        from package.refactor.menu.mysql_menu_builder import MySQLMenuBuilder
    else:
        # Import Menu (Before Refactor)
        from package.cli import Menu

        # Import Database (Before Refactor)
        from package.database.mysqldb import MySQLDB

    unittest.main(verbosity=2)
