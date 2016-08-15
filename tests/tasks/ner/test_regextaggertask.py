
from . import RegexTaggerTask
import unittest
import os

text = ""
json = {
    'entities':[
        {'entity':r'Moody\'s', 'tags':['ORGANIZATION']},
        {'entity':r'Javascript', 'tags':['LANGUAGE']},
        {'entity':r'Java', 'tags':['LANGUAGE']},
        {'entity':r'C#', 'tags':['LANGUAGE']},
        {'entity':r'.*SQL', 'tags':['LANGUAGE']},
        {'entity':r'tokyo', 'tags':['LOCATION']},
        {'entity':r'japan', 'tags':['LOCATION']},
    ],
    'additional_tags':['TEST1']
}
class RegexTaggerTaskTestCase(unittest.TestCase):
    task = None
    name = "Regex Tagger Test Task"
    currentDirectory = currentDirectory = "%s" % (os.path.dirname(os.path.realpath(__file__)), )
    testTextsDirectory = "%s/../../data/text/" % (currentDirectory, )


    def setUp(self):
        self.task = RegexTaggerTask(self.name, data=json, optionals={})

    def tearDown(self):
        self.task = None

    def test_task_initialization_fails_if_name_is_None(self):
        """
        Test that a task throws an exception if the name is None
        """
        name = None

        self.assertRaises(Exception, RegexTaggerTask, name)

    def test_task_initialization_fails_if_name_is_empty(self):
        """
        Test that a task throws an exception if the name is empty
        """
        name = ""

        self.assertRaises(Exception, RegexTaggerTask, name)

    def test_task_initialization_with_valid_name(self):
        """
        Test the initialization of theRegexTaggerTask
        """
        self.assertIsNotNone(self.task)

    def test_task_execute_with_input_without_main_key(self):
        """
        Test that the RegexTaggerTask fails if a requested key is missing (pos-no)
        """
        input = {}
        self.task.execute(input)
        self.assertTrue(self.task.hasFailed())

    def test_task_execute_with_valid_json(self):
        """
        Test that the RegexTaggerTask is extracting data from the json
        """
        text = """
        This is Moody javascript in Tokyo and PL/SQL in C# and Transact-SQL
        """
        input = {"data": text}
        self.task = RegexTaggerTask(self.name, data=json, optionals={})
        self.task.execute(input)

        actual = self.task.getOutput()
        expected = {'data': [{'entity': 'javascript', 'tags': ['TEST1', 'LANGUAGE']},
           {'entity': 'Tokyo', 'tags': ['TEST1', 'LOCATION']},
           {'entity': 'PL/SQL', 'tags': ['TEST1', 'LANGUAGE']},
           {'entity': 'SQL', 'tags': ['TEST1', 'LANGUAGE']},
           {'entity': 'C#', 'tags': ['TEST1', 'LANGUAGE']},
           {'entity': 'Transact-SQL', 'tags': ['TEST1', 'LANGUAGE']},
           {'entity': 'SQL', 'tags': ['TEST1', 'LANGUAGE']}]}
        self.assertEquals(expected, actual)



    def helper_readFilename(self, filename=''):
        stopwords = []
        if not filename:
            raise Exception("The file is empty")

        fileToRead = "%s%s" % (self.testTextsDirectory, filename)

        with open(fileToRead) as f:
            text = f.read()
        #f.close()
        return text
