from abc import ABCMeta, abstractmethod


class Cmd():
    def __init__(self):
        self.db = None
        self.analyser = None

    def set_db(self, db):
        self.db = db

    def set_analyser(self, analyser):
        self.analyser = analyser

    def loop(self):
        self.db.print()
        self.analyser.print()
        print('LOOPING...')


class Database():
    def print(self):
        print('Im a database')


class Analyser():
    def print(self):
        print('Im an analyser')


class Director():
    def __init__(self, builder):
        self.builder = builder

    def build_cmd(self):
        self.builder.build_cmd()


class Builder(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        self.cmd = None

    @abstractmethod
    def build_cmd(self):
        pass

    @abstractmethod
    def get_cmd(self):
        pass


class MainBuilder(Builder):
    def __init__(self):
        self.cmd = None

    def build_cmd(self):
        cmd = Cmd()

        db = Database()
        cmd.set_db(db)

        analyser = Analyser()
        cmd.set_analyser(analyser)

        self.cmd = cmd

    def get_cmd(self):
        return self.cmd


if __name__ == '__main__':
    builder = MainBuilder()
    director = Director(builder)

    director.build_cmd()

    cmd = builder.get_cmd()
    cmd.loop()
