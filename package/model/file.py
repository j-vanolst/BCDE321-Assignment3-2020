import re

from package.model.abc.fileABC import FileABC
from package.model.class_model import Class

class_regex = r'(?<=class\s)[a-zA-Z0-9]+((?:extends)?\s[a-zA-Z0-9]+)*(?=\s\{)'


class File(FileABC):
    '''Represents a file object, contains a filename,
    location, file lines and a list of classes'''

    def __init__(self, name, location, lines):
        super().__init__(name, location, lines)
        self.classes = []

        self.find_classes()

    def add_class(self, newClass):
        self.classes.append(newClass)

    def find_classes(self):
        '''Uses regular expressions to locate class definitions
        within a JavaScript file'''
        class_names = []
        class_indexes = []

        for aLine in self.lines:
            re_match = re.search(class_regex, aLine)
            if (re_match):
                class_names.append(re_match.group())
                class_indexes.append(self.lines.index(aLine))

        # If the current file contains multiple class declarations
        # splice the lines
        # according to the start and end line index of the current class
        # declaration
        for i in range(0, len(class_names)):
            if (i < len(class_names) - 1):
                class_start_index = class_indexes[i]
                class_end_index = class_indexes[i + 1]
                lines = self.lines[class_start_index:class_end_index]

                new_class = Class(class_names[i], lines)
                self.add_class(new_class)
            else:
                class_start_index = class_indexes[i]
                lines = self.lines[class_start_index:]

                new_class = Class(class_names[i], lines)
                self.add_class(new_class)

    def get_classes(self):
        return self.classes

    def class_count(self):
        return len(self.classes)

    def method_count(self):
        method_count = 0
        for aClass in self.classes:
            method_count += aClass.method_count()

        return method_count

    def attribute_count(self):
        attribute_count = 0
        for aClass in self.classes:
            attribute_count += aClass.attribute_count()

        return attribute_count

    def __str__(self):
        output_string = '\n'
        output_string += f'Filename: {self.name}\n'
        output_string += f'Location: {self.location}\n'

        output_string += f'{len(self.classes)} Class(es):\n'
        for aClass in self.classes:
            output_string += '\tClass'
            output_string += str(aClass)

        return output_string
