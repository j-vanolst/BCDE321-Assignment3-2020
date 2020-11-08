from abc import ABCMeta, abstractmethod


class MethodABC(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name
        self.parameters = []

    @abstractmethod
    def add_parameter(self, newParameter):
        pass

    @abstractmethod
    def find_parameters(self):
        pass

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_parameters(self):
        pass
