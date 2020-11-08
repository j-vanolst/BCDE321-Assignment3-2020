from abc import ABCMeta, abstractmethod


class ClassABC(metaclass=ABCMeta):
    def __init__(self, name, lines):
        self.name = name
        self.lines = lines
        self.methods = []
        self.attributes = []

    @abstractmethod
    def add_method(self, newMethod):
        pass

    @abstractmethod
    def find_methods(self):
        pass

    @abstractmethod
    def add_attribute(self, newAttribute):
        pass

    @abstractmethod
    def find_attributes(self):
        pass

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_attributes(self):
        pass

    @abstractmethod
    def get_methods(self):
        pass

    @abstractmethod
    def method_count(self):
        pass

    @abstractmethod
    def attribute_count(self):
        pass
