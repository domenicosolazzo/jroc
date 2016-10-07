# -*- coding: utf-8 -*-
from . import StopwordFilteringTask
import unittest
import os

class StopwordFilteringTaskTestCase(unittest.TestCase):
    task = None
    name = "Stopword Filtering Task"

    def setUp(self):
        self.task = StopwordFilteringTask(name="Stopword filtering task")

    def tearDown(self):
        self.task = None

    def test_task_initialization_fails_if_name_is_None(self):
        """
        Test that a Stopword Filtering Task task throws an exception if the name is None
        """
        self.assertRaises(Exception, StopwordFilteringTask, None)

    def test_task_initialization_fails_if_name_is_empty(self):
        """
        Test that a Stopword Filtering Task task throws an exception if the name is Empty
        """
        self.assertRaises(Exception, StopwordFilteringTask, "")

    def test_task_initialization(self):
        """
        Test that a Stopword Filtering Task task is not None
        """
        self.assertIsNotNone(self.task)


    def test_task_filter_english_words(self):
        """
        Test the filtering of english stopwords
        """
        input = {"data":["The", "New York", "is", "wonderful"]}

        expected = {"data": ["New York", "wonderful"]}
        actual = self.task.execute(input)

        self.assertEqual(expected, actual)

    def test_task_filter_norwegian_words(self):
        """
        Test the filtering of english stopwords
        """
        self.task = StopwordFilteringTask(name="Norwegian Stopword Filtering", language="no")
        input = {"data":["og", "jeg", "det", "Oslo", "venter"]}

        expected = {"data": ["Oslo", "venter"]}
        actual = self.task.execute(input)
        print("actual",actual);

        self.assertEqual(expected, actual)
