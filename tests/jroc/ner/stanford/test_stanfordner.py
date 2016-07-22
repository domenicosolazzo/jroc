from . import StanfordTagger
import unittest
import nltk
import os

class StanfordNERTaggerTestCase(unittest.TestCase):
    tagger = None
    currentDirectory = currentDirectory = "%s" % (os.path.dirname(os.path.realpath(__file__)), )
    testTextsDirectory = "%s/../../../data/text/" % (currentDirectory, )

    def setUp(self):
        self.tagger = StanfordTagger()

    def tearDown(self):
        self.tagger = None

    def test_nertagger_returns_named_entities(self):
        """
        Test the tags method of the Stanford NER Tagger.
        """
        text = self.helper_readFilename('en/article2.txt')

        actual = self.tagger.tags(raw_text=text)
        self.assertTrue(isinstance(actual, list))
        self.assertTrue(len(actual) > 0)
        firstElement = actual[0]
        self.assertTrue(isinstance(firstElement, tuple))
        self.assertEqual('ORGANIZATION', firstElement[1])

    def test_nertagger_returns_bio_tags(self):
        """
        Test for checking if the tagger returns BIO tags
        """
        text = self.helper_readFilename('en/article2.txt')
        ne_entities = self.tagger.tags(raw_text=text)

        actual = self.tagger.bio_tagger(ne_entities)
        self.assertTrue(isinstance(actual, list))
        self.assertTrue(len(actual) > 0)
        firstElement = actual[0]
        self.assertTrue(isinstance(firstElement, tuple))
        self.assertEqual('B-ORGANIZATION', firstElement[1])

    def test_nertagger_returns_stanford_tree(self):
        """
        Test for checking if the tagger returns the stanford tree
        """
        text = self.helper_readFilename('en/article2.txt')
        ne_entities = self.tagger.tags(raw_text=text)
        bio_tags = self.tagger.bio_tagger(ne_entities)
        actual = self.tagger.stanford_tree(bio_tags)

        self.assertTrue(isinstance(actual,nltk.tree.Tree))

    def test_nertagger_returns_stanford_ne(self):
        """
        Test for checking if the tagger returns named entities from the stanford tree
        """
        text = self.helper_readFilename('en/article2.txt')
        ne_entities = self.tagger.tags(raw_text=text)
        bio_tags = self.tagger.bio_tagger(ne_entities)
        stanford_tree = self.tagger.stanford_tree(bio_tags)

        actual = self.tagger.stanford_ne(stanford_tree)
        expected = [(u'House', u'ORGANIZATION'), (u'John Boehner', u'PERSON'),
                        (u'Keystone Pipeline', u'ORGANIZATION'), (u'Obama', u'PERSON'),
                        (u'Republican House', u'ORGANIZATION'), (u'John Boehner', u'PERSON'),
                        (u'Keystone Pipeline', u'ORGANIZATION'), (u'Boehner', u'PERSON'),
                        (u'America', u'LOCATION'), (u'United States', u'LOCATION'), (u'Keystone Pipeline', u'ORGANIZATION'),
                        (u'Boehner', u'PERSON'), (u'State Department', u'ORGANIZATION'), (u'GOP', u'ORGANIZATION'),
                        (u'Obama', u'PERSON'), (u'White House', u'ORGANIZATION')]

        self.assertEqual(expected, actual)

    def test_nertagger_returns_stanford_ne_spanish_text(self):
        """
        Test for checking if the tagger returns named entities from the stanford tree with Spanish Text
        """
        text = self.helper_readFilename('es/article1.txt')
        ne_entities = self.tagger.tags(raw_text=text)
        bio_tags = self.tagger.bio_tagger(ne_entities)
        stanford_tree = self.tagger.stanford_tree(bio_tags)

        actual = self.tagger.stanford_ne(stanford_tree)
        expected = [(u'House', u'ORGANIZATION'), (u'John Boehner', u'PERSON'),
                        (u'Keystone Pipeline', u'ORGANIZATION'), (u'Obama', u'PERSON'),
                        (u'Republican House', u'ORGANIZATION'), (u'John Boehner', u'PERSON'),
                        (u'Keystone Pipeline', u'ORGANIZATION'), (u'Boehner', u'PERSON'),
                        (u'America', u'LOCATION'), (u'United States', u'LOCATION'), (u'Keystone Pipeline', u'ORGANIZATION'),
                        (u'Boehner', u'PERSON'), (u'State Department', u'ORGANIZATION'), (u'GOP', u'ORGANIZATION'),
                        (u'Obama', u'PERSON'), (u'White House', u'ORGANIZATION')]
        print(actual)

        self.assertEqual(expected, actual)




    def helper_readFilename(self, filename=''):
        stopwords = []
        if not filename:
            raise Exception("The file is empty")

        fileToRead = "%s%s" % (self.testTextsDirectory, filename)

        with open(fileToRead) as f:
            text = f.read()
        #f.close()
        return text
