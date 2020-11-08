import os
import re
import glob

from model.abc.analyserABC import Analyser
from model.file import File

filename_regex = r'(?<=[a-zA-Z0-9])*[a-zA-Z0-9]+\.[a-zA-Z0-9]*'


class JSAnalyser(Analyser):

    def __init__(self, path):
        super().__init__(path)
        self.filenames = []
        self.files = []

        self.get_filenames()
        self.read_files()

    def get_filenames(self):
        '''Returns a list of all javascript files recursively
        from a given path'''
        # Check if the supplied path is a folder or a directory
        if os.path.isdir(self.path):
            # print(f'Finding JavaScript files in: {self.path}...')
            for folder in os.walk(self.path):
                for filename in glob.glob(os.path.join(folder[0], '*.js')):
                    self.filenames.append(filename)
            # filenames = '\n\t'
            # print(
                # f'Found {len(self.filenames)} JavaScript
                # file(s):\n\t{filenames.join(self.filenames)}')
        elif os.path.isfile(self.path):
            # print(f'Analyzing JavaScript file: {self.path}')
            self.filenames.append(self.path)
        else:
            print(f'Invalid path: {self.path}')

    def read_files(self):
        '''Returns a list of all lines in a specified file'''
        for aFilename in self.filenames:
            try:
                file = open(aFilename, 'r')
                lines = file.read().split('\n')
                file.close()
            except (OSError, IOError):
                print(
                    f'File: {os.path.join(os.path.abspath(self.path))}'
                    f' not found.')
                lines = []

            if (file):
                location = os.path.join(os.path.abspath(aFilename))
                re_match = re.search(filename_regex, aFilename)
                filename = re_match.group()

                new_file = File(filename, location, lines)
                self.files.append(new_file)

    def get_files(self):
        return self.files

    def get_classes(self):
        classes = []
        for aFile in self.files:
            for aClass in aFile.get_classes():
                classes.append(aClass)
        return classes

    def file_count(self):
        return len(self.files)

    def class_count(self):
        class_count = 0
        for aFile in self.files:
            class_count += aFile.class_count()

        return class_count

    def method_count(self):
        method_count = 0
        for aFile in self.files:
            method_count += aFile.method_count()

        return method_count

    def attribute_count(self):
        attribute_count = 0
        for aFile in self.files:
            attribute_count += aFile.attribute_count()

        return attribute_count

    def __str__(self):
        output_string = ''
        for aFile in self.files:
            output_string += str(aFile)
        return output_string
