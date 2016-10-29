# -*- coding: utf-8 -*-
from . import NLTKTagger
import unittest
import os
import codecs


class TaggerStorageAdapterTestCase(unittest.TestCase):
    tagger = NLTKTagger()
    currentDirectory =  "%s" % (os.path.dirname(os.path.realpath(__file__)), )
    testTextsDirectory = "%s/../../../../data/text/" % (currentDirectory, )

    def setUp(self):
        text = "Det er norsk"
        self.tagger = NLTKTagger()

    def tearDown(self):
        #self.obtManager.cleanUp()
        self.tagger  = None




    def test_pos_classifier_text_english(self):
        """
        Test the classifier tagger with an english text
        """
        text = self.helper_readFilename("en/article1.txt")
        text = text.decode('utf-8')
        result = self.tagger.analyze(text)
        expected = (u'Congress\u2019s', u'NNP')
        self.assertTrue(isinstance(result, dict))
        self.assertTrue('pos' in result)
        self.assertEqual(expected, result['pos'][0])

    def test_pos_result_keys(self):
        """
        Test that all the expected keys are returned as results
        """
        text = self.helper_readFilename("en/article1.txt")
        text = text.decode('utf-8')
        result = self.tagger.analyze(text)
        expected = ['pos', 'indexed', 'JJ', 'VB', 'NN', 'NNP', 'RB', 'common']
        self.assertTrue(isinstance(result, dict))
        for key in expected:
            self.assertTrue(key in result)

    #TODO: Add more test with several language and articles



    def helper_readFilename(self, filename=''):
        stopwords = []
        if not filename:
            raise Exception("The file is empty")

        fileToRead = "%s%s" % (self.testTextsDirectory, filename)

        with open(fileToRead) as f:
            text = f.read()
        #f.close()
        return text
