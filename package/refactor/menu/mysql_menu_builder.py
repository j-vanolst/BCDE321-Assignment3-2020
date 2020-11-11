from .menu_builder import MenuBuilder

from package.refactor.database.database import Database
from package.graph.grapher import Grapher
from package.model.analyser import JSAnalyser
from package.cli import Menu

# Import Database Behaviours
from package.refactor.database.behaviours.setup_behaviour import MySQLSetup
from package.refactor.database.behaviours.query_behaviour import MySQLQuery
from package.refactor.database.behaviours.connect_behaviour import MySQLConnect
from package.refactor.database.behaviours.fetch_behaviour import MySQLFetch


class MySQLMenuBuilder(MenuBuilder):
    def __init__(self):
        super().__init__()

    def build_menu(self):
        # Menu
        menu = Menu()
        # Database
        database = Database('bcde321_assignment',
                            '127.0.0.1', 'root', 'password')
        database.set_connect_behaviour(MySQLConnect())
        database.set_setup_behaviour(MySQLSetup())
        database.set_query_behaviour(MySQLQuery())
        database.set_fetch_behaviour(MySQLFetch())
        # Grapher
        grapher = Grapher()
        # Analyser
        analyser = JSAnalyser()

        menu.db = database
        menu.grapher = grapher
        menu.analyser = analyser

        self.menu = menu

    def get_menu(self):
        return self.menu
