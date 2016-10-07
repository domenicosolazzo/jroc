# -*- coding: utf-8 -*-
from . import StopwordRetrievalTask
import unittest
import os

class StopwordRetrievalTaskTestCase(unittest.TestCase):
    task = None
    name = "Stopword Retrieval Task"

    def setUp(self):
        self.task = StopwordRetrievalTask(name="Stopword filtering task")

    def tearDown(self):
        self.task = None

    def test_task_initialization_fails_if_name_is_None(self):
        """
        Test that a Stopword Retrieval Task task throws an exception if the name is None
        """
        self.assertRaises(Exception, StopwordRetrievalTask, None)

    def test_task_initialization_fails_if_name_is_empty(self):
        """
        Test that a Stopword Retrieval Task task throws an exception if the name is empty
        """
        self.assertRaises(Exception, StopwordRetrievalTask, "")

    def test_task_retrieve_english_stopword(self):
        """
        Test retrieve english stopwords
        """
        self.task = StopwordRetrievalTask(name="Stopword filtering task", language="en")
        actual = self.task.execute()
        print("aaaa")

        self.assertTrue(isinstance(actual, dict))
        self.assertIsNotNone(actual)

        stopwords = actual.get('data', None)
        self.assertTrue(isinstance(stopwords, list))

    def test_task_retrieve_norwegian_stopword(self):
        """
        Test retrieve norwegian stopwords
        """
        self.task = StopwordRetrievalTask(name="Norwegian stopwords", language="no")
        actual = self.task.execute()
        self.assertTrue(isinstance(actual, dict))
        self.assertIsNotNone(actual)

        stopwords = actual.get('data', None)
        self.assertTrue(isinstance(stopwords, list))
