from package.refactor.database.database import Database
from package.refactor.database.behaviours.setup_behaviour import SqliteSetup
from package.refactor.database.behaviours.query_behaviour import SqliteQuery
from package.refactor.database.behaviours.connect_behaviour import SqliteConnect

if __name__ == '__main__':
    database = Database()
    database.set_setup_behaviour(SqliteSetup())
    database.set_connect_behaviour(SqliteConnect())
    database.set_query_behaviour(SqliteQuery())

    database.setup()
