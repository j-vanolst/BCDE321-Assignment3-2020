class Database():

    def __init__(self):
        self.database = 'test.db'
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

    def setup(self):
        self.setup_behaviour.setup(self)

    def query(self, sql):
        self.query_behaviour.query(self, sql)

    def connect(self):
        self.connect_behaviour.connect(self)
