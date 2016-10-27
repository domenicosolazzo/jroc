from . import EntityDetector
import unittest
import os

class EntityDetectorTestCase(unittest.TestCase):
    entityDetector = None

    def setUp(self):
        self.entityDetector = EntityDetector()

    def tearDown(self):
        self.entityDetector = None

    def test_entitydetector_is_not_None(self):
        """
        Test if the Entity Detector is not None
        """
        self.assertIsNotNone(self.entityDetector)

    def test_entitydetector_result_format(self):
        """
        The the result format of the Entity Detector
        {
            "is_person": True,
            "is_org": False,
            "is_event": False,
            "is_work": False,
            "is_location": False,
            "other": False,
            "type": "Other"
        }
        """
        actual = self.entityDetector.detect([])
        self.assertTrue(isinstance(actual, dict))
        self.assertTrue('is_person' in actual)
        self.assertTrue('is_org' in actual)
        self.assertTrue('is_event' in actual)
        self.assertTrue('is_work' in actual)
        self.assertTrue('is_location' in actual)
        self.assertTrue('other' in actual)
        self.assertTrue('type' in actual)

    def test_entitydetector_is_Person(self):
        """
        Test if it detects a Person type
        """
        expected = True
        types = ["http://xmlns.com/foaf/0.1/Person"]
        actual = self.entityDetector.detect(types)
        self.assertEqual(actual.get('is_person', None), expected)

        types = ["http://schema.org/Person"]
        actual = self.entityDetector.detect(types)
        self.assertEqual(actual.get('is_person', None), expected)

        types = ["http://dbpedia.org/ontology/Person"]
        actual = self.entityDetector.detect(types)
        self.assertEqual(actual.get('is_person', None), expected)

        types = ["http://umbel.org/umbel/rc/Athlete"]
        actual = self.entityDetector.detect(types)
        self.assertEqual(actual.get('is_person', None), expected)

    def test_entitydetector_is_Organization(self):
        """
        Test if it detects an Organization type
        """
        expected = True
        types = ["http://schema.org/Organization"]
        actual = self.entityDetector.detect(types)
        self.assertEqual(actual.get('is_org', None), expected)

        types = ["http://dbpedia.org/ontology/Company"]
        actual = self.entityDetector.detect(types)
        self.assertEqual(actual.get('is_org', None), expected)

        types = ["http://dbpedia.org/ontology/Organisation"]
        actual = self.entityDetector.detect(types)
        self.assertEqual(actual.get('is_org', None), expected)

        types = ["http://umbel.org/umbel/rc/Business"]
        actual = self.entityDetector.detect(types)
        self.assertEqual(actual.get('is_org', None), expected)

    def test_entitydetector_is_Event(self):
        """
        Test if it detects an Event type
        """
        expected = True
        types = ["http://umbel.org/umbel/rc/Event"]
        actual = self.entityDetector.detect(types)
        self.assertEqual(actual.get('is_event', None), expected)

        types = ["http://umbel.org/umbel/rc/Festival"]
        actual = self.entityDetector.detect(types)
        self.assertEqual(actual.get('is_event', None), expected)

        types = ["http://dbpedia.org/class/yago/SocialEvent107288639"]
        actual = self.entityDetector.detect(types)
        self.assertEqual(actual.get('is_event', None), expected)

        types = ["http://dbpedia.org/class/yago/Event100029378"]
        actual = self.entityDetector.detect(types)
        self.assertEqual(actual.get('is_event', None), expected)

    def test_entitydetector_is_Location(self):
        """
        Test if it detects a Location type
        """

        expected = True
        types = ["http://schema.org/Place"]
        actual = self.entityDetector.detect(types)
        self.assertEqual(actual.get('is_location', None), expected)

        types = ["http://schema.org/Country"]
        actual = self.entityDetector.detect(types)
        self.assertEqual(actual.get('is_location', None), expected)

        types = ["http://dbpedia.org/ontology/Country"]
        actual = self.entityDetector.detect(types)
        self.assertEqual(actual.get('is_location', None), expected)

        types = ["http://dbpedia.org/ontology/PopulatedPlace"]
        actual = self.entityDetector.detect(types)
        self.assertEqual(actual.get('is_location', None), expected)

        types = ["http://dbpedia.org/ontology/Settlement"]
        actual = self.entityDetector.detect(types)
        self.assertEqual(actual.get('is_location', None), expected)

        types = ["http://dbpedia.org/ontology/Place"]
        actual = self.entityDetector.detect(types)
        self.assertEqual(actual.get('is_location', None), expected)

        types = ["http://umbel.org/umbel/rc/Village"]
        actual = self.entityDetector.detect(types)
        self.assertEqual(actual.get('is_location', None), expected)

        types = ["http://umbel.org/umbel/rc/PopulatedPlace"]
        actual = self.entityDetector.detect(types)
        self.assertEqual(actual.get('is_location', None), expected)

        types = ["http://umbel.org/umbel/rc/Country"]
        actual = self.entityDetector.detect(types)
        self.assertEqual(actual.get('is_location', None), expected)

        types = ["http://dbpedia.org/ontology/Planet"]
        actual = self.entityDetector.detect(types)
        self.assertEqual(actual.get('is_location', None), expected)
