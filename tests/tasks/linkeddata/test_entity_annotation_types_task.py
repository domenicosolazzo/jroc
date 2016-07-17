# -*- coding: utf-8 -*-
from . import EntityAnnotationTypesTask
import unittest
import os

class EntityAnnotationTypesTaskTestCase(unittest.TestCase):
    task = None
    name = "Entity Annotation Types Test Task"

    def setUp(self):
        self.task = EntityAnnotationTypesTask(self.name )

    def tearDown(self):
        self.task = None

    def test_task_retrieve_entity(self):
        """
        Test that it is possible to retrieve the unique URI for a given entity
        """
        data = "Cristiano Ronaldo"

        self.task.execute(data)
        actual = self.task.getOutput()
        self.assertTrue('data' in actual)
        data = actual.get('data')
        self.assertTrue('entity_detection' in data)
        self.assertTrue('types' in data)
