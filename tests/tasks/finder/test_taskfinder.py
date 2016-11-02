# -*- coding: utf-8 -*-
from . import TaskFinder
import unittest
import os

class TaskFinderTestCase(unittest.TestCase):
    taskFinder = None
    name = "Task Finder Test Task"

    def setUp(self):
        self.taskFinder = TaskFinder()

    def tearDown(self):
        self.taskFinder = None

    def test_taskfinder_availabletasks_is_not_none(self):
        """
        Check the available tasks in the task finder
        """
        available_tasks = self.taskFinder.getAvailableTasks()

        self.assertIsNotNone(available_tasks)

    def test_taskfinder_availabletasks_has_basic_task(self):
        """
        Check if it contains a BASIC task
        """
        available_tasks = self.taskFinder.getAvailableTasks()

        taskName = 'BASIC'
        task = available_tasks.get(taskName, None)
        self.assertIsNotNone(taskName)

    def test_taskfinder_availabletasks_has_datacleaner_task(self):
        """
        Check if it contains a DATA_CLEANER task
        """
        available_tasks = self.taskFinder.getAvailableTasks()

        taskName = 'DATA_CLEANER'
        task = available_tasks.get(taskName, None)
        self.assertIsNotNone(taskName)

    def test_taskfinder_availabletasks_has_languagedetector_task(self):
        """
        Check if it contains a LANGUAGE_DETECTOR task
        """
        available_tasks = self.taskFinder.getAvailableTasks()

        taskName = 'LANGUAGE_DETECTOR'
        task = available_tasks.get(taskName, None)
        self.assertIsNotNone(taskName)

    def test_taskfinder_availabletasks_has_loader_task(self):
        """
        Check if it contains a LOADER task
        """
        available_tasks = self.taskFinder.getAvailableTasks()

        taskName = 'LOADER'
        task = available_tasks.get(taskName, None)
        self.assertIsNotNone(taskName)

    def test_taskfinder_availabletasks_has__ner_nltk_tagging_task(self):
        """
        Check if it contains a NER_NLTK_TAGGING task
        """
        available_tasks = self.taskFinder.getAvailableTasks()

        taskName = 'NER_NLTK_TAGGING'
        task = available_tasks.get(taskName, None)
        self.assertIsNotNone(taskName)

    def test_taskfinder_availabletasks_has__ner_regex_tagging_task(self):
        """
        Check if it contains a NER_REGEX_TAGGING task
        """
        available_tasks = self.taskFinder.getAvailableTasks()

        taskName = 'NER_REGEX_TAGGING'
        task = available_tasks.get(taskName, None)
        self.assertIsNotNone(taskName)

    def test_taskfinder_availabletasks_has__ner_regex_tagging_mixing_task(self):
        """
        Check if it contains a NER_REGEX_TAGGING_MIXING task
        """
        available_tasks = self.taskFinder.getAvailableTasks()

        taskName = 'NER_REGEX_TAGGING_MIXING'
        task = available_tasks.get(taskName, None)
        self.assertIsNotNone(taskName)

    def test_taskfinder_availabletasks_has__ner_stanford_tagging_task(self):
        """
        Check if it contains a NER_STANFORD_TAGGING task
        """
        available_tasks = self.taskFinder.getAvailableTasks()

        taskName = 'NER_STANFORD_TAGGING'
        task = available_tasks.get(taskName, None)
        self.assertIsNotNone(taskName)

    def test_taskfinder_availabletasks_has__ner_pos_tagging_task(self):
        """
        Check if it contains a NER_POS_TAGGING task
        """
        available_tasks = self.taskFinder.getAvailableTasks()

        taskName = 'NER_POS_TAGGING'
        task = available_tasks.get(taskName, None)
        self.assertIsNotNone(taskName)

    def test_taskfinder_availabletasks_has__mixdata_task(self):
        """
        Check if it contains a MIXDATA task
        """
        available_tasks = self.taskFinder.getAvailableTasks()

        taskName = 'MIXDATA'
        task = available_tasks.get(taskName, None)
        self.assertIsNotNone(taskName)

    def test_taskfinder_availabletasks_has__pos_tagging_task(self):
        """
        Check if it contains a POS_TAGGING task
        """
        available_tasks = self.taskFinder.getAvailableTasks()

        taskName = 'POS_TAGGING'
        task = available_tasks.get(taskName, None)
        self.assertIsNotNone(taskName)

    def test_taskfinder_availabletasks_has__pos_tagging_tags_task(self):
        """
        Check if it contains a POS_TAGGING_TAGS task
        """
        available_tasks = self.taskFinder.getAvailableTasks()

        taskName = 'POS_TAGGING_TAGS'
        task = available_tasks.get(taskName, None)
        self.assertIsNotNone(taskName)


    def test_taskfinder_availabletasks_has__sparql_annotation_task(self):
        """
        Check if it contains a SPARQL_ANNOTATION task
        """
        available_tasks = self.taskFinder.getAvailableTasks()

        taskName = 'SPARQL_ANNOTATION'
        task = available_tasks.get(taskName, None)
        self.assertIsNotNone(taskName)

    def test_taskfinder_availabletasks_has__sparql_annotation_uri_task(self):
        """
        Check if it contains a SPARQL_ANNOTATION_URI task
        """
        available_tasks = self.taskFinder.getAvailableTasks()

        taskName = 'SPARQL_ANNOTATION_URI'
        task = available_tasks.get(taskName, None)
        self.assertIsNotNone(taskName)

    def test_taskfinder_availabletasks_has__sparql_annotation_types_task(self):
        """
        Check if it contains a SPARQL_ANNOTATION_TYPES task
        """
        available_tasks = self.taskFinder.getAvailableTasks()

        taskName = 'SPARQL_ANNOTATION_TYPES'
        task = available_tasks.get(taskName, None)
        self.assertIsNotNone(taskName)

    def test_taskfinder_availabletasks_has__sparql_annotation_properties_task(self):
        """
        Check if it contains a SPARQL_ANNOTATION_PROPERTIES task
        """
        available_tasks = self.taskFinder.getAvailableTasks()

        taskName = 'SPARQL_ANNOTATION_PROPERTIES'
        task = available_tasks.get(taskName, None)
        self.assertIsNotNone(taskName)

    def test_taskfinder_availabletasks_has__sparql_annotation_thumbnail_task(self):
        """
        Check if it contains a SPARQL_ANNOTATION_THUMBNAIL task
        """
        available_tasks = self.taskFinder.getAvailableTasks()

        taskName = 'SPARQL_ANNOTATION_THUMBNAIL'
        task = available_tasks.get(taskName, None)
        self.assertIsNotNone(taskName)

    def test_taskfinder_availabletasks_has__stopword_filtering_task(self):
        """
        Check if it contains a STOPWORD_FILTERING task
        """
        available_tasks = self.taskFinder.getAvailableTasks()

        taskName = 'STOPWORD_FILTERING'
        task = available_tasks.get(taskName, None)
        self.assertIsNotNone(taskName)

    def test_taskfinder_availabletasks_has__stopword_retrieving_task(self):
        """
        Check if it contains a STOPWORD_RETRIEVAL task
        """
        available_tasks = self.taskFinder.getAvailableTasks()

        taskName = 'STOPWORD_RETRIEVAL'
        task = available_tasks.get(taskName, None)
        self.assertIsNotNone(taskName)

    def test_taskfinder_availabletasks_has__tokenizer_sentence_task(self):
        """
        Check if it contains a TOKENIZER_SENTENCE task
        """
        available_tasks = self.taskFinder.getAvailableTasks()

        taskName = 'TOKENIZER_SENTENCE'
        task = available_tasks.get(taskName, None)
        self.assertIsNotNone(taskName)

    def test_taskfinder_availabletasks_has__tokenizer_word_task(self):
        """
        Check if it contains a TOKENIZER_WORD task
        """
        available_tasks = self.taskFinder.getAvailableTasks()

        taskName = 'TOKENIZER_WORD'
        task = available_tasks.get(taskName, None)
        self.assertIsNotNone(taskName)

    def test_taskfinder_availabletasks_has__wordnet_task(self):
        """
        Check if it contains a WORDNET task
        """
        available_tasks = self.taskFinder.getAvailableTasks()

        taskName = 'WORDNET'
        task = available_tasks.get(taskName, None)
        self.assertIsNotNone(taskName)

    def test_taskfinder_taskname_is_None(self):
        """
        Check if the task name is None
        """
        taskName = None
        self.assertRaises(Exception, self.taskFinder.lookup, taskName)

    def test_taskfinder_taskname_is_empty(self):
        """
        Check if the task name is empty
        """
        taskName = ""
        self.assertRaises(Exception, self.taskFinder.lookup, taskName)

    def test_taskfinder_task_description_is_None(self):
        """
        Check if the task description is None
        """
        taskName = "BASIC"
        taskDescription = None
        self.assertRaises(Exception, self.taskFinder.lookup, taskName, taskDescription)

    def test_taskfinder_task_description_is_empty(self):
        """
        Check if the task description is empty
        """
        taskName = "BASIC"
        taskDescription = ""
        self.assertRaises(Exception, self.taskFinder.lookup, taskName, taskDescription)

    def test_taskfinder_task_input_is_None(self):
        """
        Check if the task input is None
        """
        taskName = "BASIC"
        taskDescription = "This is a description"
        taskInput = None
        self.assertRaises(Exception, self.taskFinder.lookup, taskName, taskDescription, taskInput)

    def test_taskfinder_task_input_is_empty(self):
        """
        Check if the task input is empty
        """
        taskName = "BASIC"
        taskDescription = "This is a description"
        taskInput = []
        self.assertRaises(Exception, self.taskFinder.lookup, taskName, taskDescription, taskInput)

    def test_taskfinder_task_input_is_not_array(self):
        """
        Check if the task input is not an array
        """
        taskName = "BASIC"
        taskDescription = "This is a description"
        taskInput = 1234
        self.assertRaises(Exception, self.taskFinder.lookup, taskName, taskDescription, taskInput)

    def test_taskfinder_task_input_has_invalid_values(self):
        """
        Check if the task input has invalid values
        """
        taskName = "BASIC"
        taskDescription = "This is a description"
        taskInput = [1]
        self.assertRaises(Exception, self.taskFinder.lookup, taskName, taskDescription, taskInput)

    def test_taskfinder_task_input_has_invalid_keys(self):
        """
        Check if the task input has invalid keys
        """
        taskName = "BASIC"
        taskDescription = "This is a description"
        taskInput = [{'a':1, 'b':2, 'c':3}]
        self.assertRaises(Exception, self.taskFinder.lookup, taskName, taskDescription, taskInput)

    def test_taskfinder_task_input_has_missing_keys(self):
        """
        Check if the task input has missing keys. Expected key, source, map-key
        """
        taskName = "BASIC"
        taskDescription = "This is a description"
        taskInput = [{'key':'abc', 'source':'internal-json'}]

        self.assertRaises(Exception, self.taskFinder.lookup, taskName, taskDescription, taskInput)


    def test_taskfinder_task_output_is_empty(self):
        """
        Check if the task output is empty
        """
        taskName = "BASIC"
        taskDescription = "This is a description"
        taskInput = [{"key": "pos", "source": "internal-output", "map-key": "data"}]
        taskOutput = None
        self.assertRaises(Exception, self.taskFinder.lookup, taskName, taskDescription, taskInput, taskOutput)

    def test_taskfinder_invalid_task_name(self):
        """
        Check if the task finder raises an exception if the task name does not match a task in the system
        """
        taskName = "not existing"
        taskDescription = "This is a description"
        taskInput = [{"key": "pos", "source": "internal-output", "map-key": "data"}]
        taskOutput = {'type': 'merge'}

        self.assertRaises(Exception, self.taskFinder.lookup, taskName, taskDescription, taskInput, taskOutput)

    def test_taskfinder_valid_task(self):
        """
        Check if the task finder can retrieve a task given a task name
        """
        taskName = "basic"
        taskDescription = "This is a description"
        taskInput = [{"key": "pos", "source": "internal-output", "map-key": "data"}]
        taskOutput = {'type': 'merge'}

        self.taskFinder.lookup(taskName, taskDescription, taskInput, taskOutput)

if __name__ == '__main__':
    unittest.main()
