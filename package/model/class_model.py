import re

from model.abc.classABC import ClassABC
from model.method import Method

method_regex = r'^\s*[a-zA-Z0-9]+(\(){1}[a-zA-Z0-9,\s]*(\)){1}(?=\s\{)'
attribute_regex = r'(?<=this\.)[a-zA-Z0-9]*(?=\s=\s[a-zA-Z0-9\[\]\{\}])'


class Class(ClassABC):
    '''Represents a class object, contains a name,
    a list of methods and a list of attributes'''

    def __init__(self, name, lines):
        super().__init__(name, lines)
        self.methods = []
        self.attributes = []

        self.find_methods()
        self.find_attributes()

    def add_method(self, newMethod):
        self.methods.append(newMethod)

    def find_methods(self):
        '''Uses regular expressions to locate method definitions
        within a JavaScript file'''
        for aLine in self.lines:
            re_match = re.search(method_regex, aLine)
            if (re_match):
                newMethod = Method(re_match.group().strip())
                self.add_method(newMethod)

    def add_attribute(self, newAttribute):
        self.attributes.append(newAttribute)

    def find_attributes(self):
        '''Uses regular expressions to locate attribute definitions
        within a JavaScript file'''
        for aLine in self.lines:
            re_match = re.search(attribute_regex, aLine)
            if (re_match):
                self.add_attribute(re_match.group())

    def get_name(self):
        return self.name

    def get_attributes(self):
        return self.attributes

    def get_methods(self):
        return self.methods

    def method_count(self):
        return len(self.methods)

    def attribute_count(self):
        return len(self.attributes)

    def __str__(self):
        output_string = ''
        output_string += f'\t{self.name}\n'
        output_string += f'\t{len(self.attributes)} Attribute(s):\n'
        for aAttribute in self.attributes:
            output_string += f'\t\t{aAttribute}\n'

        output_string += f'\t{len(self.methods)} Method(s):\n'
        for aMethod in self.methods:
            output_string += f'\t\t{str(aMethod)}\n'

        return output_string
