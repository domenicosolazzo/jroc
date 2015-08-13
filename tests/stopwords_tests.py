from . import StopwordManager
import unittest

class StopwordManagerTestCase(unittest.TestCase):
    swManager = None
    def setUp(self):
        self.swManager = StopwordManager()

    def tearDown(self):
        self.swManager = None

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

if __name__ == '__main__':
    unittest.main()
