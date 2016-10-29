# -*- coding: utf-8 -*-
from . import WordnetTask
import unittest
import os

class WordnetTaskTestCase(unittest.TestCase):
    task = None
    name = "Wordnet Task"

    def setUp(self):
        self.task = WordnetTask(name="Wordnet Task")

    def tearDown(self):
        self.task = None

    def test_task_initialization_fails_if_name_is_None(self):
        """
        Test that a Wordnet Task task throws an exception if the name is None
        """
        self.assertRaises(Exception, WordnetTask, None)

    def test_task_initialization_fails_if_name_is_empty(self):
        """
        Test that a Wordnet Task task throws an exception if the name is Empty
        """
        self.assertRaises(Exception, WordnetTask, "")

    def test_task_initialization(self):
        """
        Test that a Wordnet Task task is not None
        """
        self.assertIsNotNone(self.task)

    def test_task_raises_exception_if_data_is_none(self):
        """
        Test that the task will raise an exception if data is None
        """
        input = {"data": None}

        self.task.execute(input)
        self.assertTrue(self.task.hasFailed())

    def test_task_raises_exception_if_data_is_not_a_list(self):
        """
        Test that the task will raise an exception if data is not a list
        """
        input = {"data": 'abc'}

        self.task.execute(input)
        self.assertTrue(self.task.hasFailed())



    def test_task_get_synonyms_hyperyms_hyponyms_english(self):
        """
        Test if the task can fetch synonyms, hyperyms and hyponyms of some english words
        """
        input = {"data":["car", "home"]}

        expected = {'data': {
                        'car': {
                            'synonyms': {
                                'lemmas': {
                                    'en': [ u'auto', u'automobile', u'cable_car', u'car', u'elevator_car',
                                            u'gondola', u'machine', u'motorcar', u'railcar', u'railroad_car',
                                            u'railway_car']}},
                            'hyponyms': {
                                'lemmas': {
                                    'en': [ u'ambulance', u'baggage_car', u'beach_waggon', u'beach_wagon', u'bus', u'cab',
                                            u'cabin_car', u'caboose', u'carriage', u'club_car', u'coach', u'compact',
                                            u'compact_car', u'convertible', u'coupe', u'cruiser', u'electric',
                                            u'electric_automobile', u'electric_car', u'estate_car', u'freight_car',
                                            u'gas_guzzler', u"guard's_van", u'hack', u'handcar', u'hardtop',
                                            u'hatchback', u'heap', u'horseless_carriage', u'hot-rod', u'hot_rod',
                                            u'jalopy', u'jeep', u'landrover', u'limo', u'limousine', u'loaner',
                                            u'lounge_car', u'luggage_van', u'mail_car', u'minicar', u'minivan',
                                            u'Model_T', u'pace_car', u'passenger_car', u'patrol_car', u'phaeton',
                                            u'police_car', u'police_cruiser', u'prowl_car', u'race_car', u'racer',
                                            u'racing_car', u'roadster', u'runabout', u'S.U.V.', u'saloon',
                                            u'secondhand_car', u'sedan', u'slip_carriage', u'slip_coach', u'sport_car',
                                            u'sport_utility', u'sport_utility_vehicle', u'sports_car', u'squad_car',
                                            u'Stanley_Steamer', u'station_waggon', u'station_wagon', u'stock_car',
                                            u'subcompact', u'subcompact_car', u'SUV', u'taxi', u'taxicab', u'tender',
                                            u'tourer', u'touring_car', u'two-seater', u'used-car', u'van', u'waggon',
                                            u'wagon']},
                                'language': 'en'},
                            'hyperyms': {
                                'lemmas': {
                                    'en': [u'automotive_vehicle', u'compartment', u'motor_vehicle', u'wheeled_vehicle']},
                                'language': 'en'}},
                        'home': {
                            'synonyms': {
                                'lemmas': {
                                    'en': [ u'abode', u'base', u'domicile', u'dwelling', u'dwelling_house', u'family',
                                            u'habitation', u'home', u'home_base', u'home_plate', u'house', u'household',
                                            u'interior', u'internal', u'menage', u'national', u'nursing_home', u'place',
                                            u'plate', u'rest_home']}},
                            'hyponyms': {
                                'lemmas': {
                                    'en': [ u'broken_home', u'cliff_dwelling', u'condo', u'condominium', u'conjugal_family', u'extended_family',
                                            u'fireside', u'fixer-upper', u'foster_family', u'foster_home', u'hearth',
                                            u'hermitage', u'home_away_from_home', u'home_from_home', u'homestead',
                                            u'house', u'indian_lodge', u'lake_dwelling', u'lodge', u'menage_a_trois',
                                            u'messuage', u'nuclear_family', u'pile_dwelling', u'semi-detached_house',
                                            u'vacation_home', u'yurt']},
                                    'language': 'en'},
                            'hyperyms': {
                                'lemmas': {
                                    'en': [ u'abode', u'bag', u'base', u'beginning', u'domiciliate', u'environment',
                                            u'house', u'housing', u'institution', u'living_accommodations', u'location',
                                            u'lodging', u'origin', u'put_up', u'residence', u'return', u'root', u'rootage',
                                            u'social_unit', u'source', u'unit']},
                                'language': 'en'}}}}
        actual = self.task.execute(input)

        self.assertEqual(expected, actual)

    def test_task_get_synonyms_hyperyms_hyponyms_norwegian(self):
        """
        Test if the task can fetch synonyms, hyperyms and hyponyms of some norwegian words
        """
        input = {"data":["bil", "hjem"], "language":"no"}

        expected = {'data': {
                        'hjem': {
                            'synonyms': {
                                'lemmas': {
                                    'en': [ u'abode', u'domicile', u'dwelling', u'dwelling_house', u'habitation',
                                            u'home', u'housing', u'living_accommodations', u'lodging', u'prison',
                                            u'prison_house', u'residence'],
                                    'no': [ u'bopel', u'bop\xe6l', u'hjem', u'hjemsted', u'hus', u'privatbolig',
                                            u'residens', u'stue']}},
                            'hyponyms': {
                                'lemmas': {
                                    'en': [ u'abode', u'apartment', u'bastille', u'billet', u'block',
                                            u'camp', u'chokey', u'choky', u'cliff_dwelling', u'condo',
                                            u'condominium', u'domicile', u'dwelling', u'dwelling_house',
                                            u'fireside', u'fixer-upper', u'flat', u'habitation', u'hearth',
                                            u'hermitage', u'home', u'homestead', u'hospice', u'hostel',
                                            u'house', u'indian_lodge', u'lake_dwelling', u'legal_residence',
                                            u'living_quarters', u'lodge', u'manufactured_home', u'messuage',
                                            u'mobile_home', u'nick', u'panopticon', u'pied-a-terre',
                                            u'pile_dwelling', u'place', u'quartering', u'quarters', u'rattrap',
                                            u'semi-detached_house', u'shelter', u'state_prison', u'student_lodging',
                                            u'tract_housing', u'vacation_home', u'youth_hostel', u'yurt'],
                                    'no': [ u'bopel', u'bop\xe6l', u'eiendom', u'herberge', u'hjem', u'hjemsted',
                                            u'hus', u'leilighet', u'privatbolig', u'residens', u'stue']},
                                'language': 'no'},
                            'hyperyms': {
                                'lemmas': {
                                    'en': [ u'address', u'construction', u'correctional_institution',
                                            u'housing', u'living_accommodations', u'lodging', u'structure'],
                                    'no': [ u'adresse', u'bolig', u'bosetning', u'hjem', u'hjemsted', u'hus', u'hytte']},
                                'language': 'no'}},
                        'bil': {
                            'synonyms': {
                                'lemmas': {
                                    'en': [ u'auto', u'automobile', u'car', u'machine', u'motorcar'],
                                    'no': [u'bil', u'karet', u'slede', u'vogn', u'\xf8se']}},
                            'hyponyms': {
                                'lemmas': {
                                    'en': [
                                        u'ambulance', u'beach_waggon', u'beach_wagon', u'bus', u'cab', u'compact',
                                        u'compact_car', u'convertible', u'coupe', u'cruiser', u'electric',
                                        u'electric_automobile', u'electric_car', u'estate_car', u'gas_guzzler',
                                        u'hack', u'hardtop', u'hatchback', u'heap', u'horseless_carriage',
                                        u'hot-rod', u'hot_rod', u'jalopy', u'jeep', u'landrover', u'limo',
                                        u'limousine', u'loaner', u'minicar', u'minivan', u'Model_T', u'pace_car',
                                        u'patrol_car', u'phaeton', u'police_car', u'police_cruiser', u'prowl_car',
                                        u'race_car', u'racer', u'racing_car', u'roadster', u'runabout', u'S.U.V.',
                                        u'saloon', u'secondhand_car', u'sedan', u'sport_car', u'sport_utility',
                                        u'sport_utility_vehicle', u'sports_car', u'squad_car', u'Stanley_Steamer',
                                        u'station_waggon', u'station_wagon', u'stock_car', u'subcompact', u'subcompact_car',
                                        u'SUV', u'taxi', u'taxicab', u'tourer', u'touring_car', u'two-seater', u'used-car',
                                        u'waggon', u'wagon'],
                                    'no': [u'ambulanse', u'drosje', u'sedan', u'taxi', u'vogn']},
                                'language': 'no'},
                            'hyperyms': {
                                'lemmas': {
                                    'en': [u'automotive_vehicle', u'motor_vehicle'],
                                    'no': []},
                                'language': 'no'}}}}
        actual = self.task.execute(input)

        self.assertEqual(expected, actual)

    def test_task_get_synonyms_hyperyms_hyponyms_norwegian_wrong_language_selected(self):
        """
        Test if the task can fetch synonyms, hyperyms and hyponyms of some norwegian words with a wrong language as input.
        """
        input = {"data":["bil", "hjem"], "language":"en"}

        expected = {'data': {
                        'hjem': {'synonyms': {'lemmas': {'en': []}}, 'hyponyms': {'lemmas': {'en': []}, 'language': 'en'}, 'hyperyms': {'lemmas': {'en': []}, 'language': 'en'}},
                        'bil': {'synonyms': {'lemmas': {'en': []}}, 'hyponyms': {'lemmas': {'en': []}, 'language': 'en'}, 'hyperyms': {'lemmas': {'en': []}, 'language': 'en'}}}}
        actual = self.task.execute(input)
        self.assertEqual(expected, actual)
