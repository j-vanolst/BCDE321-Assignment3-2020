import unittest

from package.refactor.menu.menu_director import MenuDirector
from package.refactor.menu.sqlite_menu_builder import SqliteMenuBuilder

class TestBuilder(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test1(self):
        builder = SqliteMenuBuilder()
        director = MenuDirector(builder)
        director.build_menu()
        menu = builder.get_menu()
        menu.cmdloop()

if __name__ == '__main__':
    unittest.main(verbosity=2)


