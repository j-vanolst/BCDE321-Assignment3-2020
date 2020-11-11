from abc import ABCMeta, abstractmethod


class Analyser(metaclass=ABCMeta):
    def __init__(self, path='.'):
        self.path = path
        self.filenames = []
        self.files = []

    @abstractmethod
    def get_filenames(self):
        raise NotImplementedError

    @abstractmethod
    def read_files(self):
        raise NotImplementedError

    @abstractmethod
    def get_files(self):
        raise NotImplementedError

    @abstractmethod
    def get_classes(self):
        raise NotImplementedError

    @abstractmethod
    def file_count(self):
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

    @abstractmethod
    def set_path(self, path):
        raise NotImplementedError
