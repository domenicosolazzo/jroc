from . import StopwordManager
import unittest
import os

class StopwordsTestCase(unittest.TestCase):
    languageDetector = None
    currentDirectory = "%s" % (os.path.dirname(os.path.realpath(__file__)), )
    stopwordsDirectory = "%s/../../../../jroc/nlp/stopwords/data/" % (currentDirectory,)

    def setUp(self):
        self.stopwordManager = None

    def tearDown(self):
        self.stopwordManager = None

    def test_norwegian_stopwords(self):
        """
        Test the stopwords for the norwegian language
        """
        self.stopwordManager = StopwordManager(language="no")
        expected = self.helper_readFilename("stopwords_no.txt")
        actual = self.stopwordManager.getLanguageStopwords()
        self.assertEqual(expected, actual)

    def test_english_stopwords(self):
        """
        Test the stopwords for the english language
        """
        self.stopwordManager = StopwordManager(language="en")
        expected = self.helper_readFilename("stopwords_en.txt")
        actual = self.stopwordManager.getLanguageStopwords()
        self.assertEqual(expected, actual)

    def test_danish_stopwords(self):
        """
        Test the stopwords for the danish language
        """
        self.stopwordManager = StopwordManager(language="da")
        expected = self.helper_readFilename("stopwords_da.txt")
        actual = self.stopwordManager.getLanguageStopwords()
        self.assertEqual(expected, actual)

    def test_german_stopwords(self):
        """
        Test the stopwords for the german language
        """
        self.stopwordManager = StopwordManager(language="de")
        expected = self.helper_readFilename("stopwords_de.txt")
        actual = self.stopwordManager.getLanguageStopwords()
        self.assertEqual(expected, actual)

    def test_spanish_stopwords(self):
        """
        Test the stopwords for the spanish language
        """
        self.stopwordManager = StopwordManager(language="es")
        expected = self.helper_readFilename("stopwords_es.txt")
        actual = self.stopwordManager.getLanguageStopwords()
        self.assertEqual(expected, actual)

    def test_italian_stopwords(self):
        """
        Test the stopwords for the spanish language
        """
        self.stopwordManager = StopwordManager(language="it")
        expected = self.helper_readFilename("stopwords_it.txt")
        actual = self.stopwordManager.getLanguageStopwords()
        self.assertEqual(expected, actual)

    def test_finnish_stopwords(self):
        """
        Test the stopwords for the finnish language
        """
        self.stopwordManager = StopwordManager(language="fi")
        expected = self.helper_readFilename("stopwords_fi.txt")
        actual = self.stopwordManager.getLanguageStopwords()
        self.assertEqual(expected, actual)

    def test_french_stopwords(self):
        """
        Test the stopwords for the french language
        """
        self.stopwordManager = StopwordManager(language="fr")
        expected = self.helper_readFilename("stopwords_fr.txt")
        actual = self.stopwordManager.getLanguageStopwords()
        self.assertEqual(expected, actual)

    def test_swedish_stopwords(self):
        """
        Test the stopwords for the swedish language
        """
        self.stopwordManager = StopwordManager(language="sv")
        expected = self.helper_readFilename("stopwords_sv.txt")
        actual = self.stopwordManager.getLanguageStopwords()
        self.assertEqual(expected, actual)

    def test_custom_stopwords(self):
        """
        Test the custom stopwords
        """
        self.stopwordManager = StopwordManager(language="en")
        expected = self.helper_readFilename("stopwords_custom.txt")
        actual = self.stopwordManager.getCustomStopwords()
        self.assertEqual(expected, actual)

    def test_stopwords(self):
        """
        Test the stopwords
        """
        self.stopwordManager = StopwordManager(language="en")
        expected = self.helper_readFilename("stopwords_en.txt")
        custom_expected = self.helper_readFilename("stopwords_custom.txt")
        expected.extend(custom_expected)
        actual = self.stopwordManager.getStopWords()
        self.assertEqual(set(expected), actual)


    def test_filtering_words(self):
        """
        Test how to filter a list of strings using the StopwordManager
        """
        self.stopwordManager = StopwordManager(language="en")
        expected = ["Tree", "Tall"]

        words = ["The", "Tree", "is", "Tall"]
        actual = self.stopwordManager.filterStopWords(words)
        self.assertEqual(expected, actual)

    def test_language_not_available(self):
        """
        Test when a not available language is given in input to the StopwordManager
        """
        self.assertRaises(ValueError, StopwordManager, "not_valid_language")

    def helper_readFilename(self, filename=''):
        stopwords = []
        if not filename:
            raise Exception("The file is empty")

        fileToRead = "%s%s" % (self.stopwordsDirectory, filename)

        f = open(fileToRead, 'r')
        lines = f.readlines()
        f.close()

        stopwords = filter(None, map(lambda x: x.split('|')[0].strip().lower().decode('utf-8'), lines))
        return stopwords

if __name__ == '__main__':
    unittest.main()
