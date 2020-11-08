from model.abc.methodABC import MethodABC


class Method(MethodABC):
    '''Represents a method object, contains a name
    and a list of parameters'''

    def __init__(self, name):
        super().__init__(name)
        self.parameters = []

        self.find_parameters()

    def add_parameter(self, newParameter):
        self.parameters.append(newParameter)

    def find_parameters(self):
        '''Separates method parameters from a method definition
        and adds them to the parameter list'''
        open_bracket_index = self.name.index('(')
        close_bracket_index = self.name.index(')')
        parameters = []
        if (close_bracket_index - open_bracket_index > 1):
            parameters = self.name[open_bracket_index + 1:close_bracket_index]
            parameters = parameters.split(',')
        for aParameter in parameters:
            self.add_parameter(aParameter.strip())

    def get_name(self):
        return self.name

    def get_parameters(self):
        return self.parameters

    def __str__(self):
        output_string = ''
        output_string += f'{self.name}\n'

        output_string += f'\t\t{len(self.parameters)} Parameter(s):\n'
        for aParameter in self.parameters:
            output_string += f'\t\t\t{aParameter}\n'

        return output_string
