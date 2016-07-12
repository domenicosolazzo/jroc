# -*- coding: utf-8 -*-
from . import DataCleanerTask
import unittest
import os

class LoaderTaskTestCase(unittest.TestCase):
    task = None
    name = "Data Cleaner Test Task"

    def setUp(self):
        self.task = DataCleanerTask(self.name)
        #self.task.setMetadataOutput({'key':'data', 'source': 'internal-output', 'type':'json'})

    def tearDown(self):
        self.task = None

    def test_task_datacleaner_initialization_fails_if_name_is_None(self):
        """
        Test that a task throws an exception if the name is None
        """
        name = None

        self.assertRaises(Exception, DataCleanerTask, name)

    def test_task_datacleaner_initialization_fails_if_name_is_empty(self):
        """
        Test that a task throws an exception if the name is empty
        """
        name = ""

        self.assertRaises(Exception, DataCleanerTask, name)

    def test_task_datacleaner_initialization_fails_if_name_is_empty(self):
        """
        Test that a task throws an exception if the name is empty
        """
        name = ""

        self.assertRaises(Exception, DataCleanerTask, name)

    def test_task_datacleaner_initialization_with_valid_name(self):
        """
        Test the initialization of the DataCleanerTask
        """
        self.assertIsNotNone(self.task)

    def test_task_datacleaner_setIsJson_with_invalid_paramenter(self):
        """
        Test the setIsJson method of the DataCleanerTask with an invalid parameter
        """
        self.assertRaises(AssertionError, self.task.setIsJson, "this is a string")

    def test_task_datacleaner_setIsJson(self):
        """
        Test the setIsJson method of the DataCleanerTask
        """
        input = True
        self.task.setIsJson(input)
        actual = self.task._DataCleanerTask__isJsonString
        self.assertTrue(actual)

        input = False
        self.task.setIsJson(input)
        actual = self.task._DataCleanerTask__isJsonString
        self.assertFalse(actual)

    def test_task_dataclenear_setReplacementCharacter_with_invalid_character(self):
        """
        Test the setReplacementCharacter of the DataClenearTask
        """
        self.assertRaises(AssertionError, self.task.setReplacementCharacter, True)

    def test_task_dataclenear_setReplacementCharacter(self):
        """
        Test the setReplacementCharacter of the DataClenearTask
        """
        actual = self.task._DataCleanerTask__replacementCharacter
        expected = " "
        self.assertEquals(expected, actual)

        self.task.setReplacementCharacter("#")
        actual = self.task._DataCleanerTask__replacementCharacter
        expected = "#"
        self.assertEquals(expected, actual)

    def test_task_dataclenear_setRemoveDoubleQuotes_with_invalid_character(self):
        """
        Test the setRemoveDoubleQuotes of the DataClenearTask
        """
        self.assertRaises(AssertionError, self.task.setRemoveDoubleQuotes, "This is a string")

    def test_task_dataclenear_setRemoveDoubleQuotes(self):
        """
        Test the setRemoveDoubleQuotes of the DataClenearTask
        """
        actual = self.task._DataCleanerTask__removeDoubleQuotes
        expected = True
        self.assertEquals(expected, actual)

        self.task.setRemoveDoubleQuotes(False)
        actual = self.task._DataCleanerTask__removeDoubleQuotes
        expected = False
        self.assertEquals(expected, actual)

    def test_task_dataclenear_setFilterCharacters_with_invalid_first_parameter(self):
        """
        Test the setFilterCharacters of the DataClenearTask
        """
        self.assertRaises(AssertionError, self.task.setFilterCharacters, "This is a string", [])

    def test_task_dataclenear_setFilterCharacters_with_invalid_second_parameter(self):
        """
        Test the setFilterCharacters of the DataClenearTask
        """
        self.assertRaises(AssertionError, self.task.setFilterCharacters, True, None)

    def test_task_dataclenear_setFilterCharacters(self):
        """
        Test the setFilterCharacters of the DataClenearTask
        """
        actual = self.task._DataCleanerTask__filterCharacters
        expected = True
        self.assertEquals(expected, actual)

        self.task.setFilterCharacters(False)
        actual = self.task._DataCleanerTask__filterCharacters
        expected = False
        self.assertEquals(expected, actual)

        self.task.setFilterCharacters(True, ["'"])
        actual = self.task._DataCleanerTask__filterCharacters
        expected = True
        self.assertEquals(expected, actual)

        actual = self.task._DataCleanerTask__charactersToFilter
        expected = ["'"]
        self.assertEquals(expected, actual)

    def test_task_datacleaner_execute_input_with_doublequotes_and_json_string(self):
        """
        Test the data cleaner task with an input with double quotes (json string)
        """
        input = '{"data": "Hello " World"}'

        expected = {'data':'{"data": "Hello   World"}'}
        self.task.execute(input)
        actual = self.task.getOutput()

        self.assertEquals(expected, actual)

    def test_task_datacleaner_execute_input_with_doublequotes_and_Not_json_string(self):
        """
        Test the data cleaner task with an input with double quotes but not a json string
        """
        input = 'This is" a string'

        self.task.setIsJson(isJsonString=False)
        self.task.execute(input)

        expected = {'data':"This is  a string"}
        actual = self.task.getOutput()

        self.assertEquals(expected, actual)

    def test_task_datacleaner_execute_input_characters_to_be_filtered(self):
        """
        Test the data cleaner task with an input with characters that should be filtered
        """
        input = "ABC'\n«»*–•-"
        self.task.setIsJson(False)
        self.task.setReplacementCharacter("")
        self.task.execute(input)

        expected = {'data':"ABC"}
        actual = self.task.getOutput()

        self.assertEquals(expected, actual)

    def test_Task_dataclenear_execute_cleanup_input_with_characters_to_be_filtered_and_double_quotes(self):
        """
        TEst the data cleaner task with an input with characters to be filtered and double quotes
        """
        input = '{"data": "ABC«"»""}'
        self.task.setIsJson(True)
        self.task.setReplacementCharacter("")
        self.task.execute(input)

        expected = {'data':'{"data": "ABC"}'}
        actual = self.task.getOutput()
        self.assertEquals(expected, actual)

if __name__ == '__main__':
    unittest.main()
