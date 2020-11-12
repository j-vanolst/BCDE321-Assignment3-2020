from abc import ABCMeta, abstractmethod


class DatabaseABC(metaclass=ABCMeta):
    def __init__(
        self,
        database: str,
        address: str = None,
        username: str = None,
        password: str = None,
    ):
        self.database = database
        self.address = address
        self.username = username
        self.password = password
        self.db = None
        self.setup_behaviour = None
        self.connect_behaviour = None
        self.query_behaviour = None
        self.fetch_behaviour = None

    def __str__(self):
        return (
            f"Database: {self.database} Address: {self.address}"
            f" Username: {self.username} Password: {self.password}"
        )

    @abstractmethod
    def set_setup_behaviour(self):
        raise NotImplementedError

    @abstractmethod
    def set_connect_behaviour(self):
        raise NotImplementedError

    @abstractmethod
    def set_query_behaviour(self):
        raise NotImplementedError

    @abstractmethod
    def set_fetch_behaviour(self):
        raise NotImplementedError

    @abstractmethod
    def connect(self):
        raise NotImplementedError

    @abstractmethod
    def query(self, sql: str):
        raise NotImplementedError

    @abstractmethod
    def fetch(self, sql: str):
        raise NotImplementedError

    @abstractmethod
    def setup(self):
        raise NotImplementedError
