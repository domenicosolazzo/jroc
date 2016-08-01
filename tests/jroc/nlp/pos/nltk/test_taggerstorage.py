# -*- coding: utf-8 -*-
from . import TaggerStorageAdapter
import unittest
import os
import codecs


class TaggerStorageAdapterTestCase(unittest.TestCase):
    taggerStorage = TaggerStorageAdapter()
    currentDirectory =  "%s" % (os.path.dirname(os.path.realpath(__file__)), )
    testTextsDirectory = "%s/../../../../data/text/" % (currentDirectory, )

    def setUp(self):
        text = "Det er norsk"
        self.taggerStorage = TaggerStorageAdapter()

    def tearDown(self):
        #self.obtManager.cleanUp()
        self.obtManager = None


    def test_pos_initizialize(self):
        """
        Check if the initialization works
        """
        result = self.taggerStorage.getTagger()
        self.assertTrue(result is not None)

    def test_pos_initizialize_with_aubt(self):
        """
        Check if the initialization works with AUBT
        """
        self.taggerStorage = TaggerStorageAdapter(model='aubt')
        result = self.taggerStorage.getTagger()
        self.assertTrue(result is not None)

    def test_pos_classifier_text_english(self):
        """
        Test the classifier tagger with an english text
        """
        text = self.helper_readFilename("en/article1.txt")
        text = text.decode('utf-8').split()
        result = self.taggerStorage.getTagger().tag(text)
        expected = (u'Congress\u2019s', u'NNP')
        self.assertTrue(isinstance(result, list))
        self.assertTrue(len(result) > 0)
        self.assertEqual(expected, result[0])

    def helper_readFilename(self, filename=''):
        stopwords = []
        if not filename:
            raise Exception("The file is empty")

        fileToRead = "%s%s" % (self.testTextsDirectory, filename)

        with open(fileToRead) as f:
            text = f.read()
        #f.close()
        return text
