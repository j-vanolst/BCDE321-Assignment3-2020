from abc import ABCMeta, abstractmethod


class Database():
    def __init__(self):
        self.setupBehavior = None
        self.queryBehaviour = None
        self.fetchBehaviour = None

    def setInitBehaviour(self, initBehaviour):
        self.initBehavior = initBehaviour

    def setQueryBehaviour(self, queryBehaviour):
        self.queryBehaviour = queryBehaviour

    def setResultBehaviour(self, resultBehaviour):
        self.resultBehaviour = resultBehaviour

    def init(self):
        self.initBehavior.init()

    def query(self, sql):
        self.queryBehaviour.query(sql)

    def result(self, sql):
        self.resultBehaviour.result(sql)


class SetupBehaviour(metaclass=ABCMeta):
    @abstractmethod
    def init(self):
        pass


class SqliteSetup(SetupBehaviour):
    def init(self):
        print('Sqlite Init')


class MySQLSetup(SetupBehaviour):
    def init(self):
        print('MySQL Init')


class QueryBehaviour(metaclass=ABCMeta):
    @abstractmethod
    def query(self, sql):
        pass


class SqliteQuery(QueryBehaviour):
    def query(self, sql):
        print('Sqlite Query')


class MySQLQuery(QueryBehaviour):
    def query(self, sql):
        print('MySQL Query')


class FetchBehaviour(metaclass=ABCMeta):
    @abstractmethod
    def result(self, sql):
        pass


class SqliteFetch(FetchBehaviour):
    def result(self, sql):
        print('Sqlite Result')


class MySQLFetch(FetchBehaviour):
    def result(self, sql):
        print('MySQL Result')


if __name__ == '__main__':
