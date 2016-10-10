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

        expected = [
                    {'tags': [u'TEST1', u'SHITTY LANGUAGE', u'LANGUAGE'], 'entity': u'Java'},
                    {'tags': [u'TEST1', u'LOCATION'], 'entity': u'Tokyo'},
                    {'tags': [u'TEST1', u'LANGUAGE'], 'entity': u'C#'},
                    {'tags': [u'TEST1', u'LANGUAGE'], 'entity': u'Javascript'},
                    {'tags': [u'TEST1', u'LANGUAGE'], 'entity': u'Pl/Sql'},
                    {'tags': [u'TEST1', u'LANGUAGE'], 'entity': u'Sql'},
                    {'tags': [u'TEST1', u'ORGANIZATION'], 'entity': u'Moody'}
        ];
        actual = output["final regex"];
        self.assertEqual(expected, actual);

if __name__ == '__main__':
    unittest.main()
