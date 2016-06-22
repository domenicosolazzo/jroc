from . import ObtManager
import unittest
import os

class OBTManagerTestCase(unittest.TestCase):
    obtManager = None
    currentDirectory = currentDirectory = "%s" % (os.path.dirname(os.path.realpath(__file__)), )
    testTextsDirectory = "%s/../../../data/text/" % (currentDirectory, )

    def setUp(self):
        self.obtManager = None

    def tearDown(self):
        self.obtManager = None


    def test_pos_obt_initizialize(self):
        """
        Check if the initialization works
        """
        text = self.helper_readFilename("no/ivar_aasen.txt")
        self.obtManager = ObtManager(text)
        expected = "no"
        actual = self.languageDetector.classify(text)[0]
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
