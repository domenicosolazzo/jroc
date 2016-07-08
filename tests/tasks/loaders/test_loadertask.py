from . import LoaderTask
import unittest
import os

class LoaderTaskTestCase(unittest.TestCase):
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

        self.assertRaises(Exception, LoaderTask, name)
