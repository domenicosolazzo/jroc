from . import WordnetManager
import unittest
import os


class WordnetManagerTestCase(unittest.TestCase):
    wordnetManager = None

    def setUp(self):
        self.wordnetManager = WordnetManager()

    def tearDown(self):
        self.wordnetManager = None

    def test_initialize_wordnet_returns_synonyms(self):
        """
        Test the synonyms of an english word
        """
        word = 'car'
        expected = {'car':
                        {'lemmas': {
                            'en': [ u'auto', u'automobile', u'cable_car', u'car', u'elevator_car',
                                    u'gondola', u'machine', u'motorcar', u'railcar', u'railroad_car', u'railway_car']}}}
        actual = self.wordnetManager.getSynonyms([word])
        self.assertEqual(expected, actual)

    def test_initialize_wordnet_returns_synonyms_multiple_words(self):
        """
        Test the synonyms of multiple english words
        """
        words = ['car','home','rocket']
        expected = {'car': {
                        'lemmas': {
                                'en': [u'auto', u'automobile', u'cable_car', u'car', u'elevator_car', u'gondola',
                                       u'machine', u'motorcar', u'railcar', u'railroad_car', u'railway_car']}},
                    'rocket': {'lemmas': {
                                'en': [
                                       u'Eruca_sativa', u'Eruca_vesicaria_sativa', u'arugula', u'garden_rocket',
                                       u'projectile', u'rocket', u'rocket_engine', u'rocket_salad', u'roquette',
                                       u'skyrocket']}},
                    'home': {'lemmas': {
                                'en': [u'abode', u'base', u'domicile',
                                       u'dwelling', u'dwelling_house', u'family', u'habitation', u'home', u'home_base',
                                       u'home_plate', u'house', u'household', u'interior', u'internal', u'menage',
                                       u'national', u'nursing_home', u'place', u'plate', u'rest_home']}}}
        actual = self.wordnetManager.getSynonyms(words)

        self.assertEqual(expected, actual)

    def test_initialize_wordnet_returns_synonyms_norsk_multiple_words(self):
        """
        Test the synonyms of multiple norwegian words
        """
        words = ['bil','hjem']
        expected = {'hjem': {
                        'lemmas': {
                            'en': [ u'abode', u'domicile', u'dwelling', u'dwelling_house', u'habitation',
                                u'home', u'housing', u'living_accommodations', u'lodging', u'prison',
                                u'prison_house', u'residence'],
                            'no': [u'bopel', u'bop\xe6l', u'hjem',
                                u'hjemsted', u'hus', u'privatbolig', u'residens', u'stue']}},
                    'bil': {
                        'lemmas': {
                            'en': [u'auto', u'automobile', u'car', u'machine', u'motorcar'],
                            'no': [u'bil', u'karet', u'slede', u'vogn', u'\xf8se']}}}
        actual = self.wordnetManager.getSynonyms(words, language_code="no")

        self.assertEqual(expected, actual)

    def test_initialize_wordnet_returns_synonyms_italian_multiple_words(self):
        """
        Test the synonyms of multiple italian words
        """
        words = ['automobile','casa']
        expected = {'automobile': {
                        'lemmas': {
                                'en': [u'auto', u'automobile', u'car', u'machine', u'motorcar'],
                                'it': [u'auto', u'automobile', u'autovettura', u'macchina', u'vettura']}},
                    'casa': {
                        'lemmas': {
                                'en': [ u'abode', u'business', u'business_concern', u'business_organisation',
                                        u'business_organization', u'concern', u'domicile', u'dwelling',
                                        u'dwelling_house', u'dynasty', u'family', u'habitation',
                                        u'home', u'house', u'household', u'mansion', u'menage', u'planetary_house',
                                        u'sign', u'sign_of_the_zodiac', u'square', u'star_sign'],
                                'it': [u'casa', u'casa_astrologica', u'segno', u'segno_zodiacale']}}}
        actual = self.wordnetManager.getSynonyms(words, language_code="it")

        self.assertEqual(expected, actual)

    def test_initialize_wordnet_returns_synonyms_norsk(self):
        """
        Test the synonyms of a norwegian word
        """
        word = 'bil'
        expected = {'bil': {
                        'lemmas': {
                                'en': [u'auto', u'automobile', u'car', u'machine', u'motorcar'],
                                'no': [u'bil', u'karet', u'slede', u'vogn', u'\xf8se']}}}

        actual = self.wordnetManager.getSynonyms([word],language_code="no")

        self.assertEqual(expected, actual)

    def test_initialize_wordnet_returns_synonyms_italian(self):
        """
        Test the synonyms of an italian word
        """
        word = 'automobile'
        expected = {'automobile':
                        {'lemmas':  {
                                        'en': [u'auto', u'automobile', u'car', u'machine', u'motorcar'],
                                        'it': [u'auto', u'automobile', u'autovettura', u'macchina', u'vettura']}}}

        actual = self.wordnetManager.getSynonyms([word],language_code="it")
        self.assertEqual(expected, actual)

    def test_initialize_wordnet_returns_hyponyms(self):
        """
        Test the hyponyms of an english word
        """
        word = 'car'
        expected = {'car': {
                            'lemmas': {
                                'en': [u'ambulance', u'baggage_car', u'beach_waggon', u'beach_wagon',
                                        u'bus', u'cab', u'cabin_car', u'caboose', u'carriage', u'club_car',
                                        u'coach', u'compact', u'compact_car', u'convertible', u'coupe', u'cruiser',
                                        u'electric', u'electric_automobile', u'electric_car', u'estate_car',
                                        u'freight_car', u'gas_guzzler', u"guard's_van", u'hack', u'handcar',
                                        u'hardtop', u'hatchback', u'heap', u'horseless_carriage', u'hot-rod',
                                        u'hot_rod', u'jalopy', u'jeep', u'landrover', u'limo', u'limousine',
                                        u'loaner', u'lounge_car', u'luggage_van', u'mail_car', u'minicar',
                                        u'minivan', u'Model_T', u'pace_car', u'passenger_car', u'patrol_car',
                                        u'phaeton', u'police_car', u'police_cruiser', u'prowl_car', u'race_car',
                                        u'racer', u'racing_car', u'roadster', u'runabout', u'S.U.V.', u'saloon',
                                        u'secondhand_car', u'sedan', u'slip_carriage', u'slip_coach', u'sport_car',
                                        u'sport_utility', u'sport_utility_vehicle', u'sports_car', u'squad_car',
                                        u'Stanley_Steamer', u'station_waggon', u'station_wagon', u'stock_car',
                                        u'subcompact', u'subcompact_car', u'SUV', u'taxi', u'taxicab', u'tender',
                                        u'tourer', u'touring_car', u'two-seater', u'used-car', u'van',
                                        u'waggon', u'wagon']},
                            'language': 'en'}}
        actual = self.wordnetManager.getHyponyms([word])

        self.assertEqual(expected, actual)

    def test_initialize_wordnet_returns_hyponyms_multiple_words(self):
        """
        Test the hyponyms of some english words
        """
        words = ['car', 'home']
        expected = {'car': {
                        'lemmas': {
                            'en': [ u'ambulance', u'baggage_car', u'beach_waggon', u'beach_wagon', u'bus',
                                    u'cab', u'cabin_car', u'caboose', u'carriage', u'club_car', u'coach',
                                    u'compact', u'compact_car', u'convertible', u'coupe', u'cruiser', u'electric',
                                    u'electric_automobile', u'electric_car', u'estate_car', u'freight_car',
                                    u'gas_guzzler', u"guard's_van", u'hack', u'handcar', u'hardtop', u'hatchback',
                                    u'heap', u'horseless_carriage', u'hot-rod', u'hot_rod', u'jalopy', u'jeep',
                                    u'landrover', u'limo', u'limousine', u'loaner', u'lounge_car', u'luggage_van',
                                    u'mail_car', u'minicar', u'minivan', u'Model_T', u'pace_car', u'passenger_car',
                                    u'patrol_car', u'phaeton', u'police_car', u'police_cruiser', u'prowl_car',
                                    u'race_car', u'racer', u'racing_car', u'roadster', u'runabout', u'S.U.V.',
                                    u'saloon', u'secondhand_car', u'sedan', u'slip_carriage', u'slip_coach',
                                    u'sport_car', u'sport_utility', u'sport_utility_vehicle', u'sports_car',
                                    u'squad_car', u'Stanley_Steamer', u'station_waggon', u'station_wagon',
                                    u'stock_car', u'subcompact', u'subcompact_car', u'SUV', u'taxi', u'taxicab',
                                    u'tender', u'tourer', u'touring_car', u'two-seater', u'used-car', u'van',
                                    u'waggon', u'wagon']},
                        'language': 'en'},
                    'home': {
                        'lemmas': {
                            'en': [ u'broken_home', u'cliff_dwelling', u'condo', u'condominium', u'conjugal_family',
                                    u'extended_family', u'fireside', u'fixer-upper', u'foster_family', u'foster_home',
                                    u'hearth', u'hermitage', u'home_away_from_home', u'home_from_home', u'homestead',
                                    u'house', u'indian_lodge', u'lake_dwelling', u'lodge', u'menage_a_trois', u'messuage',
                                    u'nuclear_family', u'pile_dwelling', u'semi-detached_house', u'vacation_home', u'yurt']},
                        'language': 'en'}}
        actual = self.wordnetManager.getHyponyms(words)
        self.assertEqual(expected, actual)

    def test_initialize_wordnet_returns_hyponyms_norsk(self):
        """
        Test the hyponyms of an norwegian word
        """
        word = 'bil'
        expected = {'bil': {
                            'lemmas': {
                                    'en': [u'ambulance', u'beach_waggon', u'beach_wagon', u'bus', u'cab',
                                        u'compact', u'compact_car', u'convertible', u'coupe', u'cruiser',
                                        u'electric', u'electric_automobile', u'electric_car', u'estate_car',
                                        u'gas_guzzler', u'hack', u'hardtop', u'hatchback', u'heap',
                                        u'horseless_carriage', u'hot-rod', u'hot_rod', u'jalopy', u'jeep',
                                        u'landrover', u'limo', u'limousine', u'loaner', u'minicar', u'minivan',
                                        u'Model_T', u'pace_car', u'patrol_car', u'phaeton', u'police_car',
                                        u'police_cruiser', u'prowl_car', u'race_car', u'racer', u'racing_car',
                                        u'roadster', u'runabout', u'S.U.V.', u'saloon', u'secondhand_car', u'sedan',
                                        u'sport_car', u'sport_utility', u'sport_utility_vehicle', u'sports_car',
                                        u'squad_car', u'Stanley_Steamer', u'station_waggon', u'station_wagon',
                                        u'stock_car', u'subcompact', u'subcompact_car', u'SUV', u'taxi', u'taxicab',
                                        u'tourer', u'touring_car', u'two-seater', u'used-car', u'waggon', u'wagon'],
                                    'no': [u'ambulanse', u'drosje', u'sedan', u'taxi', u'vogn']},
                            'language': 'no'}}
        actual = self.wordnetManager.getHyponyms([word], language_code="no")

        self.assertEqual(expected, actual)

    def test_initialize_wordnet_returns_hyponyms_norsk_multiple_words(self):
        """
        Test the hyponyms of some norwegian words
        """
        words = ['bil', 'hjem']
        expected = {'hjem': {
                        'lemmas': {
                                'en': [ u'abode', u'apartment', u'bastille', u'billet', u'block', u'camp',
                                        u'chokey', u'choky', u'cliff_dwelling', u'condo', u'condominium',
                                        u'domicile', u'dwelling', u'dwelling_house', u'fireside', u'fixer-upper',
                                        u'flat', u'habitation', u'hearth', u'hermitage', u'home', u'homestead',
                                        u'hospice', u'hostel', u'house', u'indian_lodge', u'lake_dwelling',
                                        u'legal_residence', u'living_quarters', u'lodge', u'manufactured_home',
                                        u'messuage', u'mobile_home', u'nick', u'panopticon', u'pied-a-terre',
                                        u'pile_dwelling', u'place', u'quartering', u'quarters', u'rattrap',
                                        u'semi-detached_house', u'shelter', u'state_prison', u'student_lodging',
                                        u'tract_housing', u'vacation_home', u'youth_hostel', u'yurt'],
                                'no': [ u'bopel', u'bop\xe6l', u'eiendom', u'herberge', u'hjem', u'hjemsted',
                                        u'hus', u'leilighet', u'privatbolig', u'residens', u'stue']},
                        'language': 'no'},
                    'bil': {
                        'lemmas': {
                                'en': [ u'ambulance', u'beach_waggon', u'beach_wagon', u'bus', u'cab',
                                        u'compact', u'compact_car', u'convertible', u'coupe', u'cruiser',
                                        u'electric', u'electric_automobile', u'electric_car', u'estate_car',
                                        u'gas_guzzler', u'hack', u'hardtop', u'hatchback', u'heap',
                                        u'horseless_carriage', u'hot-rod', u'hot_rod', u'jalopy', u'jeep',
                                        u'landrover', u'limo', u'limousine', u'loaner', u'minicar', u'minivan',
                                        u'Model_T', u'pace_car', u'patrol_car', u'phaeton', u'police_car',
                                        u'police_cruiser', u'prowl_car', u'race_car', u'racer', u'racing_car',
                                        u'roadster', u'runabout', u'S.U.V.', u'saloon', u'secondhand_car',
                                        u'sedan', u'sport_car', u'sport_utility', u'sport_utility_vehicle',
                                        u'sports_car', u'squad_car', u'Stanley_Steamer', u'station_waggon',
                                        u'station_wagon', u'stock_car', u'subcompact', u'subcompact_car',
                                        u'SUV', u'taxi', u'taxicab', u'tourer', u'touring_car', u'two-seater',
                                        u'used-car', u'waggon', u'wagon'],
                                'no': [u'ambulanse', u'drosje',
                                        u'sedan', u'taxi', u'vogn']},
                        'language': 'no'}}
        actual = self.wordnetManager.getHyponyms(words, language_code="no")
        self.assertEqual(expected, actual)

    def test_initialize_wordnet_returns_hyponyms_italian(self):
        """
        Test the hyponyms of an italian word
        """
        word = 'automobile'
        expected = {'automobile': {
                        'lemmas': {
                            'en': [u'ambulance', u'beach_waggon', u'beach_wagon', u'bus', u'cab',
                                   u'compact', u'compact_car', u'convertible', u'coupe', u'cruiser',
                                   u'electric', u'electric_automobile', u'electric_car', u'estate_car',
                                   u'gas_guzzler', u'hack', u'hardtop', u'hatchback', u'heap',
                                   u'horseless_carriage', u'hot-rod', u'hot_rod', u'jalopy', u'jeep',
                                   u'landrover', u'limo', u'limousine', u'loaner', u'minicar', u'minivan',
                                   u'Model_T', u'pace_car', u'patrol_car', u'phaeton', u'police_car',
                                   u'police_cruiser', u'prowl_car', u'race_car', u'racer', u'racing_car',
                                   u'roadster', u'runabout', u'S.U.V.', u'saloon', u'secondhand_car', u'sedan',
                                   u'sport_car', u'sport_utility', u'sport_utility_vehicle', u'sports_car',
                                   u'squad_car', u'Stanley_Steamer', u'station_waggon', u'station_wagon',
                                   u'stock_car', u'subcompact', u'subcompact_car', u'SUV', u'taxi', u'taxicab',
                                   u'tourer', u'touring_car', u'two-seater', u'used-car', u'waggon', u'wagon'],
                            'it': [u'ambulanza', u'autoambulanza', u'autolettiga', u'automobile_della_polizia',
                                   u'automobile_sportiva', u'autopubblica', u'bagnarola', u'berlina', u'bolide',
                                   u'cabriolet', u'caffettiera', u'campagnola', u'carretta', u'catenaccio',
                                   u'catorcio', u'compatta', u'convertibile', u'coup\xe9', u'decappottabile',
                                   u'fuoristrada', u'giardinetta', u'giardiniera', u'jeep', u'limousine',
                                   u'macchina_a_due_posti', u'macchina_da_corsa', u'macchina_della_polizia',
                                   u'macchina_truccata', u'macinino', u'minivan', u'monovolume', u'pantera',
                                   u'panti\xe8ra', u'spider', u'tass\xec', u'taxi', u'torpedo', u'trabiccolo',
                                   u'vettura_sportiva']},
                        'language': 'it'}}
        actual = self.wordnetManager.getHyponyms([word], language_code="it")

        self.assertEqual(expected, actual)

    def test_initialize_wordnet_returns_hyperyms(self):
        """
        Test the hyperyms of an english word
        """
        word = 'car'
        expected = {'car': {
                            'lemmas': {
                                    'en': [u'automotive_vehicle', u'compartment', u'motor_vehicle', u'wheeled_vehicle']},
                     'language': 'en'}}
        actual = self.wordnetManager.getHypernyms([word])

        self.assertEqual(expected, actual)

    def test_initialize_wordnet_returns_hyperyms_norsk(self):
        """
        Test the hyperyms of a norwegian word
        """
        word = 'bil'
        expected = {'bil': {
                        'lemmas': {
                                'en': [u'automotive_vehicle', u'motor_vehicle'],
                                'no': []},
                        'language': 'no'}}
        actual = self.wordnetManager.getHypernyms([word], language_code="no")

        self.assertEqual(expected, actual)

    def test_initialize_wordnet_returns_hyperyms_italian(self):
        """
        Test the hyperyms of an italian word
        """
        word = 'automobile'
        expected = {'automobile': {
                        'lemmas': {
                                'en': [u'automotive_vehicle', u'motor_vehicle'],
                                'it': [u'motore', u'motoveicolo', u'veicolo_a_motore']},
                        'language': 'it'}}
        actual = self.wordnetManager.getHypernyms([word], language_code="it")

        self.assertEqual(expected, actual)
