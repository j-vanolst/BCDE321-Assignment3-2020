from abc import ABCMeta, abstractmethod


class FileABC(metaclass=ABCMeta):
    def __init__(self, name, location, lines):
        self.name = name
        self.location = location
        self.lines = lines
        self.classes = []

    @abstractmethod
    def add_class(self, newClass):
        raise NotImplementedError

    @abstractmethod
    def find_classes(self):
        raise NotImplementedError

    @abstractmethod
    def get_classes(self):
        raise NotImplementedError

    @abstractmethod
    def class_count(self):
        raise NotImplementedError

    @abstractmethod
    def method_count(self):
        raise NotImplementedError

    @abstractmethod
    def attribute_count(self):
        raise NotImplementedError
