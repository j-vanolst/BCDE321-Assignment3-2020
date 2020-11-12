import unittest
from os import remove

from package.model.analyser import JSAnalyser


class TestAnalyser(unittest.TestCase):
    def setUp(self):
        self.analyser = JSAnalyser(path="package/sample-es6/src/js")
        self.analyser.get_filenames()
        self.analyser.read_files()

    def tearDown(self):
        self.analyser = None

    def test_analyser_set_path(self):
        self.analyser.set_path("test/")
        result = self.analyser.path
        expected = "test/"
        self.assertEqual(result, expected)

    def test_analyser_get_filenames(self):
        self.analyser.get_filenames()
        result = self.analyser.filenames
        expected = [
            "package/sample-es6/src/js\\drag.js",
            "package/sample-es6/src/js\\html.js",
            "package/sample-es6/src/js\\main.js",
            "package/sample-es6/src/js\\utils.js",
        ]
        self.assertEqual(result, expected)

    def test_analyser_get_filenames_with_file(self):
        self.analyser.set_path("package/sample-es6/src/js/drag.js")
        self.analyser.get_filenames()
        result = self.analyser.filenames
        expected = ["package/sample-es6/src/js/drag.js"]
        self.assertEqual(result, expected)

    def test_analyser_get_filenames_incorrect(self):
        self.analyser.set_path("incorrect path")
        self.analyser.get_filenames()
        result = self.analyser.filenames
        expected = []
        self.assertEqual(result, expected)

    def test_analyser_read_files_fail(self):
        self.analyser.filenames.append("incorrect file name")
        result = self.analyser.read_files()
        self.assertFalse(result)

    def test_analyser_get_files(self):
        result = len(self.analyser.get_files())
        expected = 4
        self.assertEqual(result, expected)

    def test_analyser_get_classes(self):
        result = []
        for aClass in self.analyser.get_classes():
            result.append(aClass.get_name())
        expected = ["Drag", "Html", "Base"]
        self.assertEqual(result, expected)

    def test_analyser_file_count(self):
        result = self.analyser.file_count()
        expected = 4
        self.assertEqual(result, expected)

    def test_analyser_class_count(self):
        result = self.analyser.class_count()
        expected = 3
        self.assertEqual(result, expected)

    def test_analyser_method_count(self):
        result = self.analyser.method_count()
        expected = 6
        self.assertEqual(result, expected)

    def test_analyser_attribute_count(self):
        result = self.analyser.attribute_count()
        expected = 2
        self.assertEqual(result, expected)

    def test_analyser_to_string(self):
        result = str(self.analyser)
        expected = type("string")
        self.assertEqual(type(result), expected)

    def test_class_model_get_attributes(self):
        result = []
        for aClass in self.analyser.get_classes():
            if len(aClass.get_attributes()) > 0:
                result.append(aClass.get_attributes())
        expected = [["Base"], ["container"]]
        self.assertEqual(result, expected)

    def test_class_model_get_methods(self):
        result = []
        for aClass in self.analyser.get_classes():
            for aMethod in aClass.get_methods():
                result.append(aMethod.get_name())
        expected = [
            "constructor(base)",
            "constructor(base)",
            "createContainer()",
            "htmlTest()",
            "constructor()",
            "baseTest()",
        ]
        self.assertEqual(result, expected)

    def test_file_model_multiple_classes(self):
        self.analyser.set_path(
            "package/unit-tests/test_files/single_file_multiple_class.js"
        )
        self.analyser.get_filenames()
        self.analyser.read_files()
        result = []
        for aClass in self.analyser.get_classes():
            result.append(aClass.get_name())
        expected = ["Animal", "Insect"]
        self.assertEqual(result, expected)

    def test_method_model_get_parameters(self):
        result = []
        for aClass in self.analyser.get_classes():
            for aMethod in aClass.get_methods():
                for aParameter in aMethod.get_parameters():
                    result.append(aParameter)
        expected = ["base", "base"]
        self.assertEqual(result, expected)


