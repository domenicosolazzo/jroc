from . import SPARQLAdapter
import unittest
import os

class SPARQLAdapterTestCase(unittest.TestCase):
    sparql = None

    def setUp(self):
        self.sparql = SPARQLAdapter()

    def tearDown(self):
        self.sparql = None

    def test_sparql_get_properties(self):
        """
        Test the retrieval of the sparql endpoint
        """
        input = "Asti"
        actual = self.sparql.getProperties(input, fetchValues=True)
        self.assertTrue('properties' in actual)
        self.assertIsNotNone(actual.get('properties', None))
        self.assertTrue(isinstance(actual.get('properties'), dict))

    def test_sparql_get_thumbnail(self):
        """
        Test getThumbnail for a given entity
        """
        input = "Asti"
        actual = self.sparql.getThumbnail(input)
        self.assertTrue('thumbnail' in actual)
        self.assertIsNotNone(actual.get('thumbnail', None))

    def test_sparql_get_thumbnail(self):
        """
        Test getThumbnail for a given entity
        """
        input = "Asti"
        actual = self.sparql.getThumbnail(input)
        self.assertTrue('thumbnail' in actual)
        self.assertIsNotNone(actual.get('thumbnail', None))

    def test_sparql_get_unique_uri(self):
        """
        Test get unique uri
        """
        input = "Asti"
        actual = self.sparql.getUniqueURI(input)
        self.assertTrue('uri' in actual)

    def test_sparql_get_unique_uri_startwith(self):
        """
        Test get unique uri
        """
        input = "Asti"
        actual = self.sparql.getUniqueURIStartWith(input)
        self.assertTrue('uri' in actual)

    def test_sparql_get_basic_info(self):
        """
        Test get basic info
        """
        input = "Cristiano_Ronaldo"
        actual = self.sparql.getBasicInfo(input)
        self.assertIsNotNone(actual)
        self.assertTrue(isinstance(actual, dict))

    def test_sparql_get_entity_types(self):
        """
        Test get entity types
        """
        input = "Cristiano_Ronaldo"
        actual = self.sparql.getEntityTypes(input)
        self.assertIsNotNone(actual)
        self.assertTrue(isinstance(actual, dict))
        self.assertTrue('type' in actual)
        print(type(actual.get(type)))
        self.assertTrue(isinstance(actual.get('type'), list))
