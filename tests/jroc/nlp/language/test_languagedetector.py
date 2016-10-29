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

if __name__ == '__main__':
    unittest.main()
