# -*- coding: utf-8 -*-
from . import LanguageDetectionPipeline
import unittest
import os

class LanguageDetectionPipelineTestCase(unittest.TestCase):
    pipeline = None
    name = "Language Detection Pipeline tests"

    def setUp(self):
        self.pipeline = None

    def tearDown(self):
        self.pipeline = None


    def test_pipeline_execute_with_invalid_input(self):
        """
        Test the execution of the language detection pipeline
        """
        input = '{"data" "this is a " " "-test"}'
        self.pipeline = LanguageDetectionPipeline(input=input,name=self.name)
        self.assertRaises(Exception, self.pipeline.execute, None)

    def test_pipeline_execute(self):
        """
        Test the execution of the language detection pipeline
        """
        input = '{"data":"this is a " " "-test"}'
        self.pipeline = LanguageDetectionPipeline(input=input,name=self.name)
        self.pipeline.execute()
        output = self.pipeline.getOutput()
        self.assertIsNotNone(output)

        expected = "en"
        actual = output.get('language', None)
        self.assertEquals(expected, actual)

if __name__ == '__main__':
    unittest.main()
