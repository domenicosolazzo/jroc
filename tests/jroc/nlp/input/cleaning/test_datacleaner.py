from . import DataCleaner
import unittest
import os

class DataCleanerTestCase(unittest.TestCase):
    dataCleaner = None
    currentDirectory = currentDirectory = "%s" % (os.path.dirname(os.path.realpath(__file__)), )
    testTextsDirectory = "%s/../../../data/text/" % (currentDirectory, )

    def setUp(self):
        self.dataCleaner = DataCleaner()

    def tearDown(self):
        self.dataCleaner = None

    def test_datacleaner_with_empty_character_list(self):
        """
        Check that the data cleaner returns the same text if an empty
        list of characters has been given in input
        """
        text = "This is a text"
        expected = "This is a text"
        actual = self.dataCleaner.filterCharacters(characters=[], text=text)
        self.assertEqual(expected, actual)

    def test_datacleaner_with_character_list(self):
        text = "This is a text -"
        expected = "This is a text  "
        actual = self.dataCleaner.filterCharacters(characters=["-"], text=text)
        self.assertEqual(expected, actual)

    def test_datacleaner_with_default_character_list(self):
        text = "This is a text -"
        expected = "This is a text  "
        actual = self.dataCleaner.filterCharacters(text=text)
        self.assertEqual(expected, actual)

    def test_datacleaner_exception_if_characters_is_not_list(self):
        characters = "String"
        self.assertRaises(AssertionError, self.dataCleaner.filterCharacters, characters)

    def test_datacleaner_replacementcharacter(self):
        text = "This is a text -"
        replacementCharacter = ""

        expected = "This is a text "
        actual = self.dataCleaner.filterCharacters(replacement_character=replacementCharacter, text=text)
        self.assertEqual(expected, actual)

    def test_datacleaner_replacemenent_character_is_not_string(self):
        text = "This is a text -"
        replacemenentCharacter = 1

        expected = "This is a text  "
        actual = self.dataCleaner.filterCharacters(replacement_character=replacemenentCharacter, text=text)
        self.assertEqual(expected, actual)

    def test_datacleaner_text_is_not_string(self):
        text = 1234
        self.assertRaises(AssertionError, self.dataCleaner.filterCharacters, [], "", text)


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
