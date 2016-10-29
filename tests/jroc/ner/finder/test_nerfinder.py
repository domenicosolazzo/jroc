from . import NERFinder
import unittest
import nltk
import os

class StanfordNERTaggerTestCase(unittest.TestCase):
    finder = None
    currentDirectory = currentDirectory = "%s" % (os.path.dirname(os.path.realpath(__file__)), )
    testTextsDirectory = "%s/../../../data/text/" % (currentDirectory, )

    def setUp(self):
        self.finder = NERFinder()

    def tearDown(self):
        self.finder = None

    def test_nerfinder_returns_named_entities(self):
        """
        Test the tags method of the NER Finder
        """
        """
        text = self.helper_readFilename('en/article2.txt')

        actual = self.tagger.tags(raw_text=text)
        self.assertTrue(isinstance(actual, list))
        self.assertTrue(len(actual) > 0)
        firstElement = actual[0]
        self.assertTrue(isinstance(firstElement, tuple))
        self.assertEqual('ORGANIZATION', firstElement[1])
        """

    def test_nertagger_returns_bio_tags(self):
        """
        Test for checking if the tagger returns BIO tags
        """
        """
        text = self.helper_readFilename('en/article2.txt')
        ne_entities = self.tagger.tags(raw_text=text)

        actual = self.tagger.bio_tagger(ne_entities)
        self.assertTrue(isinstance(actual, list))
        self.assertTrue(len(actual) > 0)
        firstElement = actual[0]
        self.assertTrue(isinstance(firstElement, tuple))
        self.assertEqual('B-ORGANIZATION', firstElement[1])
        """

    def test_nertagger_returns_stanford_tree(self):
        """
        Test for checking if the tagger returns the stanford tree
        """
        """
        text = self.helper_readFilename('en/article2.txt')
        ne_entities = self.tagger.tags(raw_text=text)
        bio_tags = self.tagger.bio_tagger(ne_entities)
        actual = self.tagger.stanford_tree(bio_tags)

        self.assertTrue(isinstance(actual,nltk.tree.Tree))
        """
