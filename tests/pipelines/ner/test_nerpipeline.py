# -*- coding: utf-8 -*-
from . import NERPipeline
import unittest
import os

class NERPipelineTestCase(unittest.TestCase):
    pipeline = None
    name = "NER Pipeline tests"

    def setUp(self):
        self.pipeline = None

    def tearDown(self):
        self.pipeline = None


    def test_pipeline_execute_with_invalid_input(self):
        """
        Test the execution of the pos pipeline with wrong input data. (Malformed JSON)
        """
        input = '{"data" "Ivar Aasen ble født på gården Åsen i " "  " Hovdebygda på Sunnmøre som sønn av småbrukeren Ivar Jonsson."}'
        self.pipeline = NERPipeline(input=input,name=self.name, withEntityAnnotation=False)
        self.assertRaises(Exception, self.pipeline.execute, None)

    def test_pipeline_execute_with_valid_text(self):
        """
        Test the execution of the ner pipeline with a valid text. No Entity Annotation
        """
        input = '{"data":"Ivar Aasen ble født på gården Åsen i Hovdebygda på Sunnmøre som sønn av småbrukeren Ivar Jonsson."}'
        self.pipeline = NERPipeline(input=input, name=self.name, withEntityAnnotation=False)
        self.pipeline.execute()

        actual = self.pipeline.getOutput()
        expected = [u'Sunnm\xf8re', u'\xc5sen', u'Ivar Aasen', u'Ivar Jonsson', u'Hovdebygda']
        self.assertTrue('entities' in actual)
        self.assertEqual(expected, actual.get('entities'))

    def test_pipeline_execute_with_valid_text_and_entity_annotation(self):
        """
        Test the execution of the ner pipeline with a valid text. It is using Entity Annotation
        """
        input = '{"data":"Ivar Aasen ble født på gården Åsen i Hovdebygda på Sunnmøre som sønn av småbrukeren Ivar Jonsson."}'
        self.pipeline = NERPipeline(input=input, name=self.name, withEntityAnnotation=True)
        self.pipeline.execute()

        actual = self.pipeline.getOutput()
        self.assertTrue('entities-annotated' in actual)
        self.assertTrue(isinstance(actual.get('entities-annotated'), list))

    def test_pipeline_execute_with_characters_to_be_removed(self):
        """
        Test the execution of the ner pipeline with an input with characters that should be removed
        """
        input = '{"data":"Ivar Aasen ble født " "  "på gården Åsen i Hovdebygda på Sunnmøre som sønn av småbrukeren Ivar Jonsson."}'
        self.pipeline = NERPipeline(input=input, name=self.name, withEntityAnnotation=False)
        self.pipeline.execute()

        actual = self.pipeline.getOutput()
        expected = [u'Sunnm\xf8re', u'\xc5sen', u'Ivar Aasen', u'Ivar Jonsson', u'Hovdebygda']
        self.assertTrue('entities' in actual)
        self.assertEqual(expected, actual.get('entities'))
