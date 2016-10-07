# -*- coding: utf-8 -*-
from . import RegexTaggerPipeline
import unittest
import os

class RegexTaggerPipelineTestCase(unittest.TestCase):
    pipeline = None
    name = "RegexTagger Pipeline tests"

    def setUp(self):
        self.pipeline = None

    def tearDown(self):
        self.pipeline = None




    def test_pipeline_execute(self):
        """
        Test the execution of the RegexTagger pipeline
        """
        input = '{"data":"This is Moody javascript in Tokyo and PL/SQL in C# and Transact-SQL and Java"}'
        self.pipeline = RegexTaggerPipeline(input=input,name=self.name)
        self.pipeline.execute()
        output = self.pipeline.getOutput()
        self.assertIsNotNone(output)


        print(output)
        self.assertTrue(False)

if __name__ == '__main__':
    unittest.main()
