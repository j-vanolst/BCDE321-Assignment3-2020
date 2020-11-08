from abc import ABCMeta, abstractmethod


class Analyser(metaclass=ABCMeta):
    def __init__(self, path):
        self.path = path
        self.filenames = []
        self.files = []

    @abstractmethod
    def get_filenames(self):
        pass

    @abstractmethod
    def read_files(self):
        pass

    @abstractmethod
    def get_files(self):
        pass

    @abstractmethod
    def get_classes(self):
        pass

    @abstractmethod
    def file_count(self):
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
