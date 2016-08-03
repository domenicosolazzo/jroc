# -*- coding: utf-8 -*-
from . import MixDataTask
import unittest
import os

class MixDataTaskTestCase(unittest.TestCase):
    task = None
    name = "MixData Task"

    def setUp(self):
        self.task = MixDataTask(name="MixData task")

    def tearDown(self):
        self.task = None

    def test_task_throws_error(self):
        """
        Test that a MixData Task task throws an exception if the name is None
        """
        self.assertRaises(Exception, MixDataTask, None)

    def test_task_mix_two_lists(self):
        """
        Test that a MixData Task task with two lists
        """
        input = dict([
            ('input1', ['one', 'two', 'three']),
            ('input2',  ['4', '5', '6']),
            ('metadata', dict([
                ('input1', dict([('type', 'list'), ('item-type','string')])),
                ('input2', dict([('type', 'list'), ('item-type','string')]))
            ]))
        ])
        actual = self.task.execute(input)
        actual = actual.get('data', None) if isinstance(actual, dict) else []
        expected = sorted(['one', 'two', 'three', '4', '5', '6'])

        self.assertEqual(sorted(actual), expected)

    def test_task_mix_two_wrong_type(self):
        """
        Test that a MixData Task task with two lists but the wrong type in the metadata
        """
        input = dict([
            ('input1', ['one', 'two', 'three']),
            ('input2',  ['4', '5', '6']),
            ('metadata', dict([
                ('input1', dict([('type', 'notexist'), ('item-type','string')])),
                ('input2', dict([('type', 'notexist'), ('item-type','string')]))
            ]))
        ])
        actual = self.task.execute(input)
        actual = actual.get('data', None) if isinstance(actual, dict) else []
        expected = []

        self.assertEqual(sorted(actual), expected)

    def test_task_mix_list_tuple(self):
        """
        Test that a MixData Task task with one list of string and one list of tuples
        """
        input = dict([
            ('input1', ['one', 'two', 'three']),
            ('input2',  [('mambo', 'italiano'), ('ohoh', 'ihih'), ('me', 'you')]),
            ('metadata', dict([
                ('input1', dict([('type', 'list'), ('item-type','string')])),
                ('input2', dict([('type', 'list'), ('item-type','tuple'), ('index', 0)]))
            ]))
        ])
        actual = self.task.execute(input)
        actual = actual.get('data', None) if isinstance(actual, dict) else []
        expected = sorted(['mambo', 'me', 'ohoh', 'one', 'three', 'two'])

        self.assertEqual(sorted(actual), expected)

    def test_task_mix_list_tuple_not_existing_index(self):
        """
        Test that a MixData Task task with one list of string and one list of tuples with a not existing index.
        The list of tuples is ignored because of a wrong index. It can only be either 0 or 1
        """
        input = dict([
            ('input1', ['one', 'two', 'three']),
            ('input2',  [('mambo', 'italiano'), ('ohoh', 'ihih'), ('me', 'you')]),
            ('metadata', dict([
                ('input1', dict([('type', 'list'), ('item-type','string')])),
                ('input2', dict([('type', 'list'), ('item-type','tuple'), ('index', 2)]))
            ]))
        ])
        actual = self.task.execute(input)
        actual = actual.get('data', None) if isinstance(actual, dict) else []
        expected = sorted(['one', 'three', 'two'])

        self.assertEqual(sorted(actual), expected)

    def test_task_mix_list_dict(self):
        """
        Test that a MixData Task task with one list of string and one list of dictionaries
        """
        input = dict([
            ('input1', ['one', 'two', 'three']),
            ('input2',  [dict([('key1','ciao'), ('key2', 'hello')]), dict([('key1','wonderful'), ('key2', 'life')])]),
            ('metadata', dict([
                ('input1', dict([('type', 'list'), ('item-type','string')])),
                ('input2', dict([('type', 'list'), ('item-type','dict'), ('key', 'key1')]))
            ]))
        ])
        actual = self.task.execute(input)
        actual = actual.get('data', None) if isinstance(actual, dict) else []
        expected = sorted(['ciao', 'one', 'three', 'two', 'wonderful'])

        self.assertEqual(sorted(actual), expected)

    def test_task_mix_list_dict_wrong_key(self):
        """
        Test that a MixData Task task with one list of string and one list of dictionaries but the dictionary key does not exist
        The values inside the dictionary are ignored
        """
        input = dict([
            ('input1', ['one', 'two', 'three']),
            ('input2',  [dict([('key1','ciao'), ('key2', 'hello')]), dict([('key1','wonderful'), ('key2', 'life')])]),
            ('metadata', dict([
                ('input1', dict([('type', 'list'), ('item-type','string')])),
                ('input2', dict([('type', 'list'), ('item-type','dict'), ('key', 'notexist')]))
            ]))
        ])
        actual = self.task.execute(input)
        actual = actual.get('data', None) if isinstance(actual, dict) else []
        expected = sorted(['one', 'three', 'two'])

        self.assertEqual(sorted(actual), expected)
