# -*- coding: utf-8 -*-
from . import PosTaggerPipeline
import unittest
import os

class PosTaggerPipelineTestCase(unittest.TestCase):
    pipeline = None
    name = "PosTagger Pipeline tests"

    def setUp(self):
        self.pipeline = None

    def tearDown(self):
        self.pipeline = None


    #def test_pipeline_execute_with_invalid_input(self):
        """
        Test the execution of the pos pipeline with wrong input data. (Malformed JSON)
        """
        input = '{"data" "Ivar Aasen ble født på gården Åsen i " "  " Hovdebygda på Sunnmøre som sønn av småbrukeren Ivar Jonsson."}'
        self.pipeline = PosTaggerPipeline(input=input,name=self.name)
        self.assertRaises(Exception, self.pipeline.execute, None)

    def test_pipeline_execute(self):
        """
        Test the execution of the language detection pipeline
        """
        input = '{"data":"Ivar Aasen ble født på gården Åsen i Hovdebygda på Sunnmøre som sønn av småbrukeren Ivar Jonsson."}'
        self.pipeline = PosTaggerPipeline(input=input,name=self.name)
        self.pipeline.execute()
        output = self.pipeline.getOutput()
        self.assertIsNotNone(output)

        expected = "no"
        actual = output.get('language', None)
        self.assertEquals(expected, actual)
        
    def test_pipeline_execute_with_characters_to_be_removed(self):
        """
        Test the execution of the pos pipeline with an input with characters that should be removed
        """
        input = '{"data":"Ivar Aasen ble født " "  "på gården Åsen i Hovdebygda på Sunnmøre som sønn av småbrukeren Ivar Jonsson."}'
        self.pipeline = PosTaggerPipeline(input=input,name=self.name)
        self.pipeline.execute()
        output = self.pipeline.getOutput()
        self.assertIsNotNone(output)

        expected = "no"
        actual = output.get('language', None)
        self.assertEquals(expected, actual)

if __name__ == '__main__':
    unittest.main()
