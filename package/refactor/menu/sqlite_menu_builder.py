from .menu_builder import MenuBuilder

from package.database.sqlitedb import SqliteDB
from package.graph.grapher import Grapher
from package.model.analyser import JSAnalyser
from package.cli import Menu

class SqliteMenuBuilder(MenuBuilder):
    def __init__(self):
        super().__init__()
        
    def build_menu(self):
        menu = Menu()
        database = SqliteDB('unittest.db')
        grapher = Grapher()
        analyser = JSAnalyser()

        menu.db = database
        menu.grapher = grapher
        menu.analyser = analyser

        self.menu = menu
        
    def get_menu(self):
        return self.menu

