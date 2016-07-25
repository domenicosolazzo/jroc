
from . import StanfordTaggerTask
import unittest
import os

text = ""

class StanfordTaggerTaskTestCase(unittest.TestCase):
    task = None
    name = "Stanford Tagger Test Task"
    currentDirectory = currentDirectory = "%s" % (os.path.dirname(os.path.realpath(__file__)), )
    testTextsDirectory = "%s/../../data/text/" % (currentDirectory, )


    def setUp(self):
        self.task = StanfordTaggerTask(self.name)

    def tearDown(self):
        self.task = None

    def test_task_initialization_fails_if_name_is_None(self):
        """
        Test that a task throws an exception if the name is None
        """
        name = None

        self.assertRaises(Exception, StanfordTaggerTask, name)

    def test_task_initialization_fails_if_name_is_empty(self):
        """
        Test that a task throws an exception if the name is empty
        """
        name = ""

        self.assertRaises(Exception, StanfordTaggerTask, name)

    def test_task_initialization_with_valid_name(self):
        """
        Test the initialization of the StanfordTaggerTask
        """
        self.assertIsNotNone(self.task)

    def test_task_execute_with_input_without_main_key(self):
        """
        Test that the StanfordTaggerTask fails if a requested key is missing (pos-no)
        """
        input = {}
        self.task.execute(input)
        self.assertTrue(self.task.hasFailed())

    def test_task_execute_with_valid_json(self):
        """
        Test that the StanfordTaggerTask is extracting data from the json
        """
        text = self.helper_readFilename("en/article1.txt")
        input = {"data": text}

        self.task.execute(input)

        actual = self.task.getOutput()
        print("ACTUAL", actual, self.task.hasFailed(), self.task.getError())
        expected = {'data': [(u'House', u'ORGANIZATION'), (u'Senate', u'ORGANIZATION'),
                            (u'GOP', u'ORGANIZATION'), (u'John Mc', u'PERSON'), (u'Cain', u'PERSON'),
                            (u'Ariz.', u'LOCATION'), (u'Iraq', u'LOCATION'), (u'Syria', u'LOCATION'),
                            (u'Afghanistan', u'LOCATION'), (u'Donald Trump', u'PERSON'),
                            (u'Randy Forbes', u'PERSON'), (u'Virginia', u'LOCATION'),
                            (u'Armed Services Committee', u'ORGANIZATION'), (u'Cain', u'PERSON'),
                            (u'Kelly Ayotte', u'PERSON'), (u'N. H. )', u'PERSON'), (u'House', u'ORGANIZATION'),
                            (u'Senate', u'ORGANIZATION'), (u'House Armed Services', u'ORGANIZATION'),
                            (u'House', u'ORGANIZATION'), (u'Senate', u'ORGANIZATION'), (u'Robert Byrd', u'PERSON'),
                            (u'Ted Kennedy', u'PERSON'), (u'House Armed Services Chairman Mac Thornberry ( R', u'ORGANIZATION'),
                            (u'Texas', u'LOCATION'), (u'Congress', u'ORGANIZATION'), (u'Pentagon', u'ORGANIZATION'),
                            (u'Congress', u'ORGANIZATION'), (u'Pentagon', u'ORGANIZATION'), (u'Mackenzie Eaglen', u'PERSON'),
                            (u'American Enterprise Institute', u'ORGANIZATION'), (u'Senate Armed Services', u'ORGANIZATION'),
                            (u'POLITICO', u'ORGANIZATION'), (u'Carl Levin', u'PERSON'), (u'Mich.', u'LOCATION'),
                            (u'Joe Lieberman', u'PERSON'), (u'Connecticut', u'LOCATION'), (u'Kennedy', u'PERSON'),
                            (u'Byrd', u'PERSON'), (u'House Armed Service Committee', u'ORGANIZATION'), (u'Forbes', u'PERSON'),
                            (u'House Armed Services Republican', u'ORGANIZATION'), (u'Seapower Subcommittee', u'ORGANIZATION'),
                            (u'Obama', u'PERSON'), (u'Navy', u'ORGANIZATION'), (u'Joe Heck', u'PERSON'), (u'Nevada', u'LOCATION'),
                            (u'Senate', u'ORGANIZATION'), (u'Harry Reid', u'PERSON'), (u'Loretta Sanchez', u'PERSON'),
                            (u'California', u'LOCATION'), (u'Senate', u'ORGANIZATION'), (u'Jeff Miller', u'PERSON'),
                            (u'Florida', u'LOCATION'), (u'John Kline', u'PERSON'), (u'Minnesota', u'LOCATION'),
                            (u'Armed Services', u'ORGANIZATION'), (u'Chris Gibson', u'PERSON'), (u'N. Y. )', u'PERSON'),
                            (u'Army', u'ORGANIZATION'), (u'Marine Corps', u'ORGANIZATION'), (u'HASC', u'ORGANIZATION'),
                            (u'Justin Johnson', u'PERSON'), (u'House Armed Services Republicans', u'ORGANIZATION'),
                            (u'Heritage Foundation', u'ORGANIZATION'), (u'Senate Armed Services Committee', u'ORGANIZATION'),
                            (u'Mc', u'PERSON'), (u'Cain', u'PERSON'), (u'Ayotte', u'PERSON'), (u'Ayotte', u'PERSON'),
                            (u'Readiness Subcommittee', u'ORGANIZATION'), (u'White House', u'ORGANIZATION'),
                            (u'Guantanamo Bay', u'LOCATION'), (u'Cuba', u'LOCATION'), (u'New Hampshire Republican', u'ORGANIZATION'),
                             (u'Obama', u'PERSON'), (u'NDAA', u'ORGANIZATION'), (u'Mc', u'PERSON'), (u'Cain', u'PERSON'),
                             (u'Senate Armed Services', u'ORGANIZATION'), (u'Pentagon', u'ORGANIZATION'),
                             (u'Heritage', u'ORGANIZATION'), (u'Johnson', u'PERSON'), (u'Oklahoma', u'LOCATION'),
                             (u'Jim Inhofe', u'PERSON'), (u'Mc', u'LOCATION'), (u'Cain', u'PERSON'), (u'Eaglen', u'PERSON'),
                             (u'Senate', u'ORGANIZATION'), (u'Eaglen', u'PERSON'), (u'Senate', u'ORGANIZATION'),
                             (u'Mieke Eoyang', u'PERSON'), (u'House Armed Services', u'ORGANIZATION'), (u'Kennedy', u'PERSON'),
                             (u'Eoyang', u'PERSON'), (u'HASC', u'ORGANIZATION'), (u'Johnson', u'PERSON'),
                             (u'House Armed Services', u'ORGANIZATION'), (u'Adam Smith', u'PERSON'), (u'Washington', u'LOCATION'),
                             (u'Thornberry', u'PERSON'), (u'Smith', u'PERSON'), (u'Marc Veasey', u'PERSON'), (u'Texas', u'LOCATION'),
                             (u'Seth Moulton', u'PERSON'), (u'Massachusetts', u'LOCATION'), (u'Martha Mc', u'PERSON'), (u'Sally', u'PERSON'),
                             (u'Arizona', u'LOCATION'), (u'Jackie Walorski', u'PERSON'), (u'Indiana', u'LOCATION'), (u'Thornberry', u'PERSON'),
                             (u'Congress', u'ORGANIZATION'), (u'Iraq', u'LOCATION'), (u'Afghanistan', u'LOCATION'), (u'Thornberry', u'PERSON')]}
        self.assertEquals(expected, actual)

    def test_task_execute_with_valid_json_norwegian_article1(self):
        """
        Test that the StanfordTaggerTask is extracting data from the json (article1.txt)
        """
        text = self.helper_readFilename("no/article1.txt")
        input = {"data": text}

        self.task.execute(input)

        actual = self.task.getOutput()
        expected = {'data': [(u'NRK', u'ORGANIZATION'), (u'Rauma', u'ORGANIZATION'),
                            (u'Lars Hardeland', u'PERSON'), (u'Dagrunn Krakeli', u'PERSON')]}
        self.assertEquals(expected, actual)

    def test_task_execute_with_valid_json_norwegian_article2(self):
        """
        Test that the StanfordTaggerTask is extracting data from the json (article2.txt)
        """
        text = self.helper_readFilename("no/article2.txt")
        input = {"data": text}

        self.task.execute(input)

        actual = self.task.getOutput()
        expected = {'data': [(u'Sunday Times', u'ORGANIZATION'), (u'Coworth Park', u'LOCATION'),
                            (u'Berkshire', u'ORGANIZATION'), (u'Prins Harry', u'PERSON'),
                            (u'Berkshire', u'ORGANIZATION'), (u'Ellie Goulding', u'PERSON'),
                            (u'Rex Features', u'PERSON'), (u'Harry', u'PERSON'), (u'Ellie', u'PERSON'),
                            (u'Ellie', u'PERSON'), (u'Suns', u'ORGANIZATION'), (u'Skuespiller Tom Hardy', u'PERSON'),
                            (u'Leonardo Di', u'PERSON'), (u'Caprio', u'ORGANIZATION'), (u'Harry', u'PERSON'),
                            (u'Ellie Goudling', u'PERSON'), (u'Hardy', u'PERSON'), (u'Rex Features', u'PERSON'),
                            (u'Ellie', u'PERSON'), (u'Hverken', u'PERSON'), (u'Ellie Goulding', u'PERSON'),
                            (u'B\xe5de Ellie Goulding', u'PERSON'), (u'Kate', u'PERSON'), (u'William', u'PERSON'),
                            (u'NTB Scanpix', u'ORGANIZATION'), (u'Prns Harry', u'PERSON'), (u'Ellie Goulding', u'PERSON'),
                            (u'Westminster Abbey', u'ORGANIZATION'), (u'Kort', u'PERSON'), (u'Ellie Goulding', u'PERSON'),
                            (u'Dougie Poynter', u'PERSON'), (u'London', u'LOCATION'), (u'Konserten', u'PERSON'),
                            (u'Joner', u'PERSON')]}
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
