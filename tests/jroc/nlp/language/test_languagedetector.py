from . import LanguageDetector
import unittest
import os

class LanguageDetectorTestCase(unittest.TestCase):
    languageDetector = None
    currentDirectory = currentDirectory = "%s" % (os.path.dirname(os.path.realpath(__file__)), )
    testTextsDirectory = "%s/../../../data/text/" % (currentDirectory, )

    def setUp(self):
        self.languageDetector = LanguageDetector()

    def tearDown(self):
        self.languageDetector = None

    def test_initialize_languageDetector(self):
        self.assertTrue(True)

    def test_languagedetector_with_norwegian_text(self):
        """
        Check that the detected language is norwegian (no)
        """
        text = self.helper_readFilename("no/language.txt")
        expected = "no"
        actual = self.languageDetector.classify(text)[0]
        self.assertEqual(expected, actual)

    def test_languagedetector_with_norwegian_bokmal_text(self):
        """
        Check that the detected language is norwegian (no)
        """
        text = self.helper_readFilename("nb/language.txt")
        expected = "no"
        actual = self.languageDetector.classify(text)[0]
        self.assertEqual(expected, actual)

    def test_languagedetector_with_norwegian_nynorsk_text(self):
        """
        Check that the detected language is norwegian - nynorsk (nn)
        """
        text = self.helper_readFilename("nn/language.txt")
        expected = "nn"
        actual = self.languageDetector.classify(text)[0]
        self.assertEqual(expected, actual)

    def test_languagedetector_with_english_text(self):
        """
        Check that the detected language is norwegian (no)
        """
        text = self.helper_readFilename("en/language.txt")
        expected = "en"
        actual = self.languageDetector.classify(text)[0]
        self.assertEqual(expected, actual)

    def helper_readFilename(self, filename=''):
        stopwords = []
        if not filename:
            raise Exception("The file is empty")

        fileToRead = "%s%s" % (self.testTextsDirectory, filename)

        f = open(fileToRead, 'r')
        text = f.read()
        f.close()

        return text

    """
    def test_initialize_manager_with_wrong_filename(self):
        self.assertRaises(IOError, StopwordManager, "fakefile.txt")

    def test_initialize_manager_with_empty_filename(self):
        self.assertRaises(IOError, StopwordManager, "")

    def test_get_stopwords(self):
        words = self.swManager.getStopWords()
        self.assertTrue(len(words) > 0)

    def test_filter_words_contained_in_stopwords(self):
        words = ["jeg"]
        words = self.swManager.filterStopWords(words)
        self.assertTrue(len(words) == 0)

    def test_filter_words_not_contained_in_stopwords(self):
        words = ["inter milan"]
        words = self.swManager.filterStopWords(words)
        self.assertTrue(len(words) == 1)

    def test_filter_words_list_containing_stopwords(self):
        words = ["inter milan", "jeg", "og"]
        words = self.swManager.filterStopWords(words)
        self.assertTrue(len(words) == 1)

    def test_filter_words_list_is_not_a_list(self):
        self.assertRaises(AssertionError, self.swManager.filterStopWords, True)
        self.assertRaises(AssertionError, self.swManager.filterStopWords, 1)
    """

if __name__ == '__main__':
    unittest.main()
