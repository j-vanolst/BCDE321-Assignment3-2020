from abc import ABCMeta, abstractmethod


class MethodABC(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name
        self.parameters = []

    @abstractmethod
    def add_parameter(self, newParameter):
        raise NotImplementedError

    @abstractmethod
    def find_parameters(self):
        raise NotImplementedError

    @abstractmethod
    def get_name(self):
        raise NotImplementedError

    @abstractmethod
    def get_parameters(self):
        raise NotImplementedError
