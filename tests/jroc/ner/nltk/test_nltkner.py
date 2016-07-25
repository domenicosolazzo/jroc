from . import NLTKTagger
import unittest
import nltk
import os

class NLTKTaggerTestCase(unittest.TestCase):
    tagger = None
    currentDirectory = currentDirectory = "%s" % (os.path.dirname(os.path.realpath(__file__)), )
    testTextsDirectory = "%s/../../../data/text/" % (currentDirectory, )

    def setUp(self):
        self.tagger = NLTKTagger()

    def tearDown(self):
        self.tagger = None


    def test_nertagger_returns_nltk_ne(self):
        """
        Test for checking if the tagger returns named entities from the NLTK tree
        """
        text = self.helper_readFilename('en/article2.txt')
        actual = self.tagger.getEntities(raw_text=text)
        print(actual)
        expected = [(u'House', 'ORGANIZATION'), (u'John Boehner', 'PERSON'),
                    (u'Keystone Pipeline', 'PERSON'), (u'Obama', 'ORGANIZATION'),
                    (u'Republican', 'ORGANIZATION'), (u'House', 'ORGANIZATION'),
                    (u'John Boehner', 'PERSON'), (u'Keystone Pipeline', 'ORGANIZATION'),
                    (u'Keystone Pipeline', 'ORGANIZATION'), (u'Boehner', 'PERSON'),
                    (u'America', 'GPE'), (u'United States', 'GPE'), (u'Keystone Pipeline', 'ORGANIZATION'),
                    (u'Listen', 'PERSON'), (u'Keystone', 'ORGANIZATION'), (u'Boehner', 'PERSON'),
                    (u'State Department', 'ORGANIZATION'), (u'Democratic', 'ORGANIZATION'),
                    (u'GOP', 'ORGANIZATION'), (u'Obama', 'PERSON'), (u'White House', 'FACILITY')]
        self.assertEqual(expected, actual)


    def test_nertagger_returns_nltk_ne_norwegian_text(self):
        """
        Test for checking if the tagger returns named entities from the NLTK tree with Norwegian Text
        """
        text = self.helper_readFilename('no/article11.txt')
        actual = self.tagger.getEntities(raw_text=text)
        expected = [(u'Jan', 'PERSON'), (u'Solberg', 'ORGANIZATION'), (u'Bryggeri G\xe5rdene', 'PERSON'),
                    (u'Han', 'PERSON'), (u'Carl Otto S\xe6tre', 'PERSON'), (u'Dette', 'PERSON'),
                    (u'Solberg', 'PERSON'), (u'H\xf8nefoss', 'PERSON'), (u'S\xe6tre', 'PERSON'),
                    (u'Salget', 'PERSON'), (u'Solberg', 'PERSON'), (u'Hotell Service', 'ORGANIZATION'),
                    (u'De', 'PERSON'), (u'Knut Solberg', 'PERSON'), (u'Unni', 'PERSON'), (u'Finn Ove Carlsen', 'PERSON')]

        self.assertEqual(expected, actual)


    def test_nertagger_returns_nltk_ne_spanish_text(self):
        """
        Test for checking if the tagger returns named entities from the NLTK tree with Spanish Text
        """
        text = self.helper_readFilename('es/article1.txt')
        actual = self.tagger.getEntities(raw_text=text)
        expected = [(u'La', 'GPE'), (u'Andr\xe9 Gomes', 'PERSON'), (u'Barcelona', 'PERSON'),
                    (u'Ivan Rakitic', 'PERSON'), (u'Miquel Sors', 'ORGANIZATION'), (u'Arturo Canales', 'PERSON'),
                    (u'Ivan Rakitic', 'PERSON'), (u'Rakitic', 'PERSON'), (u'Barcelona', 'PERSON'),
                    (u'Miquel Sors', 'PERSON'), (u'Bar\xe7a', 'PERSON'), (u'Rakitic', 'PERSON'),
                    (u'Luis Enrique', 'PERSON'), (u'Miquel Sors', 'ORGANIZATION'), (u'Andr\xe9 Gomes', 'PERSON')]

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
