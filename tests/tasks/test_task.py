from . import Task
import unittest
import os

class TaskTestCase(unittest.TestCase):
    task = None

    def setUp(self):
        self.task = None

    def tearDown(self):
        self.task = None

    def test_task_initialization_fails_if_name_is_None(self):
        """
        Test that a task throws an exception if the name is None
        """
        name = None

        self.assertRaises(Exception, Task, name)

    def test_task_initialization_fails_if_name_is_empty(self):
        """
        Test that a task throws an exception if the name is Empty
        """
        name = ""

        self.assertRaises(Exception, Task, name)

    def test_task_initialization(self):
        """
        Test that a task has been created
        """
        name = "test1"
        self.task = Task(name=name)

        self.assertTrue(True)

    def test_task_getName(self):
        """
        Test that getName returns the task name
        """
        expected = "Test"
        self.task = Task(name=expected)
        actual = self.task.getName()
        self.assertEqual(actual, expected)

    def test_task_getPrefix(self):
        """
        Test that getName returns the task prefix
        """
        name = "Test"
        self.task = Task(name=name)

        expected = "test"
        actual = self.task.getPrefix()
        self.assertEqual(actual, expected)

    def test_task_getPrefix_with_spaces(self):
        """
        Test that getName returns the task prefix
        """
        name = "Test Name"
        self.task = Task(name=name)

        expected = "test-name"
        actual = self.task.getPrefix()
        self.assertEqual(actual, expected)

    def test_task_getPrefix(self):
        """
        Test that getName returns the task prefix
        """
        name = "Test"

        self.task = Task(name=name)

        expected = False
        actual = self.task.isInitialTask()
        self.assertEqual(actual, expected)

        self.task = Task(name=name, initial_task=True)
        expected = True
        actual = self.task.isInitialTask()
        self.assertEqual(actual, expected)

    def test_task_execute_fails(self):
        """
        Check the execute method fails
        """
        name = "Test"
        self.task = Task(name=name)

        self.assertRaises(Exception, self.task.execute, None)

    def test_task_execute(self):
        """
        Check the execute method
        """
        name = "Test"
        self.task = Task(name=name)
        self.task.execute(input="This is a test")
        self.assertTrue(True)

    def test_task_finish(self):
        """
        Check the finish method
        """
        name = "Test"
        self.task = Task(name=name)
        self.task.finish("Data", failed=False, error=None)
        self.assertEqual({"data":"Data"}, self.task.getOutput())
        self.assertTrue(True)

    def test_task_hasFailed(self):
        """
        Check if the task has failed
        """
        name = "Test"
        self.task = Task(name=name)
        self.task.finish(None, failed=True, error="Error")

        actual = self.task.hasFailed()
        expected = True

        self.assertEqual(actual, expected)

    def test_task_setOutput(self):
        """
        Check if the task saves the output
        """
        name = "Test"
        output = 'Output'
        self.task = Task(name=name)
        self.task.setOutput(output)

        actual = self.task.getOutput()
        expected = {'data': output}

        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
