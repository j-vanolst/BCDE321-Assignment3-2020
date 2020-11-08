from abc import ABCMeta, abstractmethod


class FileABC(metaclass=ABCMeta):
    def __init__(self, name, location, lines):
        self.name = name
        self.location = location
        self.lines = lines
        self.classes = []

    @abstractmethod
    def add_class(self, newClass):
        pass

    @abstractmethod
    def find_classes(self):
        pass

    @abstractmethod
    def get_classes(self):
        pass

    @abstractmethod
    def class_count(self):
        pass

    @abstractmethod
    def method_count(self):
        pass

    @abstractmethod
    def attribute_count(self):
        pass
