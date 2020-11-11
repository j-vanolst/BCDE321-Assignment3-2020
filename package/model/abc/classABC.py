from abc import ABCMeta, abstractmethod


class ClassABC(metaclass=ABCMeta):
    def __init__(self, name, lines):
        self.name = name
        self.lines = lines
        self.methods = []
        self.attributes = []

    @abstractmethod
    def add_method(self, newMethod):
        raise NotImplementedError

    @abstractmethod
    def find_methods(self):
        raise NotImplementedError

    @abstractmethod
    def add_attribute(self, newAttribute):
        raise NotImplementedError

    @abstractmethod
    def find_attributes(self):
        raise NotImplementedError

    @abstractmethod
    def get_name(self):
        raise NotImplementedError

    @abstractmethod
    def get_attributes(self):
        raise NotImplementedError

    @abstractmethod
    def get_methods(self):
        raise NotImplementedError

    @abstractmethod
    def method_count(self):
        raise NotImplementedError

    @abstractmethod
    def attribute_count(self):
        raise NotImplementedError
