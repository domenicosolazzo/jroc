from . import RegexTagger
import unittest
import os
import re

class RegexTaggerTestCase(unittest.TestCase):
    regexTagger = None
    currentDirectory = currentDirectory = "%s" % (os.path.dirname(os.path.realpath(__file__)), )
    testTextsDirectory = "%s/../../../../data/text/" % (currentDirectory, )

    def setUp(self):
        self.regexTagger = None

    def tearDown(self):
        self.regexTagger = None


    def test_regextagger_text(self):
        """
        Check that the regex tagger is working correctly
        """
        text = """
        This is Moody javascript in Tokyo and PL/SQL in C# and Transact-SQL
        """

        json = {
            'entities':[
                {'entity':r'Moody\'s', 'tags':['ORGANIZATION']},
                {'entity':r'Javascript', 'tags':['LANGUAGE']},
                {'entity':r'Java', 'tags':['LANGUAGE']},
                {'entity':r'C#', 'tags':['LANGUAGE']},
                {'entity':r'.*SQL', 'tags':['LANGUAGE']},
                {'entity':r'tokyo', 'tags':['LOCATION']},
                {'entity':r'japan', 'tags':['LOCATION']},
            ],
            'additional_tags':[]
        }
        self.regexTagger = RegexTagger(json)

        expected = [
            {'entity': 'javascript', 'tags': ['LANGUAGE']},
            {'entity': 'Tokyo', 'tags': ['LOCATION']},
            {'entity': 'PL/SQL', 'tags': ['LANGUAGE']},
            {'entity': 'SQL', 'tags': ['LANGUAGE']},
            {'entity': 'C#', 'tags': ['LANGUAGE']},
            {'entity': 'Transact-SQL', 'tags': ['LANGUAGE']},
            {'entity': 'SQL', 'tags': ['LANGUAGE']}
        ]
        actual = self.regexTagger.getEntities(text)
        self.assertEqual(len(expected), len(actual))
        [self.assertDictEqual(res, expected[index]) for (index, res) in enumerate(actual)]
        #self.assertDictEqual(expected, actual)

    def test_regextagger_text_additional_tags(self):
        """
        Check that the regex tagger is working correctly with additional tags
        """
        text = """
        This is Moody javascript in Tokyo and PL/SQL in C# and Transact-SQL
        """

        json = {
            'entities':[
                {'entity':r'Moody\'s', 'tags':['ORGANIZATION']},
                {'entity':r'Javascript', 'tags':['LANGUAGE']},
                {'entity':r'Java', 'tags':['LANGUAGE']},
                {'entity':r'C#', 'tags':['LANGUAGE']},
                {'entity':r'.*SQL', 'tags':['LANGUAGE']},
                {'entity':r'tokyo', 'tags':['LOCATION']},
                {'entity':r'japan', 'tags':['LOCATION']},
            ],
            'additional_tags':['TEST']
        }
        self.regexTagger = RegexTagger(json)

        expected = [
            {'tags': ['LANGUAGE','TEST'], 'entity': 'javascript'},
            {'tags': ['LOCATION', 'TEST'], 'entity': 'Tokyo'}, {'tags': ['LANGUAGE','TEST'], 'entity': 'PL/SQL'}, {'tags': ['LANGUAGE','TEST'], 'entity': 'SQL'}, {'tags': ['LANGUAGE','TEST'], 'entity': 'C#'}, {'tags': ['LANGUAGE','TEST'], 'entity': 'Transact-SQL'}, {'tags': ['LANGUAGE','TEST'], 'entity': 'SQL'}]
        actual = self.regexTagger.getEntities(text)
        self.assertEqual(len(expected), len(actual))
        [self.assertDictEqual(res, expected[index]) for (index, res) in enumerate(actual)]

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
