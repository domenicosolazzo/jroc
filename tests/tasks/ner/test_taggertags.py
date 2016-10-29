
from . import TaggerTagsTask
import unittest
import os

text = ""

class TaggerTagsTaskTestCase(unittest.TestCase):
    task = None
    name = "TaggerTags Test Task"
    currentDirectory = currentDirectory = "%s" % (os.path.dirname(os.path.realpath(__file__)), )
    testTextsDirectory = "%s/../../data/text/" % (currentDirectory, )


    def setUp(self):
        self.task = TaggerTagsTask(self.name)

    def tearDown(self):
        self.task = None

    def test_task_initialization_fails_if_name_is_None(self):
        """
        Test that a task throws an exception if the name is None
        """
        name = None

        self.assertRaises(Exception, TaggerTagsTask, name)

    def test_task_initialization_fails_if_name_is_empty(self):
        """
        Test that a task throws an exception if the name is empty
        """
        name = ""

        self.assertRaises(Exception, TaggerTagsTask, name)

    def test_task_initialization_with_valid_name(self):
        """
        Test the initialization of the TaggerTagsTask
        """
        self.assertIsNotNone(self.task)

    def test_task_execute_with_invalid_input(self):
        """
        Test that the TaggerTagsTask fails if the input does not have the correct data
        """
        input = {}

        self.task.execute(input)
        self.assertTrue(self.task.hasFailed())

    def test_task_execute_with_invalid_input_no_pos_key(self):
        """
        Test that the TaggerTagsTask fails if the input does not have the correct data (No POS Key)
        """
        input = {'data': None}

        self.task.execute(input)
        self.assertTrue(self.task.hasFailed())


    def test_task_execute_with_valid_json(self):
        """
        Test that the TaggerTagsTask is extracting data from the json
        """
        input = {"data": dict([('pos', [(u'Jan', 'NNP'), (u'Solberg', 'NNP'), (u'er', 'VBT'), (u'den', 'DT'), (u'nye', 'JJ'), (u'eieren', 'NN'), (u'av', 'IN'), (u'Bryggeri', 'NNP'), (u'G\xe5rdene', 'NNP'), (u'AS', 'NNP'), (u'.', 'UKN'), (u'Han', 'PRP'), (u'har', 'VBT'), (u'kj\xf8pt', 'VBN'), (u'samtlige', 'DT'), (u'aksjer', 'NNS'), (u'i', 'IN'), (u'selskapet', 'NN'), (u'fra', 'IN'), (u'Carl', 'NNP'), (u'Otto', 'NNP'), (u'S\xe6tre', 'NNP'), (u'.', 'UKN'), (u'Dette', 'PRP'), (u'melder', 'VBT'), (u'partene', 'NNS'), (u'i', 'IN'), (u'en', 'DT'), (u'pressemelding', 'NN'), (u'.', 'UKN'), (u'Der', 'IN'), (u'opplyser', 'VBT'), (u'de', 'PRP'), (u'ogs\xe5', 'RB'), (u'at', 'UKN'), (u'de', 'PRP'), (u'er', 'VBT'), (u'enige', 'JJ'), (u'om', 'IN'), (u'\xe5', 'UKN'), (u'ikke', 'RB'), (u'oppgi', 'VB'), (u'kj\xf8pesum', 'NN'), (u'for', 'IN'), (u'aksjene', 'NNS'), (u'.', 'UKN'), (u'Solberg', 'NNP'), (u'har', 'VBT'), (u'ogs\xe5', 'RB'), (u'inng\xe5tt', 'VBN'), (u'avtale', 'NN'), (u'med', 'IN'), (u'H\xf8nefoss', 'NNP'), (u'bryggeri', 'NNS'), (u'AS', 'NNP'), (u',', 'UKN'), (u'som', 'UKN'), (u'S\xe6tre', 'NNP'), (u'ogs\xe5', 'RB'), (u'eier', 'VBT'), (u',', 'UKN'), (u'om', 'IN'), (u'at', 'UKN'), (u'han', 'PRP'), (u'f\xe5r', 'VBT'), (u'benytte', 'VB'), (u'bryggeriets', 'NN'), (u'navn', 'NNS'), (u',', 'UKN'), (u'logo', 'NN'), (u'og', 'CC'), (u's\xe5', 'RB'), (u'videre', 'JJR'), (u'i', 'IN'), (u'markedsf\xf8ring', 'NN'), (u'og', 'CC'), (u'profilering', 'NN'), (u'i', 'NN'), (u'hva', 'PRP'), (u'enn', 'IN'), (u'den', 'DT'), (u'videre', 'JJR'), (u'driften', 'NN'), (u'inneb\xe6rer', 'VBT'), (u'.', 'UKN'), (u'Salget', 'NN'), (u'ble', 'VBD'), (u'inng\xe5tt', 'VBN'), (u'onsdag', 'NN'), (u'i', 'IN'), (u'forrige', 'DT'), (u'uke', 'NN'), (u'.', 'UKN'), (u'I', 'IN'), (u'pressemeldingen', 'NN'), (u'varsler', 'VBT'), (u'Solberg', 'NNP'), (u'at', 'UKN'), (u'han', 'PRP'), (u'vil', 'VBT'), (u'komme', 'VB'), (u'tilbake', 'IN'), (u'senere', 'JJR'), (u'med', 'IN'), (u'konkrete', 'JJ'), (u'planer', 'NNS'), (u'for', 'IN'), (u'bygningsmassen', 'NNS'), (u'.', 'UKN'), (u'Solberg', 'NNP'), (u'er', 'VBT'), (u'fra', 'IN'), (u'f\xf8r', 'IN'), (u'en', 'DT'), (u'av', 'IN'), (u'deleierne', 'NNS'), (u'i', 'IN'), (u'Hotell', 'NNP'), (u'Service', 'NNP'), (u'AS', 'NNP'), (u',', 'UKN'), (u'som', 'UKN'), (u'eier', 'VBT'), (u'hotellbygget', 'NN'), (u'.', 'UKN'), (u'De', 'PRP'), (u'andre', 'DT'), (u'eierne', 'NNS'), (u'her', 'IN'), (u'er', 'VBT'), (u'Knut', 'NNP'), (u'Solberg', 'NNP'), (u',', 'UKN'), (u'Unni', 'NNP'), (u'og', 'CC'), (u'Finn', 'NNP'), (u'Ove', 'NNP'), (u'Carlsen.', 'NNP'), (u'.', 'UKN')])])}

        self.task.execute(input)

        actual = self.task.getOutput()
        expected = {'data': [
                            u'Hotell Service AS', u'Knut Solberg', u'Carl Otto S\xe6tre', u'Solberg',
                            u'H\xf8nefoss', u'AS', u'Jan Solberg', u'Finn Ove Carlsen.', u'Unni',
                            u'S\xe6tre', u'Bryggeri G\xe5rdene AS']}
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
