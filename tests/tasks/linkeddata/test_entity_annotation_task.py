# -*- coding: utf-8 -*-
from . import EntityAnnotationTask
import unittest
import os

class EntityAnnotationTaskTestCase(unittest.TestCase):
    task = None
    name = "Entity Annotation Test Task"

    def setUp(self):
        self.task = EntityAnnotationTask( self.name )

    def tearDown(self):
        self.task = None

    def test_task_retrieve_entity(self):
        """
        Test that an entity annotation task works
        """
        entities = { "entities": [ "Asti" ] }

        self.task.execute(entities)
        actual = self.task.getOutput()

        self.assertTrue('data' in actual)
        data = actual.get('data')
        self.assertTrue(isinstance(data, list))
        self.assertTrue(len(data) > 0)
        self.assertTrue(isinstance(data[0], dict))
        self.assertTrue('metadata' in data[0])
        self.assertTrue('entity' in data[0])
