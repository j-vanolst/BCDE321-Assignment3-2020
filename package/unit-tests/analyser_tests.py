import unittest

from model.analyser import JSAnalyser


class SingleFileSingleClassTest(unittest.TestCase):
    def setUp(self):
        self.analyser = JSAnalyser('test_files/single_file_single_class.js')

    def tearDown(self):
        self.analyser = None

    def test_01(self):
        '''Test the analyser has correctly identified 1 file.'''
        expected_num_files = 1
        actual_num_files = len(self.analyser.get_files())

        self.assertTrue(expected_num_files == actual_num_files, 'Number of files should equal: 1.')

    def test_02(self):
        '''Test the analyser has correctly identified 1 class.'''
        expected_num_classes = 1
        actual_num_classes = 0

        for aFile in self.analyser.get_files():
            actual_num_classes += len(aFile.get_classes())

        self.assertTrue(expected_num_classes == actual_num_classes, 'Number of classes should equal: 1.')

    def test_03(self):
        '''Test the analyser has correctly identified the class called Animal.'''
        expected_class_name = 'Animal'
        actual_class_name = self.analyser.get_files()[0].get_classes()[0].get_name()

        self.assertTrue(expected_class_name == actual_class_name, 'Class name should be: Animal.')

    def test_04(self):
        '''Test the analyser has correctly identified the class attributes name & type.'''
        expected_class_attributes = ['name', 'type']
        actual_class_attributes = self.analyser.get_files()[0].get_classes()[0].get_attributes()

        self.assertTrue(expected_class_attributes == actual_class_attributes, 'Class attributes should be: name & type.')

    def test_05(self):
        '''Test the analyser has correctly identified the class methods constructor & greet.'''
        expected_class_attributes = ['constructor(name, type)', 'greet()']
        actual_class_attributes = []

        for aMethod in self.analyser.get_files()[0].get_classes()[0].get_methods():
            actual_class_attributes.append(aMethod.get_name())

        self.assertTrue(expected_class_attributes == actual_class_attributes, 'Class methods should be: constructor(self, name, type) & greet().')

    def test_06(self):
        '''Test the analyser has correctly identified the method attributes name & type.'''
        expected_method_attributes = ['name', 'type']
        actual_method_parameters = []

        for aParameter in self.analyser.get_files()[0].get_classes()[0].get_methods()[0].get_parameters():
            actual_method_parameters.append(aParameter)

        self.assertTrue(expected_method_attributes == actual_method_parameters, 'Method parameters should be: name & type.')

    def test_07(self):
        '''Test the analyser has correctly identified no method attributes for the greet() method.'''
        expected_method_attributes = []
        actual_method_attributes = self.analyser.get_files()[0].get_classes()[0].get_methods()[1].get_parameters()

        self.assertTrue(expected_method_attributes == actual_method_attributes, 'Method parameters should be an empty list.')

class SingleFileMultipleClassTest(unittest.TestCase):
    def setUp(self):
        self.analyser = JSAnalyser('test_files/single_file_multiple_class.js')

    def tearDown(self):
        self.analyser = None

    def test_01(self):
        '''Test the analyser has correctly identified 1 file.'''
        expected_num_files = 1
        actual_num_files = len(self.analyser.get_files())

        self.assertTrue(expected_num_files == actual_num_files, 'Number of files should equal: 1.')

    def test_02(self):
        '''Test the analyser has correctly identified 2 classes.'''
        expected_num_classes = 2
        actual_num_classes = 0

        for aFile in self.analyser.get_files():
            actual_num_classes += len(aFile.get_classes())

        self.assertTrue(expected_num_classes == actual_num_classes, 'Number of classes should equal: 2.')

    def test_03(self):
        '''Test the analyser has correctly identified the classes Animal & Insect.'''
        expected_class_names = ['Animal', 'Insect']
        actual_class_names = []

        for aClass in self.analyser.get_files()[0].get_classes():
            actual_class_names.append(aClass.get_name())

        self.assertTrue(expected_class_names == actual_class_names, 'Class names should be Animal & Insect.')

class MultipleFileMultipleClassTest(unittest.TestCase):
    def setUp(self):
        self.analyser = JSAnalyser('test_files/multiple_files')

    def tearDown(self):
        self.analyser = None

    def test_01(self):
        '''Test the analyser has correctly identified 2 files.'''
        expected_num_files = 2
        actual_num_files = len(self.analyser.get_files())

        self.assertTrue(expected_num_files == actual_num_files, 'Number of files should equal: 2.')

    def test_02(self):
        '''Test the analyser has correctly identified 2 classes.'''
        expected_num_classes = 2
        actual_num_classes = 0

        for aFile in self.analyser.get_files():
            actual_num_classes += len(aFile.get_classes())

        self.assertTrue(expected_num_classes == actual_num_classes, 'Number of classes should equal: 2.')

    def test_03(self):
        '''Test the analyser has correctly identified the classes Animal & Car.'''
        expected_class_names = ['Animal', 'Car']
        actual_class_names = []

        for aFile in self.analyser.get_files():
            for aClass in aFile.get_classes():
                actual_class_names.append(aClass.get_name())

        self.assertTrue(expected_class_names == actual_class_names, 'Class names should be Animal & Car.')


if __name__ == '__main__':
    unittest.main(verbosity=2)
