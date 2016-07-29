from . import NLTKTokenizer
import unittest
import os

class NLTKTokenizerTestCase(unittest.TestCase):
    tokenizer = None
    currentDirectory = "%s" % (os.path.dirname(os.path.realpath(__file__)), )
    directory = "%s/../../../data/text/" % (currentDirectory,)

    def setUp(self):
        self.tokenizer = NLTKTokenizer(language="en")

    def tearDown(self):
        self.tokenizer = None

    def test_tokenizer(self):
        """
        Test the english tokenizer
        """
        text = self.helper_readFilename("en/article1.txt")
        expected = u'Congress\u2019s national security leadership is facing its biggest shakeup in years as some of its longest - serving and most influential members retire, seek other offices or risk losing their seats in tough reelections.'
        actual = self.tokenizer.tokenizeText(text)
        self.assertTrue(isinstance(actual, list))
        self.assertTrue(len(actual) > 0)
        self.assertEqual(expected, actual[0])

    def test_tokenizer_norwegian(self):
        """
        Test the norwegian tokenizer
        """
        self.tokenizer = NLTKTokenizer(language="no")
        text = self.helper_readFilename("no/article1.txt")
        expected = u'VG henta i fjor ut tal fr\xe5 inspeksjonane til Statens vegvesen, som viste at 104 bruer i Noreg er svekka.'
        actual = self.tokenizer.tokenizeText(text)
        self.assertTrue(isinstance(actual, list))
        self.assertTrue(len(actual) > 0)
        self.assertEqual(expected, actual[0])

    def test_tokenizer_spanish(self):
        """
        Test the spanish tokenizer
        """
        self.tokenizer = NLTKTokenizer(language="es")
        text = self.helper_readFilename("es/article1.txt")
        expected = u'La llegada de Andr\xe9 Gomes, que llena de interiores la plantilla del Barcelona, podr\xeda cobrarse una v\xedctima, Ivan Rakitic.'
        actual = self.tokenizer.tokenizeText(text)
        self.assertTrue(isinstance(actual, list))
        self.assertTrue(len(actual) > 0)
        self.assertEqual(expected, actual[0])

    def test_tokenizer_italian(self):
        """
        Test the spanish tokenizer
        """
        self.tokenizer = NLTKTokenizer(language="it")
        text = self.helper_readFilename("it/article1.txt")
        expected = u'Baggio e Ronaldo devoti a San Zico.'
        actual = self.tokenizer.tokenizeText(text)
        self.assertTrue(isinstance(actual, list))
        self.assertTrue(len(actual) > 0)
        self.assertEqual(expected, actual[0])

    def test_word_tokenizer(self):
        """
        Test the word tokenizer
        """
        text = self.helper_readFilename("en/article1.txt")
        expected = [ u'Congress\u2019s', u'national', u'security', u'leadership', u'is', u'facing', u'its',
                     u'biggest', u'shakeup', u'in', u'years', u'as', u'some', u'of', u'its', u'longest', u'-',
                     u'serving', u'and', u'most', u'influential', u'members', u'retire', u',', u'seek', u'other',
                     u'offices', u'or', u'risk', u'losing', u'their', u'seats', u'in', u'tough', u'reelections', u'.']

        actual = self.tokenizer.tokenizeSentence(sentences[0])
        print(actual)
        self.assertTrue(isinstance(actual, list))
        self.assertTrue(len(actual) > 0)
        self.assertEqual(expected, actual[0])


    def helper_readFilename(self, filename=''):
        stopwords = []
        if not filename:
            raise Exception("The file is empty")

        fileToRead = "%s%s" % (self.directory, filename)

        f = open(fileToRead, 'r')
        text = f.read()
        f.close()

        return text
