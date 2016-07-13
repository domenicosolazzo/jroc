# -*- coding: utf-8 -*-
from . import OBTManager
from . import StopwordManager
import unittest
import os
import codecs

# Stopword manager
stopwordManagerNorwegian = StopwordManager(language="no")
# Norwegian stopwords
stopwordsNorwegian = stopwordManagerNorwegian.getStopWords()

class OBTManagerTestCase(unittest.TestCase):
    #### TODO: Dockerize these tests. They need to use OBT
    obtManager = None
    currentDirectory = currentDirectory = "%s" % (os.path.dirname(os.path.realpath(__file__)), )
    testTextsDirectory = "%s/../../../../data/text/" % (currentDirectory, )

    def setUp(self):
        text = "Det er norsk"
        self.obtManager = OBTManager(text)

    def tearDown(self):
        #self.obtManager.cleanUp()
        self.obtManager = None


    def test_pos_obt_initizialize(self):
        """
        Check if the initialization works
        """
        result = self.obtManager.obtAnalyze()

        self.assertTrue(self.obtManager is not None)

    def test_pos_obt_analyze(self):
        """
        Check the analyze method of OBT
        """
        result = self.obtManager.obtAnalyze()

        wordNumber = 3
        self.assertTrue(len(result) == wordNumber) # sentence: Det er norsk
        self.assertTrue(isinstance(result, list))
        self.assertTrue(result is not None)

    def test_pos_obt_entities(self):
        """
        Check the entities method of OBT
        """
        text = "Ivar Aasen ble født på gården Åsen i Hovdebygda på Sunnmøre som sønn av småbrukeren Ivar Jonsson."
        self.obtManager = OBTManager(text)
        actual = self.obtManager.findEntities(stopwords=[])

        expectedEntities = [u'Sunnm\xf8re', u'\xc5sen', u'Ivar Aasen', u'Ivar Jonsson', u'Hovdebygda']
        expectedEntitiesCount = len(expectedEntities)

        self.assertTrue(actual is not None)
        self.assertTrue(isinstance(actual, list))
        self.assertTrue(len(actual) == expectedEntitiesCount)
        self.assertEquals(expectedEntities, actual)


    def test_pos_obt_tags(self):
        """
        Check the tags method of OBT
        """
        text = "Ivar Aasen ble født på gården Åsen i Hovdebygda på Sunnmøre som sønn av småbrukeren Ivar Jonsson."
        self.obtManager = OBTManager(text)
        actual = self.obtManager.findTags()

        expectedEntities = [u'Ivar', u'Aasen', u'Sunnm\xf8re', u'\xc5sen', u'Hovdebygda', u'Jonsson']
        expectedEntitiesCount = len(expectedEntities)

        self.assertTrue(actual is not None)
        self.assertTrue(isinstance(actual, list))
        self.assertTrue(len(actual) == expectedEntitiesCount)
        self.assertEquals(expectedEntities, actual)

    ##################################################################################################
    ##################################################################################################
    ###################### TESTING SEVERAL NORWEGIAN ARTICLES ########################################
    ##################################################################################################
    ##################################################################################################
    def test_pos_article1_entities(self):
        """
        Test the entities returned for 'article1.txt'
        """
        text = self.helper_readFilename('no/article1.txt')
        self.obtManager = OBTManager(text)
        actual = self.obtManager.findEntities(stopwords=[])

        expectedEntities = [u'NRK', u'Vegdirektoratet', u'Dykkarar', u'Lastebileigarforbundet', u'Her', u'VG', u'Vi', u'Eg', u'E136', u'Det', u'Dersom', u'Lars Hardeland',
                            u'Stensvold.', u'Rauma', u'Noreg', u'Statens', u'Stengde', u'Nettbuss', u'Stensvold', u'Dagrunn Krakeli', u'Ein']
        expectedEntitiesCount = len(expectedEntities)

        self.assertTrue(actual is not None)
        self.assertTrue(isinstance(actual, list))
        self.assertEquals(expectedEntitiesCount, len(actual))
        self.assertEquals(expectedEntities, actual)

    def test_pos_article1_entities_with_norwegian_with_stopwords(self):
        """
        Test the entities returned for 'article1.txt' after filtering the norwegian stopwords
        """
        text = self.helper_readFilename('no/article1.txt')
        self.obtManager = OBTManager(text)

        actual = self.obtManager.findEntities(stopwords=stopwordsNorwegian)
        expectedEntities = [u'NRK', u'Vegdirektoratet', u'Lastebileigarforbundet', u'VG', u'Stengde', u'Dykkarar', u'Stensvold.', u'Rauma', u'Noreg', u'Statens', u'E136', u'Nettbuss', u'Stensvold', u'Dagrunn Krakeli', u'Lars Hardeland']
        expectedEntitiesCount = len(expectedEntities)

        self.assertTrue(actual is not None)
        self.assertTrue(isinstance(actual, list))
        self.assertEquals(expectedEntitiesCount, len(actual))
        self.assertEquals(expectedEntities, actual)

    def test_pos_article1_tags(self):
        """
        Test the tags returned for 'article1.txt'
        """
        text = self.helper_readFilename('no/article1.txt')
        self.obtManager = OBTManager(text)

        actual = self.obtManager.findTags()
        expectedTags = [u'Lars', u'Her', u'Stensvold.', u'Rauma', u'Nettbuss', u'Stensvold', u'Dagrunn', u'Lastebileigarforbundet', u'Vegdirektoratet', u'Dykkarar', u'Dersom',
                        u'Krakeli', u'Hardeland', u'VG', u'Stengde', u'Det', u'Noreg', u'Ein', u'NRK', u'Vi', u'Eg', u'Statens', u'E136']
        expectedTagsCount = len(expectedTags)

        self.assertTrue(actual is not None)
        self.assertTrue(isinstance(actual, list))
        self.assertEquals(expectedTagsCount, len(actual))
        self.assertEquals(expectedTags, actual)

    def test_pos_article1_tags_with_stopwords(self):
        """
        Test the tags returned for 'article1.txt' after filtering the norwegian stopwords
        """
        text = self.helper_readFilename('no/article1.txt')
        self.obtManager = OBTManager(text)

        expectedTags = [u'Lars', u'Stensvold.', u'Rauma', u'Nettbuss', u'Stensvold', u'Dagrunn', u'Lastebileigarforbundet', u'Vegdirektoratet', u'Dykkarar', u'Krakeli', u'Hardeland', u'VG', u'Stengde', u'Noreg', u'NRK', u'Statens', u'E136']
        expectedTagsCount = len(expectedTags)

        actual = self.obtManager.findTags()
        actual = [tag for tag in actual if not tag.lower() in stopwordsNorwegian]

        self.assertTrue(actual is not None)
        self.assertTrue(isinstance(actual, list))
        self.assertEquals(expectedTagsCount, len(actual))
        self.assertEquals(expectedTags, actual)



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
