# -*- coding: utf-8 -*-
from . import LanguageDetectorTask
import unittest
import os

class LanguageDetectorTaskTestCase(unittest.TestCase):
    task = None
    name = "LanguageDetector Test Task"

    def setUp(self):
        self.task = LanguageDetectorTask(self.name)

    def tearDown(self):
        self.task = None

    def test_task_initialization_fails_if_name_is_None(self):
        """
        Test that a language detector task throws an exception if the name is None
        """
        name = None

        self.assertRaises(Exception, LanguageDetectorTask, name)

    def test_task_initialization_fails_if_name_is_empty(self):
        """
        Test that a task throws an exception if the name is empty
        """
        name = ""

        self.assertRaises(Exception, LanguageDetectorTask, name)

    def test_task_initialization_with_valid_name(self):
        """
        Test the initialization of the LanguageDetector task
        """
        self.assertIsNotNone(self.task)

    def test_task_execute_with_empty_string(self):
        """
        Test the language detector task with an empty string
        """
        input = ""
        self.task.execute(input)

        actual = self.task.hasFailed()
        self.assertTrue(actual)

    def test_task_execute_with_wrong_input_type(self):
        """
        Test the language detector task with an input that it is not a string
        """
        input = True  # It should be a string
        self.task.execute(input)

        actual = self.task.hasFailed()
        self.assertTrue(actual)

    def test_task_execute_with_input_equals_to_None(self):
        """
        Test the language detector task with an input that it is None
        """
        input = None  # It should be a string
        self.task.execute(input)

        actual = self.task.hasFailed()
        self.assertTrue(actual)

    def test_task_execute_with_english_text(self):
        """
        Test the language detector task with an english text
        """
        input = "This is english"
        result = self.task.execute(input)

        actual = result.get('language', None)
        expected = "en"
        self.assertEquals(expected, actual)

    def test_task_execute_with_norwegian_text(self):
        """
        Test the language detector task with an norwegian text
        """

        input = "Ivar Aasen ble født på gården Åsen i Hovdebygda på Sunnmøre som sønn av småbrukeren Ivar Jonsson."
        result = self.task.execute(input)

        actual = result.get('language', None)
        expected = "no"
        self.assertEquals(expected, actual)
