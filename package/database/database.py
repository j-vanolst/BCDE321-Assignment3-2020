from abc import ABCMeta, abstractmethod


class Database(metaclass=ABCMeta):
    def __init__(
            self,
            database: str,
            address: str = None,
            username: str = None,
            password: str = None):
        self.database = database
        self.address = address
        self.username = username
        self.password = password
        self.db = None

    def __str__(self):
        return f'Database: {self.database} Address: {self.address}' \
               f' Username: {self.username} Password: {self.password}'

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def query(self, sql: str):
        pass

    @abstractmethod
    def fetch(self):
        pass

    @abstractmethod
    def setup(self):
        pass
