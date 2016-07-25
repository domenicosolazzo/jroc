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


    def test_nertagger_returns_stanford_ne(self):
        """
        Test for checking if the tagger returns named entities from the stanford tree
        """
        text = self.helper_readFilename('en/article2.txt')
        actual = self.tagger.getEntities(raw_text=text)
        print(actual)
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
        actual = self.tagger.getEntities(raw_text=text)
        expected = [(u'Andr\xe9 Gomes', u'PERSON'), (u'Barcelona', u'ORGANIZATION'),
                    (u'Ivan Rakitic', u'PERSON'), (u'Miquel Sors', u'PERSON'), (u'Arturo Canales', u'PERSON'),
                    (u'Ivan Rakitic', u'PERSON'), (u'Barcelona', u'ORGANIZATION'), (u'Luis Enrique', u'PERSON'),
                    (u'Miquel Sors', u'PERSON'), (u'Andr\xe9 Gomes', u'PERSON')]

        self.assertEqual(expected, actual)

    def test_nertagger_returns_stanford_ne_norwegian_text(self):
        """
        Test for checking if the tagger returns named entities from the stanford tree with Norwegian Text
        """
        text = self.helper_readFilename('no/article11.txt')
        actual = self.tagger.getEntities(raw_text=text)
        expected = [(u'Jan Solberg', u'PERSON'), (u'Carl Otto S\xe6tre', u'PERSON'),
                    (u'Solberg', u'PERSON'), (u'Solberg', u'PERSON'), (u'Solberg', u'PERSON'),
                    (u'Hotell Service', u'ORGANIZATION'), (u'Knut Solberg', u'PERSON'),
                    (u'Unni og Finn Ove Carlsen', u'PERSON')]

        self.assertEqual(expected, actual)


    def test_nertagger_returns_stanford_ne_spanish_text(self):
        """
        Test for checking if the tagger returns named entities from the stanford tree with Spanish Text
        """
        text = self.helper_readFilename('es/article1.txt')
        actual = self.tagger.getEntities(raw_text=text)
        print(actual)
        expected = [
                    (u'Andr\xe9 Gomes', u'PERSON'), (u'Barcelona', u'ORGANIZATION'),
                    (u'Ivan Rakitic', u'PERSON'), (u'Miquel Sors', u'PERSON'),
                    (u'Arturo Canales', u'PERSON'), (u'Ivan Rakitic', u'PERSON'),
                    (u'Barcelona', u'ORGANIZATION'), (u'Luis Enrique', u'PERSON'),
                    (u'Miquel Sors', u'PERSON'), (u'Andr\xe9 Gomes', u'PERSON')]

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
