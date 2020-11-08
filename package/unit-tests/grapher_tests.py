import filecmp
import unittest

from model.analyser import JSAnalyser
from graph.grapher import Grapher

class SingleFileSingleClassTest(unittest.TestCase):
    def setUp(self):
        self.analyser = JSAnalyser('test_files/single_file_single_class.js')
        self.grapher = Grapher(self.analyser.get_classes())
        self.grapher.render(False)

    def tearDown(self):
        self.analyser = None
        self.grapher = None

    def test_01(self):
        expected = True
        actual = filecmp.cmp('output/output.pdf', 'test_files/single_file_single_class.pdf')

        self.assertTrue(expected == actual, 'Generated output file should match test output file.')

class SingleFileMultipleClassTest(unittest.TestCase):
    def setUp(self):
        self.analyser = JSAnalyser('test_files/single_file_multiple_class.js')
        self.grapher = Grapher(self.analyser.get_classes())
        self.grapher.render(False)

    def tearDown(self):
        self.analyser = None
        self.grapher = None

    def test_02(self):
        expected = True
        actual = filecmp.cmp('output/output.pdf', 'test_files/single_file_multiple_class.pdf')

        self.assertTrue(expected == actual, 'Generated output file should match test output file.')


class MultipleFileMultipleClassTest(unittest.TestCase):
    def setUp(self):
        self.analyser = JSAnalyser('test_files/multiple_files')
        self.grapher = Grapher(self.analyser.get_classes())
        self.grapher.render(False)

    def tearDown(self):
        self.analyser = None
        self.grapher = None

    def test_03(self):
        expected = True
        actual = filecmp.cmp('output/output.pdf', 'test_files/multiple_file_multiple_class.pdf')

        self.assertTrue(expected == actual, 'Generated output file should match test output file.')

if __name__ == '__main__':
    unittest.main(verbosity=2)