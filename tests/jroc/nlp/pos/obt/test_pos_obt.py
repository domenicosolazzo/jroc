# -*- coding: utf-8 -*-
from . import OBTManager
import unittest
import os

class OBTManagerTestCase(unittest.TestCase):
    #### TODO: Dockerize these tests. They need to use OBT
    obtManager = None
    currentDirectory = currentDirectory = "%s" % (os.path.dirname(os.path.realpath(__file__)), )
    testTextsDirectory = "%s/../../../data/text/" % (currentDirectory, )

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
        self.assertTrue(result is not None)

    def test_pos_obt_entities(self):
        """
        Check the entities method of OBT
        """
        result = self.obtManager.findEntities(stopwords=[])
        self.assertTrue(result is not None)

    def test_pos_obt_tags(self):
        """
        Check the tags method of OBT
        """
        result = self.obtManager.findTags()
        self.assertTrue(result is not None)




if __name__ == '__main__':
    unittest.main()
