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

    def test_pos_obtAnalyze(self):
        """
        Check the obt analyze method of OBT

        Expected result
        [
            {
                'is_inf_merke': False,
                'is_sbu': False,
                'word': u'Det',
                'is_verb': False,
                'is_number': {'ordinal': False, 'is_number': False, 'roman': False, 'quantity': False},
                'is_det': True,
                'tagging': [u'det', u'pron', u'n\xf8yt', u'ent', u'pers', u'3'],
                'is_conj': False,
                'is_unknown': False,
                'is_adj': False,
                'is_interj': False,
                'options': u'det pron n\xf8yt ent pers 3',
                'is_subst': False,
                'is_prop': False
            },
            ...
        ]
        """
        result = self.obtManager.obtAnalyze()
        wordNumber = 3
        self.assertTrue(result is not None)
        self.assertTrue(len(result) == wordNumber) # sentence: Det er norsk
        self.assertTrue(isinstance(result, list))

        actualItem = result[0] # Word 'Det'
        self.assertTrue('is_inf_merke' in actualItem)
        self.assertFalse(actualItem.get('is_inf_merke'))

        self.assertTrue('is_sbu' in actualItem)
        self.assertFalse(actualItem.get('is_sbu'))

        self.assertTrue('word' in actualItem)
        self.assertEquals(u'Det', actualItem.get('word'))

        self.assertTrue('is_verb' in actualItem)
        self.assertFalse(actualItem.get('is_verb'))

        self.assertTrue('is_number' in actualItem)
        self.assertTrue(isinstance(actualItem.get('is_number'), dict))
        self.assertTrue('ordinal' in actualItem.get('is_number'))
        self.assertFalse(actualItem.get('is_number').get('ordinal'))
        self.assertTrue('is_number' in actualItem.get('is_number'))
        self.assertFalse(actualItem.get('is_number').get('is_number'))
        self.assertTrue('roman' in actualItem.get('is_number'))
        self.assertFalse(actualItem.get('is_number').get('roman'))
        self.assertTrue('quantity' in actualItem.get('is_number'))
        self.assertFalse(actualItem.get('is_number').get('quantity'))

        self.assertTrue('is_det' in actualItem)
        self.assertTrue(actualItem.get('is_det'))

        self.assertTrue('tagging' in actualItem)
        self.assertTrue(isinstance(actualItem.get('tagging'), list))
        self.assertEquals([u'det', u'pron', u'n\xf8yt', u'ent', u'pers', u'3'], actualItem.get('tagging'))

        self.assertTrue('is_conj' in actualItem)
        self.assertFalse(actualItem.get('is_conj'))

        self.assertTrue('is_unknown' in actualItem)
        self.assertFalse(actualItem.get('is_unknown'))

        self.assertTrue('is_adj' in actualItem)
        self.assertFalse(actualItem.get('is_adj'))

        self.assertTrue('is_interj' in actualItem)
        self.assertFalse(actualItem.get('is_interj'))

        self.assertTrue('options' in actualItem)
        self.assertEquals(u'det pron n\xf8yt ent pers 3', actualItem.get('options'))

        self.assertTrue('is_subst' in actualItem)
        self.assertFalse(actualItem.get('is_subst'))

        self.assertTrue('is_prop' in actualItem)
        self.assertFalse(actualItem.get('is_prop'))

    def test_pos_analyze(self):
        """
        Check the analyze method of OBT
        """
        # Sentence: Det er norsk
        """
        Expected result:
            {
                'interjs': [],
                'inf_merks': [],
                'conjs': [],
                'substs': [],
                'unknowns': [],
                'verbs': [u'er'],
                'numbers': [],
                'props': [],
                'dets': [u'Det'],
                'sbus': [],
                'adj': [u'norsk'],
                'obt': [
                        { 'is_inf_merke': False, 'is_sbu': False, 'word': u'Det', 'is_verb': False, 'is_number': {'ordinal': False, 'is_number': False, 'roman': False, 'quantity': False}, 'is_det': True, 'tagging': [u'det', u'pron', u'n\xf8yt', u'ent', u'pers', u'3'], 'is_conj': False, 'is_unknown': False, 'is_adj': False, 'is_interj': False, 'options': u'det pron n\xf8yt ent pers 3', 'is_subst': False, 'is_prop': False},
                        {'is_inf_merke': False, 'is_sbu': False, 'word': u'er', 'is_verb': True, 'is_number': {'ordinal': False, 'is_number': False, 'roman': False, 'quantity': False}, 'is_det': False, 'tagging': [u'v\xe6re', u'verb', u'pres', u'a5', u'pr1', u'pr2', u'<aux1/perf_part>'], 'is_conj': False, 'is_unknown': False, 'is_adj': False, 'is_interj': False, 'options': u'v\xe6re verb pres a5 pr1 pr2 <aux1/perf_part>', 'is_subst': False, 'is_prop': False},
                        {'is_inf_merke': False, 'is_sbu': False, 'word': u'norsk', 'is_verb': False, 'is_number': {'ordinal': False, 'is_number': False, 'roman': False, 'quantity': False}, 'is_det': False, 'tagging': [u'norsk', u'adj', u'n\xf8yt', u'ub', u'ent', u'pos', u'<<<', u'<<<'], 'is_conj': False, 'is_unknown': False, 'is_adj': True, 'is_interj': False, 'options': u'norsk adj n\xf8yt ub ent pos <<< <<<', 'is_subst': False, 'is_prop': False}
                       ]
            }
        """
        result = self.obtManager.analyze()
        self.assertTrue(result is not None)
        self.assertTrue(isinstance(result, dict))
        self.assertTrue('obt' in result)
        self.assertTrue('VB' in result)
        self.assertTrue('NN' in result)
        self.assertTrue('NNP' in result)
        self.assertTrue('CD' in result)
        self.assertTrue('JJ' in result)
        self.assertTrue('CC' in result)
        self.assertTrue('unknowns' in result)
        self.assertTrue('DT' in result)
        self.assertTrue('inf_merks' in result)
        self.assertTrue('sbus' in result)
        self.assertTrue('interjs' in result)


        self.assertTrue( len(result.get('VB', [])) == 1 )
        self.assertTrue( len(result.get('JJ', [])) == 1 )
        self.assertTrue( len(result.get('DT', [])) == 1 )



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
        textAnalysis = self.obtManager.analyze()
        actual = self.obtManager.findTags(text_analysis=textAnalysis)

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
    def test_pos_article_ivar_aasen_analyze(self):
        """
        Test the analyze result returned for 'ivar_aasen.txt'
        """
        text = self.helper_readFilename('no/ivar_aasen.txt')
        self.obtManager = OBTManager(text.replace("-", " "))
        actual = self.obtManager.analyze()

        self.assertTrue(actual is not None)
        self.assertTrue(isinstance(actual, dict))
        self.assertTrue('obt' in actual)

    def test_pos_article_ivar_aasen_entities(self):
        """
        Test the entities returned for 'ivar_aasen.txt'
        """
        text = self.helper_readFilename('no/ivar_aasen.txt')
        self.obtManager = OBTManager(text.replace("-", " "))
        actual = self.obtManager.findEntities(stopwords=[])
        expectedEntities = [u'Rasmus Aarflots', u'Bibelen', u'\xabIvar\xbb', u'Aasen', u'Aarflot', u'Ivar Aasen', u'Sivert', u'Sunnm\xf8re', u'Ivar Jonsson', u'Ekset', u'\xc5sen', u'Iver Andreas', u'Ivar', u'Hovdebygda']
        expectedEntitiesCount = len(expectedEntities)

        self.assertTrue(actual is not None)
        self.assertTrue(isinstance(actual, list))
        self.assertEquals(expectedEntitiesCount, len(actual))
        self.assertEquals(expectedEntities, actual)


    def test_pos_article_ivar_aasen_entities_with_norwegian_with_stopwords(self):
        """
        Test the entities returned for 'ivar_aasen.txt' after filtering the norwegian stopwords
        """
        text = self.helper_readFilename('no/ivar_aasen.txt')
        self.obtManager = OBTManager(text)
        actual = self.obtManager.findEntities(stopwords=stopwordsNorwegian)

        expectedEntities = [u'Rasmus Aarflots', u'Bibelen', u'\xabIvar\xbb', u'Aasen', u'Aarflot', u'Ivar Aasen', u'Sivert', u'Sunnm\xf8re', u'Ivar Jonsson', u'Ekset', u'\xc5sen', u'Iver Andreas', u'Ivar', u'Hovdebygda']

        expectedEntitiesCount = len(expectedEntities)

        self.assertTrue(actual is not None)
        self.assertTrue(isinstance(actual, list))
        self.assertEquals(expectedEntitiesCount, len(actual))
        self.assertEquals(expectedEntities, actual)

    def test_pos_article_ivar_aasen_tags(self):
        """
        Test the tags returned for 'ivar_aasen.txt'
        """
        text = self.helper_readFilename('no/ivar_aasen.txt')
        self.obtManager = OBTManager(text)

        textAnalysis = self.obtManager.analyze()
        actual = self.obtManager.findTags(text_analysis=textAnalysis)


        expectedTags = [u'Iver', u'Bibelen', u'Andreas', u'Ivar', u'Aasen', u'Aarflot', u'\xabIvar\xbb', u'Sivert', u'Sunnm\xf8re', u'Aarflots', u'Ekset', u'\xc5sen', u'Hovdebygda', u'Rasmus', u'Jonsson']
        expectedTagsCount = len(expectedTags)

        self.assertTrue(actual is not None)
        self.assertTrue(isinstance(actual, list))
        self.assertEquals(expectedTagsCount, len(actual))
        self.assertEquals(expectedTags, actual)

    def test_pos_article_ivar_aasen_tags_with_stopwords(self):
        """
        Test the tags returned for 'ivar_aasen.txt' after filtering the norwegian stopwords
        """
        text = self.helper_readFilename('no/ivar_aasen.txt')
        self.obtManager = OBTManager(text)

        expectedTags = [u'Iver', u'Bibelen', u'Andreas', u'Ivar', u'Aasen', u'Aarflot', u'\xabIvar\xbb', u'Sivert', u'Sunnm\xf8re', u'Aarflots', u'Ekset', u'\xc5sen', u'Hovdebygda', u'Rasmus', u'Jonsson']

        expectedTagsCount = len(expectedTags)

        textAnalysis = self.obtManager.analyze()
        actual = self.obtManager.findTags(text_analysis=textAnalysis)

        actual = [tag for tag in actual if not tag.lower() in stopwordsNorwegian]

        self.assertTrue(actual is not None)
        self.assertTrue(isinstance(actual, list))
        self.assertEquals(expectedTagsCount, len(actual))
        self.assertEquals(expectedTags, actual)


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

        textAnalysis = self.obtManager.analyze()
        actual = self.obtManager.findTags(text_analysis=textAnalysis)

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

        textAnalysis = self.obtManager.analyze()
        actual = self.obtManager.findTags(text_analysis=textAnalysis)

        actual = [tag for tag in actual if not tag.lower() in stopwordsNorwegian]

        self.assertTrue(actual is not None)
        self.assertTrue(isinstance(actual, list))
        self.assertEquals(expectedTagsCount, len(actual))
        self.assertEquals(expectedTags, actual)

    def test_pos_article2_entities(self):
        """
        Test the entities returned for 'article2.txt'
        """
        text = self.helper_readFilename('no/article2.txt')
        self.obtManager = OBTManager(text)
        actual = self.obtManager.findEntities(stopwords=[])

        expectedEntities = [u'Harrys', u'Berkshire', u'Dougie Poynter', u'The Revenant', u'NTB Scanpix', u'Ellie', u'Westminster Abbey', u'Prns Harry', u'The Sun', u'Features-', u'Seogh\xf8r.', u'Di',
                            u'Commonwealth Day Observance Service', u'William', u'Audi Polo Challenge', u'Daily Mail', u'Me Like You', u'Joner', u'EKSEN', u'TONE', u'Ellie Goulding', u'Sunday Times', u'Audis Polo Challenge',
                            u'The Suns', u'Xposure- Jeg', u'Harry', u'Tom Hardy', u'Anything Could', u'Westminister Abbey', u'Features', u'Ellie Goudling', u'Coworth', u'Caprio',
                            u'Leonardo Di', u'Ellies', u'Hardy', u'London', u'Coworth Park', u'Mirror', u'Kate']
        expectedEntitiesCount = len(expectedEntities)

        self.assertTrue(actual is not None)
        self.assertTrue(isinstance(actual, list))
        self.assertEquals(expectedEntitiesCount, len(actual))
        self.assertEquals(expectedEntities, actual)

    def test_pos_article2_entities_with_norwegian_with_stopwords(self):
        """
        Test the entities returned for 'article2.txt' after filtering the norwegian stopwords
        """
        text = self.helper_readFilename('no/article2.txt')
        self.obtManager = OBTManager(text)
        actual = self.obtManager.findEntities(stopwords=stopwordsNorwegian)

        expectedEntities = [u'Like You', u'Harrys', u'Berkshire', u'Dougie Poynter', u'The Revenant', u'Ellie', u'Westminster Abbey', u'Prns Harry', u'The Sun', u'Features-', u'Seogh\xf8r.',
        u'Commonwealth Day Observance Service', u'William', u'Audi Polo Challenge', u'Daily Mail', u'Joner', u'EKSEN', u'TONE', u'Ellie Goulding', u'Sunday Times', u'Audis Polo Challenge',
        u'The Suns', u'Xposure-', u'Harry', u'Tom Hardy', u'Anything Could', u'Leonardo', u'Westminister Abbey', u'Features', u'Ellie Goudling', u'Coworth', u'Caprio', u'NTB Scanpix', u'Ellies',
        u'Hardy', u'London', u'Coworth Park', u'Mirror', u'Kate']

        expectedEntitiesCount = len(expectedEntities)

        self.assertTrue(actual is not None)
        self.assertTrue(isinstance(actual, list))
        self.assertEquals(expectedEntitiesCount, len(actual))
        self.assertEquals(expectedEntities, actual)

    def test_pos_article2_tags(self):
        """
        Test the tags returned for 'article2.txt'
        """
        text = self.helper_readFilename('no/article2.txt')
        self.obtManager = OBTManager(text)

        textAnalysis = self.obtManager.analyze()
        actual = self.obtManager.findTags(text_analysis=textAnalysis)

        expectedTags = [u'Harrys', u'Berkshire', u'Sun', u'Abbey', u'Westminster', u'Ellie', u'Jeg', u'Tom', u'Mail', u'You', u'Poynter', u'Features-', u'Service', u'Di', u'Park',
                        u'William', u'Dougie', u'Goulding', u'Could', u'Me', u'Joner', u'EKSEN', u'TONE', u'Like', u'Anything', u'Audis', u'Revenant', u'Challenge', u'Mirror', u'Daily', u'Times',
                        u'Westminister', u'Goudling', u'Harry', u'Scanpix', u'The', u'Prns', u'Leonardo', u'Xposure-', u'Commonwealth', u'Observance', u'Features', u'Suns', u'Seogh\xf8r.',
                        u'Caprio', u'Sunday', u'Day', u'Ellies', u'Hardy', u'London', u'Coworth', u'Polo', u'NTB', u'Kate', u'Audi']
        expectedTagsCount = len(expectedTags)

        self.assertTrue(actual is not None)
        self.assertTrue(isinstance(actual, list))
        self.assertEquals(expectedTagsCount, len(actual))
        self.assertEquals(expectedTags, actual)

    def test_pos_article2_tags_with_stopwords(self):
        """
        Test the tags returned for 'article2.txt' after filtering the norwegian stopwords
        """
        text = self.helper_readFilename('no/article2.txt')
        self.obtManager = OBTManager(text)

        expectedTags = [u'Harrys', u'Berkshire', u'Sun', u'Abbey', u'Westminster', u'Ellie', u'Tom', u'Mail', u'You', u'Poynter', u'Features-', u'Service', u'Park', u'William',
                        u'Dougie', u'Goulding', u'Could', u'Joner', u'EKSEN', u'TONE', u'Like', u'Anything', u'Audis', u'Revenant', u'Challenge', u'Mirror', u'Daily', u'Times',
                        u'Westminister', u'Goudling', u'Harry', u'Scanpix', u'The', u'Prns', u'Leonardo', u'Xposure-', u'Commonwealth', u'Observance', u'Features', u'Suns', u'Seogh\xf8r.',
                        u'Caprio', u'Sunday', u'Day', u'Ellies', u'Hardy', u'London', u'Coworth', u'Polo', u'NTB', u'Kate', u'Audi']
        expectedTagsCount = len(expectedTags)

        textAnalysis = self.obtManager.analyze()
        actual = self.obtManager.findTags(text_analysis=textAnalysis)

        actual = [tag for tag in actual if not tag.lower() in stopwordsNorwegian]

        self.assertTrue(actual is not None)
        self.assertTrue(isinstance(actual, list))
        self.assertEquals(expectedTagsCount, len(actual))
        self.assertEquals(expectedTags, actual)

    def test_pos_article3_entities(self):
        """
        Test the entities returned for 'article3.txt'
        """
        text = self.helper_readFilename('no/article3.txt')
        self.obtManager = OBTManager(text)
        actual = self.obtManager.findEntities(stopwords=[])

        expectedEntities = [u'Mani Hussaini', u'Nyheter', u'Brussel', u'EFTA', u'Dette', u'Grunnlovens', u'Norge', u'EFTAs', u'Grunnlov', u'ESA', u'EU', u'Arbeiderpartiets', u'Finanstilsynet', u'EUs']
        expectedEntitiesCount = len(expectedEntities)

        self.assertTrue(actual is not None)
        self.assertTrue(isinstance(actual, list))
        self.assertEquals(expectedEntitiesCount, len(actual))
        self.assertEquals(expectedEntities, actual)

    def test_pos_article3_entities_with_norwegian_with_stopwords(self):
        """
        Test the entities returned for 'article3.txt' after filtering the norwegian stopwords
        """
        text = self.helper_readFilename('no/article3.txt')
        self.obtManager = OBTManager(text)
        actual = self.obtManager.findEntities(stopwords=stopwordsNorwegian)

        expectedEntities = [u'Mani Hussaini', u'Nyheter', u'Brussel', u'EFTA', u'Grunnlovens', u'Norge', u'EFTAs', u'Grunnlov', u'ESA', u'EU', u'Arbeiderpartiets', u'Finanstilsynet', u'EUs']

        expectedEntitiesCount = len(expectedEntities)

        self.assertTrue(actual is not None)
        self.assertTrue(isinstance(actual, list))
        self.assertEquals(expectedEntitiesCount, len(actual))
        self.assertEquals(expectedEntities, actual)

    def test_pos_article3_tags(self):
        """
        Test the tags returned for 'article3.txt'
        """
        text = self.helper_readFilename('no/article3.txt')
        self.obtManager = OBTManager(text)

        textAnalysis = self.obtManager.analyze()
        actual = self.obtManager.findTags(text_analysis=textAnalysis)

        expectedTags = [u'Nyheter', u'Brussel', u'EFTA', u'Dette', u'Grunnlovens', u'Norge', u'EFTAs', u'Grunnlov', u'ESA', u'EU', u'Mani', u'Hussaini', u'Finanstilsynet', u'Arbeiderpartiets', u'EUs']
        expectedTagsCount = len(expectedTags)

        self.assertTrue(actual is not None)
        self.assertTrue(isinstance(actual, list))
        self.assertEquals(expectedTagsCount, len(actual))
        self.assertEquals(expectedTags, actual)

    def test_pos_article3_tags_with_stopwords(self):
        """
        Test the tags returned for 'article3.txt' after filtering the norwegian stopwords
        """
        text = self.helper_readFilename('no/article3.txt')
        self.obtManager = OBTManager(text)

        expectedTags = [u'Nyheter', u'Brussel', u'EFTA', u'Grunnlovens', u'Norge', u'EFTAs', u'Grunnlov', u'ESA', u'EU', u'Mani', u'Hussaini', u'Finanstilsynet', u'Arbeiderpartiets', u'EUs']
        expectedTagsCount = len(expectedTags)

        textAnalysis = self.obtManager.analyze()
        actual = self.obtManager.findTags(text_analysis=textAnalysis)

        actual = [tag for tag in actual if not tag.lower() in stopwordsNorwegian]

        self.assertTrue(actual is not None)
        self.assertTrue(isinstance(actual, list))
        self.assertEquals(expectedTagsCount, len(actual))
        self.assertEquals(expectedTags, actual)

    def test_pos_article4_entities(self):
        """
        Test the entities returned for 'article4.txt'
        """
        text = self.helper_readFilename('no/article4.txt')
        self.obtManager = OBTManager(text)
        actual = self.obtManager.findEntities(stopwords=[])
        expectedEntities = [u'Valgdeltagelse', u'Flekkefjord', u'Ordf\xf8rer Jan Sigbj\xf8rnsen', u'L\xd8VLANDValgdeltagelsen']
        expectedEntitiesCount = len(expectedEntities)

        self.assertTrue(actual is not None)
        self.assertTrue(isinstance(actual, list))
        self.assertEquals(expectedEntitiesCount, len(actual))
        self.assertEquals(expectedEntities, actual)

    def test_pos_article4_entities_with_norwegian_with_stopwords(self):
        """
        Test the entities returned for 'article4.txt' after filtering the norwegian stopwords
        """
        text = self.helper_readFilename('no/article4.txt')
        self.obtManager = OBTManager(text)
        actual = self.obtManager.findEntities(stopwords=stopwordsNorwegian)

        expectedEntities = [u'Valgdeltagelse', u'Flekkefjord', u'Ordf\xf8rer Jan Sigbj\xf8rnsen', u'L\xd8VLANDValgdeltagelsen']
        expectedEntitiesCount = len(expectedEntities)

        self.assertTrue(actual is not None)
        self.assertTrue(isinstance(actual, list))
        self.assertEquals(expectedEntitiesCount, len(actual))
        self.assertEquals(expectedEntities, actual)

    def test_pos_article4_tags(self):
        """
        Test the tags returned for 'article4.txt'
        """
        text = self.helper_readFilename('no/article4.txt')
        self.obtManager = OBTManager(text)

        textAnalysis = self.obtManager.analyze()
        actual = self.obtManager.findTags(text_analysis=textAnalysis)

        expectedTags = [u'Ordf\xf8rer', u'L\xd8VLANDValgdeltagelsen', u'Flekkefjord', u'Sigbj\xf8rnsen', u'Jan', u'Valgdeltagelse']
        expectedTagsCount = len(expectedTags)

        self.assertTrue(actual is not None)
        self.assertTrue(isinstance(actual, list))
        self.assertEquals(expectedTagsCount, len(actual))
        self.assertEquals(expectedTags, actual)

    def test_pos_article4_tags_with_stopwords(self):
        """
        Test the tags returned for 'article4.txt' after filtering the norwegian stopwords
        """
        text = self.helper_readFilename('no/article4.txt')
        self.obtManager = OBTManager(text)

        expectedTags = [u'Ordf\xf8rer', u'L\xd8VLANDValgdeltagelsen', u'Flekkefjord', u'Sigbj\xf8rnsen', u'Jan', u'Valgdeltagelse']
        expectedTagsCount = len(expectedTags)

        textAnalysis = self.obtManager.analyze()
        actual = self.obtManager.findTags(text_analysis=textAnalysis)

        actual = [tag for tag in actual if not tag.lower() in stopwordsNorwegian]

        self.assertTrue(actual is not None)
        self.assertTrue(isinstance(actual, list))
        self.assertEquals(expectedTagsCount, len(actual))
        self.assertEquals(expectedTags, actual)


    def test_pos_article5_entities(self):
        """
        Test the entities returned for 'article5.txt'
        """
        text = self.helper_readFilename('no/article5.txt')
        self.obtManager = OBTManager(text)
        actual = self.obtManager.findEntities(stopwords=[])
        expectedEntities = [u'\xc5pningshelgen', u'Rekom', u'Engene', u'The Box', u'Drammen Live24']
        expectedEntitiesCount = len(expectedEntities)

        self.assertTrue(actual is not None)
        self.assertTrue(isinstance(actual, list))
        self.assertEquals(expectedEntitiesCount, len(actual))
        self.assertEquals(expectedEntities, actual)

    def test_pos_article5_entities_with_norwegian_with_stopwords(self):
        """
        Test the entities returned for 'article5.txt' after filtering the norwegian stopwords
        """
        text = self.helper_readFilename('no/article5.txt')
        self.obtManager = OBTManager(text)
        actual = self.obtManager.findEntities(stopwords=stopwordsNorwegian)

        expectedEntities = [u'\xc5pningshelgen', u'Rekom', u'Engene', u'The Box', u'Drammen Live24']
        expectedEntitiesCount = len(expectedEntities)

        self.assertTrue(actual is not None)
        self.assertTrue(isinstance(actual, list))
        self.assertEquals(expectedEntitiesCount, len(actual))
        self.assertEquals(expectedEntities, actual)

    def test_pos_article5_tags(self):
        """
        Test the tags returned for 'article5.txt'
        """
        text = self.helper_readFilename('no/article5.txt')
        self.obtManager = OBTManager(text)

        textAnalysis = self.obtManager.analyze()
        actual = self.obtManager.findTags(text_analysis=textAnalysis)

        expectedTags = [u'Box', u'Live24', u'Drammen', u'\xc5pningshelgen', u'Rekom', u'The', u'Engene']
        expectedTagsCount = len(expectedTags)

        self.assertTrue(actual is not None)
        self.assertTrue(isinstance(actual, list))
        self.assertEquals(expectedTagsCount, len(actual))
        self.assertEquals(expectedTags, actual)

    def test_pos_article5_tags_with_stopwords(self):
        """
        Test the tags returned for 'article5.txt' after filtering the norwegian stopwords
        """
        text = self.helper_readFilename('no/article5.txt')
        self.obtManager = OBTManager(text)

        expectedTags = [u'Box', u'Live24', u'Drammen', u'\xc5pningshelgen', u'Rekom', u'The', u'Engene']
        expectedTagsCount = len(expectedTags)

        textAnalysis = self.obtManager.analyze()
        actual = self.obtManager.findTags(text_analysis=textAnalysis)

        actual = [tag for tag in actual if not tag.lower() in stopwordsNorwegian]

        self.assertTrue(actual is not None)
        self.assertTrue(isinstance(actual, list))
        self.assertEquals(expectedTagsCount, len(actual))
        self.assertEquals(expectedTags, actual)

    def test_pos_article6_entities(self):
        """
        Test the entities returned for 'article6.txt'
        """
        text = self.helper_readFilename('no/article6.txt')
        self.obtManager = OBTManager(text)
        actual = self.obtManager.findEntities(stopwords=[])

        expectedEntities = [u'Nani', u'A', u'Santos', u'Renato Sanchez', u'Tyskland', u'**', u'USA', u'Simao', u'Renato Sanches', u'Pepe', u'Luis Pimenta', u'Slik', u'S. DELEBEKK', u'\xd8sterrike', u'Italia',
        u'Jeg', u'Ekspert-tipset', u'Wembley', u'REUTERS Under', u'Spania', u'Cristiano Ronaldos', u'Cristiano Ronaldo', u'Infantino', u'FINALEEKSTASE', u'Ricardo Carvalho', u'Luiz Felipe Scolari', u'Iran',
        u'Gianni Infantino', u'Nederland', u'VG+', u'Supermannen', u'F', u'Portugals', u'PORTUGAL-EKSPERT', u'Hvilken', u'Luis Figo', u'Bruno Alves', u'Kongsvinger', u'Armenia', u'Island', u'Champions',
        u'Fernando Santos', u'Ghana', u'\xc5\u2022 Norges', u'Brasil', u'S\xf8r-Afrika', u'VG', u'Nord-Korea', u'Fotball-EM', u'Ronaldo', u'EMPS', u'Zlatans', u'Dette', u'VM', u'Norge', u'Cristiano Ronaldo Internasjonal',
        u'Belgia', u'Paulo Bento', u'Ungarn N\xe5', u'AFP Dette', u'Ronaldos', u'Tsjekkia', u'Bulgaria', u'Estland', u'Zin\xe9dine Zidane', u'Albania', u'England', u'Portugal', u'Hva', u'Ricardo Quaresma',
        u'LUIS PIMENTA\u2022 Kongsvingers', u'Jo\xe3o Moutinho', u'Frankrike', u'Hellas', u'For', u'VGs']
        expectedEntitiesCount = len(expectedEntities)

        self.assertTrue(actual is not None)
        self.assertTrue(isinstance(actual, list))
        self.assertEquals(expectedEntitiesCount, len(actual))
        self.assertEquals(expectedEntities, actual)

    def test_pos_article6_entities_with_norwegian_with_stopwords(self):
        """
        Test the entities returned for 'article6.txt' after filtering the norwegian stopwords
        """
        text = self.helper_readFilename('no/article6.txt')
        self.obtManager = OBTManager(text)
        actual = self.obtManager.findEntities(stopwords=stopwordsNorwegian)

        expectedEntities = [u'Nani', u'A', u'Santos', u'Renato Sanchez', u'Tyskland', u'**', u'USA', u'Ungarn', u'Simao', u'Renato Sanches', u'Pepe', u'S. DELEBEKK', u'\xd8sterrike', u'Italia', u'EMPS',
                            u'Ekspert-tipset', u'Wembley', u'REUTERS Under', u'Spania', u'Cristiano Ronaldos', u'Cristiano Ronaldo', u'Infantino', u'FINALEEKSTASE', u'Ricardo Carvalho', u'Iran', u'Gianni Infantino',
                            u'Nederland', u'VG+', u'Ronaldos', u'Supermannen', u'F', u'Portugals', u'PORTUGAL-EKSPERT', u'Luis Figo', u'Bruno Alves', u'Kongsvinger', u'Armenia', u'Island', u'Champions', u'Fernando Santos',
                            u'Ghana', u'\xc5\u2022 Norges', u'Brasil', u'S\xf8r-Afrika', u'VG', u'Nord-Korea', u'Fotball-EM', u'Ronaldo', u'Zlatans', u'VM', u'Luis Pimenta', u'Norge', u'Cristiano Ronaldo Internasjonal',
                            u'Belgia', u'Paulo Bento', u'Luiz Felipe Scolari', u'AFP', u'Tsjekkia', u'Bulgaria', u'Estland', u'Zin\xe9dine Zidane', u'Albania', u'England', u'Portugal', u'Ricardo Quaresma', u'LUIS PIMENTA\u2022 Kongsvingers',
                            u'Jo\xe3o Moutinho', u'Frankrike', u'Hellas', u'VGs']

        expectedEntitiesCount = len(expectedEntities)

        self.assertTrue(actual is not None)
        self.assertTrue(isinstance(actual, list))
        self.assertEquals(expectedEntitiesCount, len(actual))
        self.assertEquals(expectedEntities, actual)

    def test_pos_article6_tags(self):
        """
        Test the tags returned for 'article6.txt'
        """
        text = self.helper_readFilename('no/article6.txt')
        self.obtManager = OBTManager(text)

        textAnalysis = self.obtManager.analyze()
        actual = self.obtManager.findTags(text_analysis=textAnalysis)

        expectedTags = [u'Nani', u'Santos', u'Tyskland', u'Ricardo', u'Under', u'Tsjekkia', u'Infantino', u'FINALEEKSTASE', u'Nederland', u'Luiz', u'Hvilken', u'Luis', u'Island', u'Ronaldo', u'Zlatans', u'Ronaldos',
                        u'Albania', u'England', u'Hellas', u'S.', u'For', u'Simao', u'Paulo', u'\xd8sterrike', u'Italia', u'Ekspert-tipset', u'Wembley', u'Spania', u'VG+', u'Supermannen', u'Armenia', u'Pimenta', u'Kongsvingers', u'Ghana',
                        u'Norge', u'Felipe', u'AFP', u'Bulgaria', u'Sanchez', u'Portugal', u'Sanches', u'Zidane', u'Scolari', u'Carvalho', u'Zin\xe9dine', u'Gianni', u'Jo\xe3o', u'VGs', u'DELEBEKK', u'Alves', u'Pepe', u'Jeg', u'Portugals',
                        u'Iran', u'\xc5\u2022', u'EMPS', u'Champions', u'Brasil', u'S\xf8r-Afrika', u'F', u'Moutinho', u'Belgia', u'Estland', u'USA', u'Ungarn', u'Bento', u'N\xe5', u'PIMENTA\u2022', u'REUTERS', u'Bruno', u'LUIS', u'Renato',
                        u'Cristiano', u'Figo', u'Dette', u'PORTUGAL-EKSPERT', u'Quaresma', u'A', u'VG', u'Nord-Korea', u'Fotball-EM', u'Norges', u'Fernando', u'**', u'Kongsvinger', u'Hva', u'Slik', u'Frankrike', u'Internasjonal']
        expectedTagsCount = len(expectedTags)

        self.assertTrue(actual is not None)
        self.assertTrue(isinstance(actual, list))
        self.assertEquals(expectedTagsCount, len(actual))
        self.assertEquals(expectedTags, actual)

    def test_pos_article6_tags_with_stopwords(self):
        """
        Test the tags returned for 'article6.txt' after filtering the norwegian stopwords
        """
        text = self.helper_readFilename('no/article6.txt')
        self.obtManager = OBTManager(text)

        expectedTags = [u'Nani', u'Santos', u'Tyskland', u'Ricardo', u'Under', u'Tsjekkia', u'Infantino', u'FINALEEKSTASE', u'Nederland', u'Luiz', u'Luis', u'Island', u'Ronaldo', u'Zlatans', u'Ronaldos', u'Albania',
                        u'England', u'Hellas', u'S.', u'Simao', u'Paulo', u'\xd8sterrike', u'Italia', u'Ekspert-tipset', u'Wembley', u'Spania', u'VG+', u'Supermannen', u'Armenia', u'Pimenta', u'Kongsvingers', u'Ghana', u'Norge',
                        u'Felipe', u'AFP', u'Bulgaria', u'Sanchez', u'Portugal', u'Sanches', u'Zidane', u'Scolari', u'Carvalho', u'Zin\xe9dine', u'Gianni', u'Jo\xe3o', u'VGs', u'DELEBEKK', u'Alves', u'Pepe', u'Portugals', u'Iran',
                        u'\xc5\u2022', u'EMPS', u'Champions', u'Brasil', u'S\xf8r-Afrika', u'F', u'Moutinho', u'Belgia', u'Estland', u'USA', u'Ungarn', u'Bento', u'PIMENTA\u2022', u'REUTERS', u'Bruno', u'LUIS', u'Renato', u'Cristiano',
                        u'Figo', u'PORTUGAL-EKSPERT', u'Quaresma', u'A', u'VG', u'Nord-Korea', u'Fotball-EM', u'Norges', u'Fernando', u'**', u'Kongsvinger', u'Frankrike', u'Internasjonal']

        expectedTagsCount = len(expectedTags)

        textAnalysis = self.obtManager.analyze()
        actual = self.obtManager.findTags(text_analysis=textAnalysis)

        actual = [tag for tag in actual if not tag.lower() in stopwordsNorwegian]

        self.assertTrue(actual is not None)
        self.assertTrue(isinstance(actual, list))
        self.assertEquals(expectedTagsCount, len(actual))
        self.assertEquals(expectedTags, actual)

    def test_pos_article7_entities(self):
        """
        Test the entities returned for 'article7.txt'
        """
        text = self.helper_readFilename('no/article7.txt')
        self.obtManager = OBTManager(text)
        actual = self.obtManager.findEntities(stopwords=[])

        expectedEntities = [u'F\xf8reren', u'Rygge.', u'E6', u'Twitter', u'Aftenposten']
        expectedEntitiesCount = len(expectedEntities)

        self.assertTrue(actual is not None)
        self.assertTrue(isinstance(actual, list))
        self.assertEquals(expectedEntitiesCount, len(actual))
        self.assertEquals(expectedEntities, actual)

    def test_pos_article7_entities_with_norwegian_with_stopwords(self):
        """
        Test the entities returned for 'article7.txt' after filtering the norwegian stopwords
        """
        text = self.helper_readFilename('no/article7.txt')
        self.obtManager = OBTManager(text)
        actual = self.obtManager.findEntities(stopwords=stopwordsNorwegian)

        expectedEntities = [u'F\xf8reren', u'Rygge.', u'E6', u'Twitter', u'Aftenposten']

        expectedEntitiesCount = len(expectedEntities)

        self.assertTrue(actual is not None)
        self.assertTrue(isinstance(actual, list))
        self.assertEquals(expectedEntitiesCount, len(actual))
        self.assertEquals(expectedEntities, actual)

    def test_pos_article7_tags(self):
        """
        Test the tags returned for 'article7.txt'
        """
        text = self.helper_readFilename('no/article7.txt')
        self.obtManager = OBTManager(text)

        textAnalysis = self.obtManager.analyze()
        actual = self.obtManager.findTags(text_analysis=textAnalysis)
        expectedTags = [u'F\xf8reren', u'Rygge.', u'E6', u'Twitter', u'Aftenposten']
        expectedTagsCount = len(expectedTags)

        self.assertTrue(actual is not None)
        self.assertTrue(isinstance(actual, list))
        self.assertEquals(expectedTagsCount, len(actual))
        self.assertEquals(expectedTags, actual)

    def test_pos_article7_tags_with_stopwords(self):
        """
        Test the tags returned for 'article7.txt' after filtering the norwegian stopwords
        """
        text = self.helper_readFilename('no/article7.txt')
        self.obtManager = OBTManager(text)

        expectedTags = [u'F\xf8reren', u'Rygge.', u'E6', u'Twitter', u'Aftenposten']

        expectedTagsCount = len(expectedTags)

        textAnalysis = self.obtManager.analyze()
        actual = self.obtManager.findTags(text_analysis=textAnalysis)

        actual = [tag for tag in actual if not tag.lower() in stopwordsNorwegian]

        self.assertTrue(actual is not None)
        self.assertTrue(isinstance(actual, list))
        self.assertEquals(expectedTagsCount, len(actual))
        self.assertEquals(expectedTags, actual)

    def test_pos_article8_entities(self):
        """
        Test the entities returned for 'article8.txt'
        """
        text = self.helper_readFilename('no/article8.txt')
        self.obtManager = OBTManager(text)
        actual = self.obtManager.findEntities(stopwords=[])

        expectedEntities = [u'Menon Economics', u'Helseindustrien', u'Helse', u'Omsorg21-melding', u'NHO', u'Helsen\xe6ringen', u'Norge', u'Vestlandet,-', u'Lesarbrev']
        expectedEntitiesCount = len(expectedEntities)

        self.assertTrue(actual is not None)
        self.assertTrue(isinstance(actual, list))
        self.assertEquals(expectedEntitiesCount, len(actual))
        self.assertEquals(expectedEntities, actual)

    def test_pos_article8_entities_with_norwegian_with_stopwords(self):
        """
        Test the entities returned for 'article8.txt' after filtering the norwegian stopwords
        """
        text = self.helper_readFilename('no/article8.txt')
        self.obtManager = OBTManager(text)
        actual = self.obtManager.findEntities(stopwords=stopwordsNorwegian)

        expectedEntities = [u'Menon Economics', u'Helseindustrien', u'Helse', u'Omsorg21-melding', u'NHO', u'Helsen\xe6ringen', u'Norge', u'Vestlandet,-', u'Lesarbrev']

        expectedEntitiesCount = len(expectedEntities)

        self.assertTrue(actual is not None)
        self.assertTrue(isinstance(actual, list))
        self.assertEquals(expectedEntitiesCount, len(actual))
        self.assertEquals(expectedEntities, actual)

    def test_pos_article8_tags(self):
        """
        Test the tags returned for 'article8.txt'
        """
        text = self.helper_readFilename('no/article8.txt')
        self.obtManager = OBTManager(text)

        textAnalysis = self.obtManager.analyze()
        actual = self.obtManager.findTags(text_analysis=textAnalysis)


        expectedTags = [u'Helseindustrien', u'Helse', u'Omsorg21-melding', u'NHO', u'Economics', u'Menon', u'Helsen\xe6ringen', u'Norge', u'Vestlandet,-', u'Lesarbrev']
        expectedTagsCount = len(expectedTags)

        self.assertTrue(actual is not None)
        self.assertTrue(isinstance(actual, list))
        self.assertEquals(expectedTagsCount, len(actual))
        self.assertEquals(expectedTags, actual)

    def test_pos_article8_tags_with_stopwords(self):
        """
        Test the tags returned for 'article8.txt' after filtering the norwegian stopwords
        """
        text = self.helper_readFilename('no/article8.txt')
        self.obtManager = OBTManager(text)

        expectedTags = [u'Helseindustrien', u'Helse', u'Omsorg21-melding', u'NHO', u'Economics', u'Menon', u'Helsen\xe6ringen', u'Norge', u'Vestlandet,-', u'Lesarbrev']

        expectedTagsCount = len(expectedTags)

        textAnalysis = self.obtManager.analyze()
        actual = self.obtManager.findTags(text_analysis=textAnalysis)

        actual = [tag for tag in actual if not tag.lower() in stopwordsNorwegian]

        self.assertTrue(actual is not None)
        self.assertTrue(isinstance(actual, list))
        self.assertEquals(expectedTagsCount, len(actual))
        self.assertEquals(expectedTags, actual)

    def test_pos_article9_entities(self):
        """
        Test the entities returned for 'article9.txt'
        """
        text = self.helper_readFilename('no/article9.txt')
        self.obtManager = OBTManager(text)
        actual = self.obtManager.findEntities(stopwords=[])

        expectedEntities = [u'Sveits', u'Romania', u'Granit Xhaka', u'Han', u'Borussia M\xf6nchengladbach', u'Vi', u'23-\xe5ringen', u'Ramseys', u'Arsenal', u'Ars\xe8ne Wenger.', u'M\xf6nchengladbach', u'Kasper Wikestad', u'Xhaka', u'Bundesliga', u'Xhakas']
        expectedEntitiesCount = len(expectedEntities)

        self.assertTrue(actual is not None)
        self.assertTrue(isinstance(actual, list))
        self.assertEquals(expectedEntitiesCount, len(actual))
        self.assertEquals(expectedEntities, actual)

    def test_pos_article9_entities_with_norwegian_with_stopwords(self):
        """
        Test the entities returned for 'article9.txt' after filtering the norwegian stopwords
        """
        text = self.helper_readFilename('no/article9.txt')
        self.obtManager = OBTManager(text)
        actual = self.obtManager.findEntities(stopwords=stopwordsNorwegian)

        expectedEntities = [u'Sveits', u'Romania', u'Granit Xhaka', u'Borussia M\xf6nchengladbach', u'23-\xe5ringen', u'Ramseys', u'Arsenal', u'Ars\xe8ne Wenger.', u'M\xf6nchengladbach', u'Kasper Wikestad', u'Xhaka', u'Bundesliga', u'Xhakas']

        expectedEntitiesCount = len(expectedEntities)

        self.assertTrue(actual is not None)
        self.assertTrue(isinstance(actual, list))
        self.assertEquals(expectedEntitiesCount, len(actual))
        self.assertEquals(expectedEntities, actual)

    def test_pos_article9_tags(self):
        """
        Test the tags returned for 'article9.txt'
        """
        text = self.helper_readFilename('no/article9.txt')
        self.obtManager = OBTManager(text)

        textAnalysis = self.obtManager.analyze()
        actual = self.obtManager.findTags(text_analysis=textAnalysis)

        expectedTags = [u'Sveits', u'Ars\xe8ne', u'Romania', u'Han', u'Bundesliga', u'Borussia', u'Ramseys', u'Arsenal', u'Kasper', u'Granit', u'Xhakas', u'Wikestad', u'Vi', u'Xhaka',
                        u'23-\xe5ringen', u'M\xf6nchengladbach', u'Wenger.']
        expectedTagsCount = len(expectedTags)

        self.assertTrue(actual is not None)
        self.assertTrue(isinstance(actual, list))
        self.assertEquals(expectedTagsCount, len(actual))
        self.assertEquals(expectedTags, actual)

    def test_pos_article9_tags_with_stopwords(self):
        """
        Test the tags returned for 'article9.txt' after filtering the norwegian stopwords
        """
        text = self.helper_readFilename('no/article9.txt')
        self.obtManager = OBTManager(text)

        expectedTags = [u'Sveits', u'Ars\xe8ne', u'Romania', u'Bundesliga', u'Borussia', u'Ramseys', u'Arsenal', u'Kasper', u'Granit', u'Xhakas', u'Wikestad', u'Xhaka', u'23-\xe5ringen', u'M\xf6nchengladbach', u'Wenger.']

        expectedTagsCount = len(expectedTags)

        textAnalysis = self.obtManager.analyze()
        actual = self.obtManager.findTags(text_analysis=textAnalysis)

        actual = [tag for tag in actual if not tag.lower() in stopwordsNorwegian]

        self.assertTrue(actual is not None)
        self.assertTrue(isinstance(actual, list))
        self.assertEquals(expectedTagsCount, len(actual))
        self.assertEquals(expectedTags, actual)

    def test_pos_article10_entities(self):
        """
        Test the entities returned for 'article10.txt'
        """
        text = self.helper_readFilename('no/article10.txt')
        self.obtManager = OBTManager(text)
        actual = self.obtManager.findEntities(stopwords=[])

        expectedEntities = [u'NRK', u'Bredli', u'VG', u'Oslo', u'Det', u'Mirmotahari', u'Hege Bj\xf8lseth', u'Pharos', u'Grete Lien Metlid', u'Politioverbetjent Stein Olav Bredli', u'VGs']
        expectedEntitiesCount = len(expectedEntities)

        self.assertTrue(actual is not None)
        self.assertTrue(isinstance(actual, list))
        self.assertEquals(expectedEntitiesCount, len(actual))
        self.assertEquals(expectedEntities, actual)

    def test_pos_article10_entities_with_norwegian_with_stopwords(self):
        """
        Test the entities returned for 'article10.txt' after filtering the norwegian stopwords
        """
        text = self.helper_readFilename('no/article10.txt')
        self.obtManager = OBTManager(text)
        actual = self.obtManager.findEntities(stopwords=stopwordsNorwegian)

        expectedEntities = [u'NRK', u'VG', u'Oslo', u'Bredli', u'Mirmotahari', u'Hege Bj\xf8lseth', u'Pharos', u'Grete Lien Metlid', u'Politioverbetjent Stein Olav Bredli', u'VGs']

        expectedEntitiesCount = len(expectedEntities)

        self.assertTrue(actual is not None)
        self.assertTrue(isinstance(actual, list))
        self.assertEquals(expectedEntitiesCount, len(actual))
        self.assertEquals(expectedEntities, actual)

    def test_pos_article10_tags(self):
        """
        Test the tags returned for 'article9.txt'
        """
        text = self.helper_readFilename('no/article10.txt')
        self.obtManager = OBTManager(text)

        textAnalysis = self.obtManager.analyze()
        actual = self.obtManager.findTags(text_analysis=textAnalysis)


        expectedTags = [u'NRK', u'Politioverbetjent', u'Stein', u'VG', u'Det', u'Oslo', u'Bredli', u'Mirmotahari', u'Hege', u'Olav', u'Pharos', u'Metlid', u'Bj\xf8lseth', u'Lien', u'VGs', u'Grete']
        expectedTagsCount = len(expectedTags)

        self.assertTrue(actual is not None)
        self.assertTrue(isinstance(actual, list))
        self.assertEquals(expectedTagsCount, len(actual))
        self.assertEquals(expectedTags, actual)

    def test_pos_article10_tags_with_stopwords(self):
        """
        Test the tags returned for 'article10.txt' after filtering the norwegian stopwords
        """
        text = self.helper_readFilename('no/article10.txt')
        self.obtManager = OBTManager(text)

        expectedTags = [u'NRK', u'Politioverbetjent', u'Stein', u'VG', u'Oslo', u'Bredli', u'Mirmotahari', u'Hege', u'Olav', u'Pharos', u'Metlid', u'Bj\xf8lseth', u'Lien', u'VGs', u'Grete']

        expectedTagsCount = len(expectedTags)

        textAnalysis = self.obtManager.analyze()
        actual = self.obtManager.findTags(text_analysis=textAnalysis)

        actual = [tag for tag in actual if not tag.lower() in stopwordsNorwegian]

        self.assertTrue(actual is not None)
        self.assertTrue(isinstance(actual, list))
        self.assertEquals(expectedTagsCount, len(actual))
        self.assertEquals(expectedTags, actual)

    def test_pos_article11_entities(self):
        """
        Test the entities returned for 'article11.txt'
        """
        text = self.helper_readFilename('no/article11.txt')
        self.obtManager = OBTManager(text)
        actual = self.obtManager.findEntities(stopwords=[])

        expectedEntities = [u'Hotell Service AS', u'Knut Solberg', u'Carl Otto S\xe6tre', u'Solberg', u'H\xf8nefoss', u'AS', u'Jan Solberg', u'Finn Ove Carlsen.', u'Unni', u'S\xe6tre', u'Bryggeri G\xe5rdene AS']
        expectedEntitiesCount = len(expectedEntities)

        self.assertTrue(actual is not None)
        self.assertTrue(isinstance(actual, list))
        self.assertEquals(expectedEntitiesCount, len(actual))
        self.assertEquals(expectedEntities, actual)

    def test_pos_article11_entities_with_norwegian_with_stopwords(self):
        """
        Test the entities returned for 'article11.txt' after filtering the norwegian stopwords
        """
        text = self.helper_readFilename('no/article11.txt')
        self.obtManager = OBTManager(text)
        actual = self.obtManager.findEntities(stopwords=stopwordsNorwegian)

        expectedEntities = [u'Hotell Service AS', u'Knut Solberg', u'Carl Otto S\xe6tre', u'Solberg', u'H\xf8nefoss', u'AS', u'Jan Solberg', u'Finn Ove Carlsen.', u'Unni', u'S\xe6tre', u'Bryggeri G\xe5rdene AS']
        expectedEntitiesCount = len(expectedEntities)

        self.assertTrue(actual is not None)
        self.assertTrue(isinstance(actual, list))
        self.assertEquals(expectedEntitiesCount, len(actual))
        self.assertEquals(expectedEntities, actual)

    def test_pos_article11_tags(self):
        """
        Test the tags returned for 'article11.txt'
        """
        text = self.helper_readFilename('no/article11.txt')
        self.obtManager = OBTManager(text)

        textAnalysis = self.obtManager.analyze()
        actual = self.obtManager.findTags(text_analysis=textAnalysis)


        expectedTags = [u'Hotell', u'H\xf8nefoss', u'S\xe6tre', u'Carl', u'Service', u'Carlsen.', u'Finn', u'Bryggeri', u'Jan', u'Ove', u'Otto', u'G\xe5rdene', u'Knut', u'Unni', u'Solberg']
        expectedTagsCount = len(expectedTags)

        self.assertTrue(actual is not None)
        self.assertTrue(isinstance(actual, list))
        self.assertEquals(expectedTagsCount, len(actual))
        self.assertEquals(expectedTags, actual)

    def test_pos_article11_tags_with_stopwords(self):
        """
        Test the tags returned for 'article11.txt' after filtering the norwegian stopwords
        """
        text = self.helper_readFilename('no/article11.txt')
        self.obtManager = OBTManager(text)

        expectedTags = [u'Hotell', u'H\xf8nefoss', u'S\xe6tre', u'Carl', u'Service', u'Carlsen.', u'Finn', u'Bryggeri', u'Jan', u'Ove', u'Otto', u'G\xe5rdene', u'Knut', u'Unni', u'Solberg']
        expectedTagsCount = len(expectedTags)

        textAnalysis = self.obtManager.analyze()
        actual = self.obtManager.findTags(text_analysis=textAnalysis)

        actual = [tag for tag in actual if not tag.lower() in stopwordsNorwegian]

        self.assertTrue(actual is not None)
        self.assertTrue(isinstance(actual, list))
        self.assertEquals(expectedTagsCount, len(actual))
        self.assertEquals(expectedTags, actual)

    def test_pos_article12_entities(self):
        """
        Test the entities returned for 'article12.txt'
        """
        text = self.helper_readFilename('no/article12.txt')
        self.obtManager = OBTManager(text)
        actual = self.obtManager.findEntities(stopwords=[])
        expectedEntities = [u'600,-8', u'400,-10', u'200,-9', u'500,-5', u'Statistisk', u'200,-3', u'900,-6', u'900,-2', u'700,-4', u'Frifagbevegelse.', u'700,-7']
        expectedEntitiesCount = len(expectedEntities)

        self.assertTrue(actual is not None)
        self.assertTrue(isinstance(actual, list))
        self.assertEquals(expectedEntitiesCount, len(actual))
        self.assertEquals(expectedEntities, actual)

    def test_pos_article12_entities_with_norwegian_with_stopwords(self):
        """
        Test the entities returned for 'article12.txt' after filtering the norwegian stopwords
        """
        text = self.helper_readFilename('no/article12.txt')
        self.obtManager = OBTManager(text)
        actual = self.obtManager.findEntities(stopwords=stopwordsNorwegian)

        expectedEntities = [u'600,-8', u'400,-10', u'200,-9', u'500,-5', u'Statistisk', u'200,-3', u'900,-6', u'900,-2', u'700,-4', u'Frifagbevegelse.', u'700,-7']

        expectedEntitiesCount = len(expectedEntities)

        self.assertTrue(actual is not None)
        self.assertTrue(isinstance(actual, list))
        self.assertEquals(expectedEntitiesCount, len(actual))
        self.assertEquals(expectedEntities, actual)

    def test_pos_article12_tags(self):
        """
        Test the tags returned for 'article12.txt'
        """
        text = self.helper_readFilename('no/article12.txt')
        self.obtManager = OBTManager(text)

        textAnalysis = self.obtManager.analyze()
        actual = self.obtManager.findTags(text_analysis=textAnalysis)

        expectedTags = [u'600,-8', u'400,-10', u'200,-9', u'500,-5', u'Statistisk', u'200,-3', u'900,-6', u'900,-2', u'700,-4', u'Frifagbevegelse.', u'700,-7']
        expectedTagsCount = len(expectedTags)

        self.assertTrue(actual is not None)
        self.assertTrue(isinstance(actual, list))
        self.assertEquals(expectedTagsCount, len(actual))
        self.assertEquals(expectedTags, actual)

    def test_pos_article12_tags_with_stopwords(self):
        """
        Test the tags returned for 'article12.txt' after filtering the norwegian stopwords
        """
        text = self.helper_readFilename('no/article12.txt')
        self.obtManager = OBTManager(text)

        expectedTags = [u'600,-8', u'400,-10', u'200,-9', u'500,-5', u'Statistisk', u'200,-3', u'900,-6', u'900,-2', u'700,-4', u'Frifagbevegelse.', u'700,-7']

        expectedTagsCount = len(expectedTags)

        textAnalysis = self.obtManager.analyze()
        actual = self.obtManager.findTags(text_analysis=textAnalysis)

        actual = [tag for tag in actual if not tag.lower() in stopwordsNorwegian]

        self.assertTrue(actual is not None)
        self.assertTrue(isinstance(actual, list))
        self.assertEquals(expectedTagsCount, len(actual))
        self.assertEquals(expectedTags, actual)

    def test_pos_article14_entities(self):
        """
        Test the entities returned for 'article14.txt'
        """
        text = self.helper_readFilename('no/article14.txt')
        self.obtManager = OBTManager(text)
        actual = sorted(self.obtManager.findEntities(stopwords=[]))
        expectedEntities = sorted([u'Magnor Glassverk', u'Selvbl\xe5s', u'"Turistfelle"',
                                    u'\xabNumber 1 Christmas Attraction on TripAdvisor"', u'Yelp', u'L\xf8iten Lys AS',
                                    u'Oslo', u'Hadeland', u'Taxfree', u'Hadeland Glassverk'])

        expectedEntitiesCount = len(expectedEntities)

        self.assertTrue(actual is not None)
        self.assertTrue(isinstance(actual, list))
        self.assertEquals(expectedEntitiesCount, len(actual))
        self.assertEquals(expectedEntities, actual)

    def test_pos_article14_entities_with_norwegian_with_stopwords(self):
        """
        Test the entities returned for 'article14.txt' after filtering the norwegian stopwords
        """
        text = self.helper_readFilename('no/article14.txt')
        self.obtManager = OBTManager(text)
        actual = sorted(self.obtManager.findEntities(stopwords=stopwordsNorwegian))

        expectedEntities = sorted([u'Magnor Glassverk', u'Selvbl\xe5s',
                                    u'"Turistfelle"', u'\xabNumber 1 Christmas Attraction on TripAdvisor"',
                                    u'Yelp', u'L\xf8iten Lys AS', u'Oslo', u'Hadeland',
                                    u'Taxfree', u'Hadeland Glassverk'])
        expectedEntitiesCount = len(expectedEntities)

        self.assertTrue(actual is not None)
        self.assertTrue(isinstance(actual, list))
        self.assertEquals(expectedEntitiesCount, len(actual))
        self.assertEquals(expectedEntities, actual)

    def test_pos_article14_tags(self):
        """
        Test the tags returned for 'article14.txt'
        """
        text = self.helper_readFilename('no/article14.txt')
        self.obtManager = OBTManager(text)

        textAnalysis = self.obtManager.analyze()
        actual = sorted(self.obtManager.findTags(text_analysis=textAnalysis))

        expectedTags = sorted([u'Magnor', u'Selvbl\xe5s', u'"Turistfelle"',
                                u'\xabNumber 1 Christmas Attraction on TripAdvisor"',
                                u'Yelp', u'Lys', u'Oslo', u'Glassverk', u'L\xf8iten',
                                u'Hadeland', u'Taxfree'])

        expectedTagsCount = len(expectedTags)

        self.assertTrue(actual is not None)
        self.assertTrue(isinstance(actual, list))
        self.assertEquals(expectedTagsCount, len(actual))
        self.assertEquals(expectedTags, actual)

    def test_pos_article14_tags_with_stopwords(self):
        """
        Test the tags returned for 'article14.txt' after filtering the norwegian stopwords
        """
        text = self.helper_readFilename('no/article14.txt')
        self.obtManager = OBTManager(text)

        expectedTags = sorted([u'Magnor', u'Selvbl\xe5s', u'"Turistfelle"',
                        u'\xabNumber 1 Christmas Attraction on TripAdvisor"', u'Yelp', u'Lys', u'Oslo', u'Glassverk',
                        u'L\xf8iten', u'Hadeland', u'Taxfree'])
        expectedTagsCount = len(expectedTags)

        textAnalysis = self.obtManager.analyze()
        actual = self.obtManager.findTags(text_analysis=textAnalysis)

        actual = sorted([tag for tag in actual if not tag.lower() in stopwordsNorwegian])

        self.assertTrue(actual is not None)
        self.assertTrue(isinstance(actual, list))
        self.assertEquals(expectedTagsCount, len(actual))
        self.assertEquals(expectedTags, actual)


    ##### Ny norsk #####
    def test_pos_article1_nn_entities(self):
        """
        Test the entities returned for 'article1.txt' (Ny Norsk)
        """
        text = self.helper_readFilename('nn/article1.txt')
        self.obtManager = OBTManager(text)
        actual = self.obtManager.findEntities(stopwords=[])
        expectedEntities = [u'No', u'Stormskyene']
        expectedEntitiesCount = len(expectedEntities)

        self.assertTrue(actual is not None)
        self.assertTrue(isinstance(actual, list))
        self.assertEquals(expectedEntitiesCount, len(actual))
        self.assertEquals(expectedEntities, actual)

    def test_pos_article1_nn_entities_with_norwegian_with_stopwords(self):
        """
        Test the entities returned for 'article1.txt' (Ny Norsk) after filtering the norwegian stopwords
        """
        text = self.helper_readFilename('nn/article1.txt')
        self.obtManager = OBTManager(text)
        actual = self.obtManager.findEntities(stopwords=stopwordsNorwegian)

        expectedEntities = [u'Stormskyene']

        expectedEntitiesCount = len(expectedEntities)

        self.assertTrue(actual is not None)
        self.assertTrue(isinstance(actual, list))
        self.assertEquals(expectedEntitiesCount, len(actual))
        self.assertEquals(expectedEntities, actual)

    def test_pos_article1_nn_tags(self):
        """
        Test the tags returned for 'article1.txt' (Ny Norsk)
        """
        text = self.helper_readFilename('nn/article1.txt')
        self.obtManager = OBTManager(text)

        textAnalysis = self.obtManager.analyze()
        actual = self.obtManager.findTags(text_analysis=textAnalysis)

        expectedTags = [u'No', u'Stormskyene']
        expectedTagsCount = len(expectedTags)

        self.assertTrue(actual is not None)
        self.assertTrue(isinstance(actual, list))
        self.assertEquals(expectedTagsCount, len(actual))
        self.assertEquals(expectedTags, actual)

    def test_pos_article1_nn_tags_with_stopwords(self):
        """
        Test the tags returned for 'article1.txt' (Ny Norsk) after filtering the norwegian stopwords
        """
        text = self.helper_readFilename('nn/article1.txt')
        self.obtManager = OBTManager(text)

        expectedTags = [u'Stormskyene']
        expectedTagsCount = len(expectedTags)

        textAnalysis = self.obtManager.analyze()
        actual = self.obtManager.findTags(text_analysis=textAnalysis)

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
