from abc import ABCMeta, abstractmethod


class MenuBuilder(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        self.menu = None

    @abstractmethod
    def build_menu(self):
        raise NotImplementedError

    @abstractmethod
    def get_menu(self):
        raise NotImplementedError
