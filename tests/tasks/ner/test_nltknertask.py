
from . import NLTKTaggerTask
import unittest
import os

text = ""

class NLTKTaggerTaskTestCase(unittest.TestCase):
    task = None
    name = "NLTK Tagger Test Task"
    currentDirectory = currentDirectory = "%s" % (os.path.dirname(os.path.realpath(__file__)), )
    testTextsDirectory = "%s/../../data/text/" % (currentDirectory, )


    def setUp(self):
        self.task = NLTKTaggerTask(self.name)

    def tearDown(self):
        self.task = None

    def test_task_initialization_fails_if_name_is_None(self):
        """
        Test that a task throws an exception if the name is None
        """
        name = None

        self.assertRaises(Exception, NLTKTaggerTask, name)

    def test_task_initialization_fails_if_name_is_empty(self):
        """
        Test that a task throws an exception if the name is empty
        """
        name = ""

        self.assertRaises(Exception, NLTKTaggerTask, name)

    def test_task_initialization_with_valid_name(self):
        """
        Test the initialization of the NLTKTaggerTask
        """
        self.assertIsNotNone(self.task)

    def test_task_execute_with_input_without_main_key(self):
        """
        Test that the NLTKTaggerTask fails if a requested key is missing (pos-no)
        """
        input = {}
        self.task.execute(input)
        self.assertTrue(self.task.hasFailed())

    def test_task_execute_with_valid_json(self):
        """
        Test that the NLTKTaggerTask is extracting data from the json
        """
        text = self.helper_readFilename("en/article1.txt")
        input = {"data": text}

        self.task.execute(input)

        actual = self.task.getOutput()
        expected = {'data': [(u'House', 'ORGANIZATION'), (u'Senate', 'ORGANIZATION'), (u'GOP', 'ORGANIZATION'),
                            (u'John Mc', 'PERSON'), (u'Cain', 'GPE'), (u'R', 'ORGANIZATION'), (u'Iraq', 'GPE'),
                            (u'Syria', 'GSP'), (u'Afghanistan', 'GPE'), (u'Republican', 'ORGANIZATION'),
                            (u'Donald Trump', 'PERSON'), (u'Story Continued Below', 'PERSON'), (u'Randy Forbes', 'PERSON'),
                            (u'Virginia', 'GPE'), (u'Armed Services Committee', 'ORGANIZATION'), (u'Cain', 'PERSON'),
                            (u'R', 'ORGANIZATION'), (u'House', 'ORGANIZATION'), (u'Senate', 'ORGANIZATION'),
                            (u'House Armed Services', 'ORGANIZATION'), (u'House', 'ORGANIZATION'), (u'Senate', 'ORGANIZATION'),
                            (u'Democrats', 'ORGANIZATION'), (u'Robert Byrd', 'PERSON'), (u'Ted Kennedy', 'ORGANIZATION'),
                            (u'House Armed Services Chairman Mac Thornberry', 'PERSON'), (u'R', 'ORGANIZATION'),
                            (u'Texas', 'GPE'), (u'Congress', 'ORGANIZATION'), (u'National Defense', 'ORGANIZATION'),
                            (u'Pentagon', 'GPE'), (u'Congress', 'ORGANIZATION'), (u'Pentagon', 'ORGANIZATION'),
                            (u'Mackenzie Eaglen', 'PERSON'), (u'American Enterprise Institute', 'ORGANIZATION'),
                            (u'Senate Armed Services', 'ORGANIZATION'), (u'POLITICO', 'ORGANIZATION'),
                            (u'Carl Levin', 'PERSON'), (u'D', 'ORGANIZATION'), (u'Independent', 'ORGANIZATION'),
                            (u'Joe Lieberman', 'PERSON'), (u'Connecticut', 'GSP'), (u'Kennedy', 'PERSON'),
                            (u'Byrd', 'PERSON'), (u'House Armed Service Committee', 'ORGANIZATION'), (u'Virginian', 'GPE'),
                            (u'House Armed Services Republican', 'ORGANIZATION'), (u'Seapower Subcommittee', 'ORGANIZATION'),
                            (u'Obama', 'ORGANIZATION'), (u'House Republican', 'ORGANIZATION'), (u'Joe Heck', 'PERSON'),
                            (u'Nevada', 'GPE'), (u'Senate', 'ORGANIZATION'), (u'Minority', 'ORGANIZATION'),
                            (u'Harry Reid', 'PERSON'), (u'Loretta Sanchez', 'PERSON'), (u'California', 'GPE'),
                            (u'Senate', 'ORGANIZATION'), (u'Jeff Miller', 'PERSON'), (u'Florida', 'GPE'),
                            (u'John Kline', 'PERSON'), (u'Minnesota', 'ORGANIZATION'), (u'Armed Services', 'ORGANIZATION'),
                            (u'Chris Gibson', 'PERSON'), (u'R', 'ORGANIZATION'), (u'Army', 'ORGANIZATION'),
                            (u'Marine Corps', 'PERSON'), (u'HASC', 'ORGANIZATION'), (u'Justin Johnson', 'PERSON'),
                            (u'House Armed Services', 'ORGANIZATION'), (u'Heritage Foundation', 'ORGANIZATION'),
                            (u'Senate Armed Services Committee', 'ORGANIZATION'), (u'Cain', 'PERSON'), (u'Ayotte', 'PERSON'),
                            (u'Ayotte', 'PERSON'), (u'Readiness Subcommittee', 'ORGANIZATION'), (u'White House', 'FACILITY'),
                            (u'Guantanamo Bay', 'ORGANIZATION'), (u'Cuba', 'GPE'), (u'First', 'PERSON'),
                            (u'New Hampshire Republican', 'ORGANIZATION'), (u'Obama', 'ORGANIZATION'),
                            (u'NDAA', 'ORGANIZATION'), (u'Cain', 'PERSON'), (u'Senate Armed Services', 'ORGANIZATION'),
                            (u'Pentagon', 'ORGANIZATION'), (u'Heritage', 'PERSON'), (u'Johnson', 'PERSON'),
                            (u'Republican', 'ORGANIZATION'), (u'Oklahoma', 'PERSON'), (u'Jim Inhofe', 'PERSON'),
                            (u'Mc', 'GPE'), (u'Cain', 'PERSON'), (u'Eaglen', 'PERSON'), (u'Senate', 'ORGANIZATION'),
                            (u'Eaglen', 'PERSON'), (u'Senate', 'ORGANIZATION'), (u'Mieke Eoyang', 'PERSON'),
                            (u'House Armed Services', 'ORGANIZATION'), (u'Kennedy', 'PERSON'), (u'Third Way', 'PERSON'),
                            (u'Eoyang', 'PERSON'), (u'HASC', 'ORGANIZATION'), (u'Johnson', 'PERSON'),
                            (u'House Armed Services', 'ORGANIZATION'), (u'Democrat Adam Smith', 'PERSON'),
                            (u'Washington', 'GPE'), (u'Thornberry', 'PERSON'), (u'Smith', 'PERSON'),
                            (u'Democrats Marc Veasey', 'ORGANIZATION'), (u'Texas', 'GPE'), (u'Seth Moulton', 'PERSON'),
                            (u'Massachusetts', 'GPE'), (u'Republicans Martha Mc', 'ORGANIZATION'), (u'Sally', 'PERSON'),
                            (u'Arizona', 'GPE'), (u'Jackie Walorski', 'PERSON'), (u'Indiana', 'GPE'), (u'Thornberry', 'PERSON'),
                            (u'Congress', 'ORGANIZATION'), (u'Marine', 'GPE'), (u'Iraq', 'GPE'), (u'Afghanistan', 'GPE'),
                            (u'Thornberry', 'PERSON')]}
        self.assertEquals(expected, actual)

    def test_task_execute_with_valid_json_norwegian_article1(self):
        """
        Test that the NLTKTaggerTask is extracting data from the json (article1.txt)
        """
        text = self.helper_readFilename("no/article1.txt")
        input = {"data": text}

        self.task.execute(input)

        actual = self.task.getOutput()
        expected = {'data': [(u'Noreg', 'GPE'), (u'NRK', 'ORGANIZATION'),
                            (u'Stengde', 'PERSON'), (u'M\xe5ndag', 'PERSON'),
                            (u'Rauma', 'PERSON'), (u'E136', 'PERSON'), (u'Dykkarar', 'PERSON'),
                            (u'Dette', 'PERSON'), (u'Stensvold', 'PERSON'), (u'Dersom', 'PERSON'),
                            (u'Tryggleiken', 'PERSON'), (u'Men', 'PERSON'), (u'Ein', 'PERSON'),
                            (u'Lars Hardeland', 'PERSON'), (u'Nettbuss', 'PERSON'), (u'Dagrunn Krakeli', 'PERSON')]}
        self.assertEquals(expected, actual)

    def test_task_execute_with_valid_json_norwegian_article2(self):
        """
        Test that the StanfordTaggerTask is extracting data from the json (article2.txt)
        """
        text = self.helper_readFilename("no/article2.txt")
        input = {"data": text}

        self.task.execute(input)

        actual = self.task.getOutput()

        expected = {'data': [(u'Nylig', 'PERSON'), (u'N\xe5', 'PERSON'),
                            (u'Sun', 'ORGANIZATION'), (u'Daily Mail', 'PERSON'),
                            (u'Sun', 'ORGANIZATION'), (u'Audi Polo', 'PERSON'),
                            (u'Coworth Park', 'PERSON'), (u'Berkshire', 'ORGANIZATION'),
                            (u'Saken', 'PERSON'), (u'Harry', 'PERSON'), (u'Audis Polo', 'PERSON'),
                            (u'Coworth', 'PERSON'), (u'Berkshire', 'ORGANIZATION'),
                            (u'Ellie Goulding', 'PERSON'), (u'Rex Features', 'PERSON'),
                            (u'Avisen', 'PERSON'), (u'Kvelden', 'GPE'), (u'Harry', 'ORGANIZATION'),
                            (u'Harry', 'PERSON'), (u'Men Harry', 'PERSON'), (u'Ellie', 'PERSON'),
                            (u'De', 'PERSON'), (u'De', 'PERSON'), (u'Harry', 'PERSON'),
                            (u'Ellie', 'PERSON'), (u'Suns', 'ORGANIZATION'), (u'Saken', 'PERSON'),
                            (u'Skuespiller Tom Hardy', 'PERSON'), (u'Leonardo Di', 'PERSON'),
                            (u'Harry', 'PERSON'), (u'Ellie Goudling', 'PERSON'), (u'Rex Features', 'PERSON'),
                            (u'If\xf8lge', 'PERSON'), (u'Sun', 'ORGANIZATION'), (u'Harry', 'PERSON'),
                            (u'Could', 'PERSON'), (u'Sun', 'ORGANIZATION'), (u'Avisens', 'PERSON'),
                            (u'Harrys', 'PERSON'), (u'Han', 'GPE'), (u'Ellie', 'PERSON'), (u'Hverken', 'PERSON'),
                            (u'Harry', 'PERSON'), (u'Ellie Goulding', 'PERSON'), (u'Saken', 'PERSON'),
                            (u'N\xc6RT', 'ORGANIZATION'), (u'B\xe5de Ellie Goulding', 'PERSON'), (u'Harry', 'PERSON'),
                            (u'Kate', 'ORGANIZATION'), (u'William', 'PERSON'), (u'Westminister Abbey', 'PERSON'),
                            (u'NTB Scanpix', 'ORGANIZATION'), (u'GOD', 'ORGANIZATION'), (u'Prns Harry', 'PERSON'),
                            (u'Ellie Goulding', 'PERSON'), (u'Mirror', 'GPE'), (u'Kort', 'PERSON'), (u'Folk', 'GPE'),
                            (u'Sun', 'ORGANIZATION'), (u'Saken', 'PERSON'), (u'Ellie Goulding', 'PERSON'),
                            (u'Dougie Poynter', 'PERSON'), (u'London', 'GPE'), (u'Konserten', 'PERSON'),
                            (u'Hun', 'PERSON'), (u'Hun', 'PERSON'), (u'Joner', 'PERSON'), (u'Seogh\xf8r', 'PERSON')]}
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
