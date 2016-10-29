# -*- coding: utf-8 -*-
from . import EntityAnnotationURITask
import unittest
import os

class EntityAnnotationURITaskTestCase(unittest.TestCase):
    task = None
    name = "Entity Annotation URI Test Task"

    def setUp(self):
        self.task = EntityAnnotationURITask(self.name )

    def tearDown(self):
        self.task = None

    def test_task_retrieve_entity(self):
        """
        Test that it is possible to retrieve the unique URI for a given entity
        """
        data = "Asti"

        self.task.execute(data)
        actual = self.task.getOutput()
        
        self.assertTrue('data' in actual)
        data = actual.get('data')
        self.assertTrue('uri' in data)
