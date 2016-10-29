# -*- coding: utf-8 -*-
from . import WordTokenizerTask
import unittest
import os

class WordTokenizerTaskTestCase(unittest.TestCase):
    task = None
    currentDirectory = "%s" % (os.path.dirname(os.path.realpath(__file__)), )
    directory = "%s/../../data/text/" % (currentDirectory,)

    name = "Word Tokenizer Task"

    def setUp(self):
        self.task = WordTokenizerTask(name="Word Tokenizer task")

    def tearDown(self):
        self.task = None

    def test_task_initialization_fails_if_name_is_None(self):
        """
        Test that a Word Tokenizer  Task task throws an exception if the name is None
        """
        self.assertRaises(Exception, WordTokenizerTask, None)

    def test_task_initialization_fails_if_name_is_empty(self):
        """
        Test that a Word Tokenizer  Task task throws an exception if the name is Empty
        """
        self.assertRaises(Exception, WordTokenizerTask, "")

    def test_task_initialization(self):
        """
        Test that a Word Tokenizer  Task task is not None
        """
        self.assertIsNotNone(self.task)

    def test_task_tokenize_text_fails_if_sentences_is_none(self):
        """
        Test the this task fails if the input is none
        """
        text = self.helper_readFilename('en/article1.txt')
        input = {"sentences":None}
        self.task.execute(input)

        self.assertTrue(self.task.hasFailed())

    def test_task_tokenize_text_fails_if_sentences_is_not_list(self):
        """
        Test the this task fails if the input is not a list of sentences
        """
        text = self.helper_readFilename('en/article1.txt')
        input = {"sentences":text}
        self.task.execute(input)

        self.assertTrue(self.task.hasFailed())

    def test_task_tokenize_text(self):
        """
        Test the this task is tokenizing the text correctly
        """
        input = {"sentences":["This is a sentence."]}

        expected = {'data': [['This', 'is', 'a', 'sentence', '.']]}
        actual = self.task.execute(input)

        self.assertEqual(expected, actual)



    def helper_readFilename(self, filename=''):
        if not filename:
            raise Exception("The file is empty")

        fileToRead = "%s%s" % (self.directory, filename)

        f = open(fileToRead, 'r')
        text = f.read()
        f.close()

        return text
