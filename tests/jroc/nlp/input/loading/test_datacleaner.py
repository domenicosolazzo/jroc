from . import JSONLoader
import unittest
import os

class JSONLoaderTestCase(unittest.TestCase):
    jsonLoader = None

    def setUp(self):
        self.jsonLoader = None

    def tearDown(self):
        self.jsonLoader = None

    def test_jsonloader_loads_json(self):
        """
        Check if the json loader is loading json
        """
        json_text = "{\"data\": \"hello world\"}"
        expected = "hello world"

        self.jsonLoader = JSONLoader(json_text)
        actual = self.jsonLoader.getData()
        self.assertEqual(expected, actual)

    def test_jsonloader_input_is_not_json(self):
        """
        It should return an exception if the input is not valid json
        """
        json_text = "not json"
        self.assertRaises(ValueError, JSONLoader, json_text)

    def test_jsonloader_input_datakey_missing(self):
        """
        Check if the data key is missing from the json in input
        """
        json_text = "{\"abc\": \"hello world\"}"
        self.jsonLoader = JSONLoader(json_text)
        self.assertRaises(Exception, self.jsonLoader.getData)


    def helper_readFilename(self, filename=''):
        stopwords = []
        if not filename:
            raise Exception("The file is empty")

        fileToRead = "%s%s" % (self.testTextsDirectory, filename)

        f = open(fileToRead, 'r')
        text = f.read()
        f.close()

        return text

if __name__ == '__main__':
    unittest.main()
