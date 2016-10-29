from . import LoaderTask
import unittest
import os

class LoaderTaskTestCase(unittest.TestCase):
    task = None
    name = "Loader Test Task"

    def setUp(self):
        self.task = LoaderTask(self.name)

    def tearDown(self):
        self.task = None

    def test_task_initialization_fails_if_name_is_None(self):
        """
        Test that a task throws an exception if the name is None
        """
        name = None

        self.assertRaises(Exception, LoaderTask, name)

    def test_task_initialization_fails_if_name_is_empty(self):
        """
        Test that a task throws an exception if the name is empty
        """
        name = ""

        self.assertRaises(Exception, LoaderTask, name)


    def test_task_initialization_with_valid_name(self):
        """
        Test the initialization of the LoaderTask
        """
        self.assertIsNotNone(self.task)


    def test_task_execute_with_valid_json(self):
        """
        Test that the LaoderTask is extracting data from the json
        """
        input = {"json": '{"data": "this is data"}'}

        actual = self.task.execute(input)
        expected = {"data": "this is data"}
        self.assertEquals(expected, actual)

    def test_task_execute_with_invalid_json_double_quotes(self):
        """
        Test the Loader Task with a json that contains unescaped double quotes
        """
        input = {"json": '{"data": "This is invalid " because there is an unescaped double quote " "}'}

        expected = "Error loading the json string"
        actual = self.task.execute(input)
        self.assertTrue(self.task.hasFailed())

    def test_task_execute_with_invalid_json_single_quotes(self):
        """
        Test the Loader Task with a json that contains unescaped single quotes
        """
        input = {"json": '{"data": "This is invalid '}

        actual = self.task.execute(input)
        self.assertTrue(self.task.hasFailed())

    def test_task_execute_with_invalid_json_invalid_data(self):
        """
        Test the Loader Task with a json that contains unescaped single quotes
        """
        input = '{"data": This is invalid }'

        actual = self.task.execute(input)
        self.assertTrue(self.task.hasFailed())
