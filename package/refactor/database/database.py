from .database_abc import DatabaseABC


class Database(DatabaseABC):

    def __init__(self,
                 database: str,
                 address: str = None,
                 username: str = None,
                 password: str = None):
        self.database = database
        self.address = address
        self.username = username
        self.password = password

        self.db = None
        self.setup_behaviour = None
        self.connect_behaviour = None
        self.query_behaviour = None
        self.fetch_behaviour = None

    def set_setup_behaviour(self, setup_behaviour):
        self.setup_behaviour = setup_behaviour

    def set_query_behaviour(self, query_behaviour):
        self.query_behaviour = query_behaviour

    def set_connect_behaviour(self, connect_behaviour):
        self.connect_behaviour = connect_behaviour

    def set_fetch_behaviour(self, fetch_behaviour):
        self.fetch_behaviour = fetch_behaviour

    def setup(self):
        return self.setup_behaviour.setup(self)

    def query(self, sql):
        return self.query_behaviour.query(self, sql)

    def connect(self):
        return self.connect_behaviour.connect(self)

    def fetch(self, sql):
        return self.fetch_behaviour.fetch(self, sql)
