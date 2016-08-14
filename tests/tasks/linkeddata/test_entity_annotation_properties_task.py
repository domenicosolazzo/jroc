# -*- coding: utf-8 -*-
from . import EntityAnnotationPropertiesTask
import unittest
import os

class EntityAnnotationPropertiesTaskTestCase(unittest.TestCase):
    task = None
    name = "Entity Annotation Properties Test Task"

    def setUp(self):
        self.task = EntityAnnotationPropertiesTask(self.name, withPropertyValues=True)

    def tearDown(self):
        self.task = None

    def test_task_retrieve_entity(self):
        """
        Test that it is possible to retrieve all the properties for a given entity
        """
        data = "Cristiano Ronaldo"

        self.task.execute(data)
        actual = self.task.getOutput()
        self.assertTrue('data' in actual)
        data = actual.get('data')
        self.assertTrue('properties' in data)
