# -*- coding: utf-8 -*-
from . import PosManager
import unittest
import os
import codecs

class PosManagerTestCase(unittest.TestCase):
    posManager = None
    currentDirectory = currentDirectory = "%s" % (os.path.dirname(os.path.realpath(__file__)), )
    testTextsDirectory = "%s/../../../../data/text/" % (currentDirectory, )

    def setUp(self):
        self.posManager = None

    def tearDown(self):
        #self.obtManager.cleanUp()
        self.posManager = None


    def test_posmanager_analyze(self):
        """
        Check if the analyze method
        """
        text = self.helper_readFilename('no/article14.txt')
        self.posManager = PosManager(language="no")
        result = self.posManager.analyze(text)

        self.assertTrue(self.posManager is not None)

    def test_posmanager_common_words_no_article14(self):
        """
        Check the common words for the article
        """
        text = self.helper_readFilename('no/article14.txt')
        self.posManager = PosManager(language="no")
        result = self.posManager.analyze(text)

        expected = sorted([(u'AS', 1), (u'Aner', 1), (u'Folk', 1), (u'Glassverk', 3),
                    (u'Hadeland', 3), (u'Magnor', 2), (u'Selvbl\xe5s', 1), (u'Taxfree', 1),
                    (u'Yelp', 1), (u'bier', 1), (u'd\xf8rer', 1), (u'ganger', 1), (u'glassbl\xe5sing', 1),
                    (u'glassbutikk', 1), (u'glassutsalg', 1), (u'jul', 1), (u'juletider', 1), (u'kanefart', 1),
                    (u'klistremerker', 1), (u'lager', 1), (u'm\xe5te', 1), (u'nisser', 1), (u'preg', 1),
                    (u'selvom', 1), (u'snakk', 1), (u'sted', 1), (u'\xe5r', 1)])
        actual = sorted(result.get('common_words', []))

        self.assertIsNotNone(actual)
        self.assertEquals(expected, actual)

    def test_posmanager_pos(self):
        text = self.helper_readFilename("no/article14.txt")
        self.posManager = PosManager(language="no")
        result = self.posManager.analyze(text)

        expected = """
        Check the common words for the article
        """
        text = self.helper_readFilename('no/article14.txt')
        self.posManager = PosManager(language="no")
        result = self.posManager.analyze(text)

        expected = [(u'Hvordan', 'RB'), (u'er', 'VBT'), (u'Magnor', 'NNP'),
                    (u'Glassverk', 'NNP'), (u'kontra', 'IN'), (u'det', 'DT'),
                    (u'mer', 'JJR'), (u'ber\xf8mte', 'JJ'), (u'Hadeland', 'NNP'),
                    (u'?', 'UKN'), (u'Hei', 'VB'), (u'!', 'UKN'), (u'Har', 'VBT'),
                    (u'tidligere', 'JJR'), (u'bes\xf8kt', 'VBN'), (u'det', 'DT'),
                    (u'ber\xf8mte', 'JJ'), (u'Hadeland', 'NNP'), (u'Glassverk', 'NNP'),
                    (u'opptil', 'IN'), (u'flere', 'JJR'), (u'ganger', 'NNS'), (u'.', 'UKN'),
                    (u'Koselig', 'JJ'), (u'sted', 'NN'), (u'med', 'IN'), (u'mye', 'JJ'),
                    (u'mer', 'JJR'), (u'en', 'PRP'), (u'bare', 'RB'), (u'glassbl\xe5sing', 'NN'),
                    (u'.', 'UKN'), (u'S\xe6rlig', 'JJ'), (u'rundt', 'IN'), (u'juletider', 'NNS'),
                    (u'er', 'VBT'), (u'det', 'DT'), (u'trivelig', 'JJ'), (u'der', 'IN'), (u',', 'UKN'),
                    (u'med', 'IN'), (u'kanefart', 'NN'), (u',', 'UKN'), (u'nisser', 'NNS'), (u'og', 'CC'),
                    (u'mulighet', 'NN'), (u'for', 'IN'), (u'og', 'CC'), (u'beskue', 'VB'),
                    (u'bier', 'NNS'), (u'som', 'UKN'), (u'lager', 'VBT'), (u'honning', 'NN'),
                    (u'.', 'UKN'), (u'For', 'IN'), (u'ikke', 'RB'), (u'og', 'CC'), (u'glemme', 'VB'),
                    (u'L\xf8iten', 'NNP'), (u'Lys', 'NNP'), (u'AS', 'NNP'), (u'.', 'UKN'),
                    (u'Selvbl\xe5s', 'NNP'), (u'av', 'IN'), (u'glass', 'NN'), (u'har', 'VBT'),
                    (u'jeg', 'PRP'), (u'ogs\xe5', 'RB'), (u'deltatt', 'VBN'), (u'p\xe5', 'IN'),
                    (u'selvf\xf8lgelig', 'JJ'), (u'.', 'UKN'), (u'Men', 'CC'), (u'i', 'IN'),
                    (u'det', 'DT'), (u'siste', 'JJ'), (u'(', 'UKN'), (u'selvom', 'NN'),
                    (u'det', 'DT'), (u'begynner', 'VBT'), (u'og', 'CC'), (u'bli', 'VB'),
                    (u'en', 'DT'), (u'del', 'NN'), (u'\xe5r', 'NN'), (u'siden', 'UKN'),
                    (u'jeg', 'PRP'), (u'var', 'VBD'), (u'der', 'IN'), (u'sist', 'RB'),
                    (u')', 'UKN'), (u'synes', 'VBN'), (u'jeg', 'PRP'), (u'stedet', 'NN'),
                    (u'har', 'VBT'), (u'begynt', 'VBN'), (u'og', 'CC'), (u'b\xe6re', 'VB'),
                    (u'preg', 'NN'), (u'av', 'IN'), (u'ALT', 'PRP'), (u'for', 'IN'),
                    (u'kommersiell', 'JJ'), (u'"Turistfelle"', 'NNP'), (u'!', 'UKN'), (u'Taxfree', 'NNP'),
                    (u'flagg', 'NN'), (u'overalt', 'RB'), (u',', 'UKN'), (u'og', 'CC'),
                    (u'dr\xf8ssevis', 'RB'), (u'med', 'IN'), (u'\xab', 'UKN'), (u'Folk', 'NNS'),
                    (u'ELSKER', 'VBT'), (u'oss', 'PRP'), (u'p\xe5', 'IN'), (u'Yelp', 'NNP'),
                    (u'"', 'UKN'), (u'og', 'CC'), (u'\xabNumber 1 Christmas Attraction on TripAdvisor"', 'NNP'),
                    (u'klistremerker', 'NNS'), (u'p\xe5', 'IN'), (u'ALLE', 'DT'), (u'd\xf8rer', 'NNS'),
                    (u'.', 'UKN'), (u'Derfor', 'RB'), (u'lurte', 'VBD'), (u'jeg', 'PRP'), (u'p\xe5', 'IN'),
                    (u':', 'UKN'), (u'Hvordan', 'RB'), (u'er', 'VBT'), (u'Magnor', 'NNP'),
                    (u'Glassverk', 'NNP'), (u'?', 'UKN'), (u'Aner', 'NNS'), (u'ikke', 'RB'),
                    (u'noe', 'PRP'), (u'om', 'IN'), (u'det', 'DT'), (u',', 'UKN'), (u'annet', 'DT'),
                    (u'en', 'PRP'), (u'at', 'UKN'), (u'jeg', 'PRP'), (u'synes', 'VBT'),
                    (u'det', 'DT'), (u'de', 'PRP'), (u'lager', 'NNS'), (u'er', 'VBT'),
                    (u'helt', 'JJ'), (u'nydlig', 'JJ'), (u',', 'UKN'), (u'og', 'CC'),
                    (u'mye', 'JJ'), (u'mer', 'JJR'), (u'personlig', 'JJ'), (u'en', 'DT'),
                    (u'Hadeland', 'NNP'), (u'.', 'UKN'), (u'Er', 'VBT'), (u'det', 'DT'),
                    (u'lett', 'JJ'), (u'og', 'CC'), (u'komme', 'NN'), (u'seg', 'PRP'),
                    (u'dit', 'IN'), (u'med', 'IN'), (u'buss', 'NN'), (u'/', 'UKN'),
                    (u'tog', 'NNS'), (u'fra', 'IN'), (u'Oslo', 'NNP'), (u'?', 'UKN'),
                    (u'Hva', 'PRP'), (u'kan', 'VBT'), (u'de', 'PRP'), (u'tilby', 'VB'),
                    (u',', 'UKN'), (u'annet', 'DT'), (u'en', 'PRP'), (u'glassutsalg', 'NN'),
                    (u'?', 'UKN'), (u'Har', 'VBT'), (u'de', 'PRP'), (u'omvisning', 'NN'),
                    (u',', 'UKN'), (u'etc', 'RB'), (u'?', 'UKN'), (u'Vil', 'VBT'), (u'gjerne', 'RB'), (u'ta', 'VB'),
                    (u'med', 'IN'), (u'dama', 'NN'), (u'dit', 'IN'), (u'f\xf8r', 'IN'), (u'jul', 'NN'), (u',', 'UKN'),
                    (u'men', 'CC'), (u'veldig', 'JJ'), (u'langt', 'JJ'), (u'og', 'CC'), (u'dra', 'VB'), (u'hvis', 'UKN'),
                    (u'det', 'DT'), (u'bare', 'RB'), (u'er', 'VBT'), (u'snakk', 'NNS'), (u'om', 'IN'), (u'en', 'DT'),
                    (u'vanlig', 'JJ'), (u'glassbutikk', 'NN'), (u'!', 'UKN'), (u'Er', 'VBT'), (u'det', 'DT'),
                    (u'koslig', 'JJ'), (u',', 'UKN'), (u'p\xe5', 'IN'), (u'samme', 'DT'), (u'm\xe5te', 'NN'), (u'?', 'UKN')]

        actual = result.get('pos', None)

        self.assertIsNotNone(actual)
        self.assertEquals(expected, actual)

    def test_posmanager_common_words_article15(self):
        """
        Check the common words for the article
        """
        text = self.helper_readFilename('no/article15.txt')
        self.posManager = PosManager(language="no")
        result = self.posManager.analyze(text)

        expected = sorted([(u'polen', 1), (u'uggs', 1)])
        actual = sorted(result.get('common_words', []))

        self.assertIsNotNone(actual)
        self.assertEquals(expected, actual)

    def test_posmanager_common_words_article16(self):
        """
        Check the common words for the article
        """
        text = self.helper_readFilename('no/article16.txt')
        self.posManager = PosManager(language="no")
        result = self.posManager.analyze(text)

        expected = sorted([(u'melodien', 1), (u'm\xe5ten', 1), (u'navn', 1), (u'sang', 1), (u'sangarten', 1), (u'typen', 1)])
        actual = sorted(result.get('common_words', []))

        self.assertIsNotNone(actual)
        self.assertEquals(expected, actual)

    def helper_readFilename(self, filename=''):
        stopwords = []
        if not filename:
            raise Exception("The file is empty")

        fileToRead = "%s%s" % (self.testTextsDirectory, filename)

        with open(fileToRead) as f:
            text = f.read()
        #f.close()
        return text


if __name__ == '__main__':
    unittest.main()
