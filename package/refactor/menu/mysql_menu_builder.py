from .menu_builder import MenuBuilder

from package.refactor.database.database import Database
from package.graph.grapher import Grapher
from package.model.analyser import JSAnalyser
from package.refactor.menu.cli import Menu

# Import Database Behaviours
from package.refactor.database.behaviours.setup_behaviour import MySQLSetup
from package.refactor.database.behaviours.query_behaviour import MySQLQuery
from package.refactor.database.behaviours.connect_behaviour import MySQLConnect
from package.refactor.database.behaviours.fetch_behaviour import MySQLFetch


class MySQLMenuBuilder(MenuBuilder):
    def __init__(self):
        super().__init__()

    def build_menu(self):
        # Database
        database = Database(
            "bcde321_assignment", "127.0.0.1", "root", "password"
        )
        database.set_connect_behaviour(MySQLConnect())
        database.set_setup_behaviour(MySQLSetup())
        database.set_query_behaviour(MySQLQuery())
        database.set_fetch_behaviour(MySQLFetch())
        # Grapher
        grapher = Grapher()
        # Analyser
        analyser = JSAnalyser()
        # Menu
        menu = Menu(database, analyser, grapher)

        self.menu = menu

    def get_menu(self):
        return self.menu
