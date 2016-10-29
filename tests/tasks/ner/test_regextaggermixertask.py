
from . import RegexTaggerMixerTask
import unittest
import os

class RegexTaggerMixerTaskTestCase(unittest.TestCase):
    task = None
    name = "Regex Tagger Mixer Test Task"
    currentDirectory = currentDirectory = "%s" % (os.path.dirname(os.path.realpath(__file__)), )
    testTextsDirectory = "%s/../../data/text/" % (currentDirectory, )


    def setUp(self):
        self.task = RegexTaggerMixerTask(self.name)

    def tearDown(self):
        self.task = None

    def test_task_initialization_fails_if_name_is_None(self):
        """
        Test that a task throws an exception if the name is None
        """
        name = None

        self.assertRaises(Exception, RegexTaggerMixerTask, name)

    def test_task_initialization_fails_if_name_is_empty(self):
        """
        Test that a task throws an exception if the name is empty
        """
        name = ""

        self.assertRaises(Exception, RegexTaggerMixerTask, name)

    def test_task_initialization_with_valid_name(self):
        """
        Test the initialization of RegexTaggerMixerTask
        """
        self.assertIsNotNone(self.task)


    def test_task_execute_with_valid_input(self):
        """
        Test that the RegexTaggerMixerTask is extracting data from the json
        """
        text = """
        This is Moody javascript in Tokyo and PL/SQL in C# and Transact-SQL
        """
        input = {
            "tagger1":[{"entity": "Javascript", "tags":["Language"]}],
            "tagger2":[{"entity": "Javascript", "tags":["Programming Language"]}]
        }
        self.task = RegexTaggerMixerTask(self.name)
        self.task.execute(input)

        actual = self.task.getOutput()
        expected = {'data': [{'entity': 'Javascript', 'tags': ['LANGUAGE', 'PROGRAMMING LANGUAGE']}]}
        self.assertEquals(expected, actual)

    def test_task_execute_with_valid_input_with_several_keys(self):
        """
        Test that the RegexTaggerMixerTask is mixing data from several taggers; There are multiple keys
        """
        text = """
        This is Moody javascript in Tokyo and PL/SQL in C# and Transact-SQL
        """
        input = {
            "tagger1":[{"entity": "Javascript", "tags":["Language"]}],
            "tagger2":[{"entity": "Javascript", "tags":["Programming Language"]}, {"entity":"SQL", "tags":["Databases"]}]
        }
        self.task = RegexTaggerMixerTask(self.name)
        self.task.execute(input)

        actual = self.task.getOutput()
        expected = {'data': [
            {'tags': ['LANGUAGE', 'PROGRAMMING LANGUAGE'], 'entity': 'Javascript'},
            {'tags': ['DATABASES'], 'entity': 'Sql'}
        ]}
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
