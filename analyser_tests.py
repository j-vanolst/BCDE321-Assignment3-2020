import unittest

from package.model.analyser import JSAnalyser


class TestAnalyser(unittest.TestCase):
    def setUp(self):
        self.analyser = JSAnalyser(path="package/sample-es6/src/js")
        self.analyser.get_filenames()
        self.analyser.read_files()

    def tearDown(self):
        self.analyser = None

    def test_analyser_set_path(self):
        self.analyser.set_path("test/")
        result = self.analyser.path
        expected = "test/"
        self.assertEqual(result, expected)

    def test_analyser_get_filenames(self):
        self.analyser.get_filenames()
        result = self.analyser.filenames
        expected = [
            "package/sample-es6/src/js\\drag.js",
            "package/sample-es6/src/js\\html.js",
            "package/sample-es6/src/js\\main.js",
            "package/sample-es6/src/js\\utils.js",
        ]
        self.assertEqual(result, expected)

    def test_analyser_get_filenames_with_file(self):
        self.analyser.set_path("package/sample-es6/src/js/drag.js")
        self.analyser.get_filenames()
        result = self.analyser.filenames
        expected = ["package/sample-es6/src/js/drag.js"]
        self.assertEqual(result, expected)

    def test_analyser_get_filenames_incorrect(self):
        self.analyser.set_path("incorrect path")
        self.analyser.get_filenames()
        result = self.analyser.filenames
        expected = []
        self.assertEqual(result, expected)

    def test_analyser_read_files_fail(self):
        self.analyser.filenames.append("incorrect file name")
        result = self.analyser.read_files()
        self.assertFalse(result)

    def test_analyser_get_files(self):
        result = len(self.analyser.get_files())
        expected = 4
        self.assertEqual(result, expected)

    def test_analyser_get_classes(self):
        result = []
        for aClass in self.analyser.get_classes():
            result.append(aClass.get_name())
        expected = ["Drag", "Html", "Base"]
        self.assertEqual(result, expected)

    def test_analyser_file_count(self):
        result = self.analyser.file_count()
        expected = 4
        self.assertEqual(result, expected)

    def test_analyser_class_count(self):
        result = self.analyser.class_count()
        expected = 3
        self.assertEqual(result, expected)

    def test_analyser_method_count(self):
        result = self.analyser.method_count()
        expected = 6
        self.assertEqual(result, expected)

    def test_analyser_attribute_count(self):
        result = self.analyser.attribute_count()
        expected = 2
        self.assertEqual(result, expected)

    def test_analyser_to_string(self):
        result = str(self.analyser)
        expected = type("string")
        self.assertEqual(type(result), expected)

    def test_class_model_get_attributes(self):
        result = []
        for aClass in self.analyser.get_classes():
            if len(aClass.get_attributes()) > 0:
                result.append(aClass.get_attributes())
        expected = [["Base"], ["container"]]
        self.assertEqual(result, expected)

    def test_class_model_get_methods(self):
        result = []
        for aClass in self.analyser.get_classes():
            for aMethod in aClass.get_methods():
                result.append(aMethod.get_name())
        expected = [
            "constructor(base)",
            "constructor(base)",
            "createContainer()",
            "htmlTest()",
            "constructor()",
            "baseTest()",
        ]
        self.assertEqual(result, expected)

    def test_file_model_multiple_classes(self):
        self.analyser.set_path(
            "package/unit-tests/test_files/single_file_multiple_class.js"
        )
        self.analyser.get_filenames()
        self.analyser.read_files()
        result = []
        for aClass in self.analyser.get_classes():
            result.append(aClass.get_name())
        expected = ["Animal", "Insect"]
        self.assertEqual(result, expected)

    def test_method_model_get_parameters(self):
        result = []
        for aClass in self.analyser.get_classes():
            for aMethod in aClass.get_methods():
                for aParameter in aMethod.get_parameters():
                    result.append(aParameter)
        expected = ["base", "base"]
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
