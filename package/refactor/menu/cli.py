from cmd import Cmd
# import argparse

# Argument Parser
# parser = argparse.ArgumentParser()
# parser.add_argument(
#     'dbname',
#     metavar='DB',
#     type=str,
#     default='database.db',
#     nargs='?',
#     help='A database name for storing analyses')
# args = parser.parse_args()


class Menu(Cmd):

    def __init__(self, database, analyser, grapher):
        Cmd.__init__(self)
        self.prompt = ">>> "
        self.db = database
        self.analyser = analyser
        self.grapher = grapher

    def do_add_record(self, path: str):
        """
        Syntax: add_record [path]
        Run an analysis on a file / folder and create a record in the database
        storing file, class, attribute and method counts.
        :param path: a string representing the path to the file / folder for
        analysis
        :return: None
        """
        self.analyser.set_path(path)
        self.analyser.get_filenames()
        self.analyser.read_files()

        file_count = self.analyser.file_count()
        class_count = self.analyser.class_count()
        attribute_count = self.analyser.attribute_count()
        method_count = self.analyser.method_count()

        sql = f'insert into analysis (path, fileCount, classCount,' \
              f' attributeCount, methodCount) values ' \
              f'("{path}", {file_count}, {class_count},' \
              f' {attribute_count}, {method_count})'
        result = self.db.query(sql)

        return result

    def do_get_record(self, path: str):
        """
        Syntax: get_record [path]
        Get an analysis record from the database
        :param path: a string representing the path to the file / folder
        record in the DB
        :return: None
        """
        sql = f'select path, fileCount, classCount, attributeCount,' \
              f' methodCount from analysis where path="{path}"'
        results = self.db.fetch(sql)
        if (len(results) == 0):
            print(f'No records found for path: {path}...')
        else:
            for aResult in results:
                print(f'Path: {aResult[0]}\n'
                      f'File Count: {aResult[1]}\n'
                      f'Class Count: {aResult[2]}\n'
                      f'Attribute Count: {aResult[3]}\n'
                      f'Method Count: {aResult[4]}')
        return results

    def do_delete_record(self, path: str):
        """
        Syntax: delete_record [path]
        Remove an analysis record from the database
        :param path: a string representing the path of the
        file / folder record in the DB
        :return: None
        """
        sql = f'delete from analysis where path="{path}"'
        result = self.db.query(sql)
        
        return result

    def do_list_records(self, line):
        """
        Syntax: list_records
        Lists all stored analysis records in the database
        :return: None
        """
        sql = f'select path from analysis'
        results = self.db.fetch(sql)
        if (len(results) == 0):
            print('No records in the database...')
        else:
            for aResult in results:
                print(aResult)
        
        return results

    def do_analyse(self, path: str):
        """
        Syntax: analyse [path]
        Run an analysis on a file / folder
        :param path: a string representing the path to the
        file / folder for analysis
        :return: None
        """
        self.analyser.set_path(path)
        self.analyser.get_filenames()
        self.analyser.read_files()
        print(self.analyser)

        return True

    def do_draw_class_diagram(self, path: str):
        """
        Syntax: draw_class_diagram [path]
        Render a PDF class diagram of an es6 file / folder
        :param path: a string representing the path to the
        file / folder for analysis
        :return: None
        """
        self.analyser.set_path(path)
        self.analyser.get_filenames()
        self.analyser.read_files()

        classes = self.analyser.get_classes()
        self.grapher.set_classes(classes)

        self.grapher.configure_labels()
        self.grapher.add_nodes()
        self.grapher.render()

        return True

    def do_quit(self, line):
        print("Quitting...")
        return True
