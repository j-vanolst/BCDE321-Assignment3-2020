from .menu_builder import MenuBuilder

from package.refactor.database.database import Database
from package.graph.grapher import Grapher
from package.model.analyser import JSAnalyser
from package.refactor.menu.cli import Menu

# Import Database Behaviours
from package.refactor.database.behaviours.setup_behaviour import SqliteSetup
from package.refactor.database.behaviours.query_behaviour import SqliteQuery
from package.refactor.database.behaviours.connect_behaviour import (
    SqliteConnect,
)
from package.refactor.database.behaviours.fetch_behaviour import SqliteFetch


class SqliteMenuBuilder(MenuBuilder):
    def __init__(self):
        super().__init__()

    def build_menu(self):
        # Menu
        menu = Menu()
        # Database
        database = Database("unittest.db")
        database.set_connect_behaviour(SqliteConnect())
        database.set_setup_behaviour(SqliteSetup())
        database.set_query_behaviour(SqliteQuery())
        database.set_fetch_behaviour(SqliteFetch())
        menu.set_database(database)
        # Grapher
        grapher = Grapher()
        menu.set_grapher(grapher)
        # Analyser
        analyser = JSAnalyser()
        menu.set_analyser(analyser)

        self.menu = menu

    def get_menu(self):
        return self.menu
