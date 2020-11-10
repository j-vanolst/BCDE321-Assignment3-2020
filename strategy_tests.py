from package.refactor.database.database import Database
from package.refactor.database.behaviours.setup_behaviour import SqliteSetup, MySQLSetup
from package.refactor.database.behaviours.query_behaviour import SqliteQuery, MySQLQuery
from package.refactor.database.behaviours.connect_behaviour import SqliteConnect, MySQLConnect
from package.refactor.database.behaviours.fetch_behaviour import SqliteFetch, MySQLFetch

if __name__ == '__main__':
    ### Sqlite Database ###
    # database = Database('test.db')
    # database.set_setup_behaviour(SqliteSetup())
    # database.set_connect_behaviour(SqliteConnect())
    # database.set_query_behaviour(SqliteQuery())
    # database.set_fetch_behaviour(SqliteFetch())

    # database.setup()
    # database.query(
    #     "insert into analysis (path, fileCount, classCount, attributeCount, methodCount) values ('test/', 1, 2, 3, 4)")
    # results = database.fetch("select * from analysis where path = 'test/'")
    # print(results)
    # remove_sql = "delete from analysis where path = 'test/'"
    # database.query(remove_sql)
    # database.query(
    #     "insert into analysis (path, fileCount, classCount, attributeCount, methodCount) values ('test/', 1, 2, 3, 4)")
    # results = database.fetch("select * from analysis where path = 'test/'")
    # print(results)

    ### MySQL Database ###
    # database = Database('bcde321_assignment', '127.0.0.1', 'root', 'password')
    # database.set_setup_behaviour(MySQLSetup())
    # database.set_connect_behaviour(MySQLConnect())
    # database.set_query_behaviour(MySQLQuery())
    # database.set_fetch_behaviour(MySQLFetch())

    # database.setup()

    # sql = "insert into analysis (path, fileCount, classCount, attributeCount, methodCount) values ('test/', 1, 2, 3, 4)"
    # database.query(sql)
    # fetch_sql = "select * from analysis where path = 'test/'"
    # results = database.fetch(fetch_sql)
    # print(results)
    # delete_sql = "delete from analysis where path = 'test/'"
    # database.query(delete_sql)
    # results = database.fetch(fetch_sql)
    # print(results)
    print(0)