class TestSqliteDatabase(unittest.TestCase):
    def setUp(self):
        if after_refactor == 1:
            self.database = Database("unittest.db")
            self.database.set_connect_behaviour(SqliteConnect())
            self.database.set_setup_behaviour(SqliteSetup())
            self.database.set_query_behaviour(SqliteQuery())
            self.database.set_fetch_behaviour(SqliteFetch())
        else:
            self.database = SqliteDB("unittest.db")

    def tearDown(self):
        self.database = None
        try:
            remove("unittest.db")
        except Exception:
            print("Nothing to remove")

    def test_database_setup(self):
        result = self.database.setup()
        self.assertTrue(result)

    def test_database_setup_fail(self):
        self.database.database = "readonly/unittest.db"
        result = self.database.setup()
        self.assertFalse(result)

    def test_database_connect(self):
        result = self.database.connect()
        self.assertTrue(result)

    def test_database_connect_fail(self):
        self.database.database = "readonly/unittest.db"
        result = self.database.connect()
        self.assertFalse(result)

    def test_database_query_fail(self):
        sql = "incorrect query"
        result = self.database.query(sql)
        self.assertFalse(result)

    def test_database_insert(self):
        self.database.setup()
        sql = "insert into analysis "\
            "(path, fileCount, classCount, attributeCount, methodCount) "\
            "values ('test/', 1, 2, 3, 4)"
        result = self.database.query(sql)
        self.assertTrue(result)

    def test_database_fetch(self):
        self.database.setup()
        sql = "insert into analysis "\
            "(path, fileCount, classCount, attributeCount, methodCount) "\
            "values ('test/', 1, 2, 3, 4)"
        self.database.query(sql)
        sql = "select * from analysis where path = 'test/'"
        result = self.database.fetch(sql)[0]
        expected = (1, "test/", 1, 2, 3, 4)
        self.assertEqual(result, expected)

    def test_database_fetch_fail(self):
        sql = "incorrect fetch"
        result = self.database.fetch(sql)
        self.assertFalse(result)

    def test_database_str(self):
        result = str(self.database)
        expected = (
            "Database: unittest.db Address: None Username: None Password: None"
        )
        self.assertEqual(result, expected)


class TestMySQLDatabase(unittest.TestCase):
    def setUp(self):
        if after_refactor == 1:
            self.database = Database(
                "bcde321_assignment", "127.0.0.1", "root", "password"
            )
            self.database.set_connect_behaviour(MySQLConnect())
            self.database.set_setup_behaviour(MySQLSetup())
            self.database.set_query_behaviour(MySQLQuery())
            self.database.set_fetch_behaviour(MySQLFetch())
        else:
            self.database = MySQLDB(
                "bcde321_assignment", "127.0.0.1", "root", "password"
            )

    def tearDown(self):
        self.database = None

    def test_database_connect(self):
        result = self.database.connect()
        self.assertTrue(result)

    def test_database_setup(self):
        result = self.database.setup()
        self.assertTrue(result)

    def test_database_setup_fail(self):
        self.database.password = "incorrect"
        result = self.database.setup()
        self.assertFalse(result)

    def test_database_query_fail(self):
        sql = "incorrect query"
        result = self.database.query(sql)
        self.assertFalse(result)

    def test_database_insert(self):
        sql = "insert into analysis "\
            "(path, fileCount, classCount, attributeCount, methodCount) "\
            "values ('test/', 1, 2, 3, 4)"
        result = self.database.query(sql)
        self.assertTrue(result)

    def test_database_fetch_fail(self):
        sql = "incorrect fetch"
        result = self.database.fetch(sql)
        self.assertFalse(result)

    def test_database_fetch(self):
        delete_sql = "delete * from analysis"
        self.database.query(delete_sql)
        insert_sql = "insert into analysis "\
            "(path, fileCount, classCount, attributeCount, methodCount) "\
            "values ('test/', 1, 2, 3, 4)"
        self.database.query(insert_sql)
        fetch_sql = "select * from analysis where path = 'test/'"
        result = self.database.fetch(fetch_sql)[0]
        expected = (1, "test/", 1, 2, 3, 4)
        self.assertEqual(result, expected)

    def test_database_str(self):
        result = str(self.database)
        expected = "Database: bcde321_assignment Address: 127.0.0.1 "\
            "Username: root Password: password"
        self.assertEqual(result, expected)


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
    after_refactor = int(input("Run refactored version of tests? 1=yes 0=no"))

    if after_refactor == 1:
        # Import Database
        from package.refactor.database.database import Database

        # Import Database Behaviours
        from package.refactor.database.behaviours.setup_behaviour import (
            SqliteSetup,
            MySQLSetup,
        )
        from package.refactor.database.behaviours.query_behaviour import (
            SqliteQuery,
            MySQLQuery,
        )
        from package.refactor.database.behaviours.connect_behaviour import (
            SqliteConnect,
            MySQLConnect,
        )
        from package.refactor.database.behaviours.fetch_behaviour import (
            SqliteFetch,
            MySQLFetch,
        )

        # Import Builders
        from package.refactor.menu.menu_director import MenuDirector
        from package.refactor.menu.sqlite_menu_builder import SqliteMenuBuilder
        from package.refactor.menu.mysql_menu_builder import MySQLMenuBuilder
    else:
        # Import Database
        from package.database.sqlitedb import SqliteDB
        from package.database.mysqldb import MySQLDB

        # Import Menu (Before Refactor)
        from package.cli import Menu

        # Import Database (Before Refactor)
        from package.database.mysqldb import MySQLDB

    unittest.main(verbosity=2)
