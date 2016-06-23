from . import OBTManager
import unittest
import os

class OBTManagerTestCase(unittest.TestCase):
    #### TODO: Dockerize these tests. They need to use OBT
    obtManager = None
    currentDirectory = currentDirectory = "%s" % (os.path.dirname(os.path.realpath(__file__)), )
    testTextsDirectory = "%s/../../../data/text/" % (currentDirectory, )

    def setUp(self):
        self.obtManager = None

    def tearDown(self):
        self.obtManager.cleanUp()
        self.obtManager = None


    def test_pos_obt_initizialize(self):
        """
        Check if the initialization works
        """
        text = "Det er norsk"
        self.obtManager = OBTManager(text)
        self.assertTrue(self.obtManager._filename is not None)


if __name__ == '__main__':
    unittest.main()
