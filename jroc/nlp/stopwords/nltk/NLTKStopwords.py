# -*- coding: utf-8 -*-
import os
from nltk.corpus import stopwords

class NLTKStopwords(object):
    """
    StopwordManager takes care to import the stopwords for a given language and filters a collection of strings.
    """
    AVAILABLE_LANGUAGES = dict(zip(['da', 'nl','en', 'fi', 'fr', 'de', 'hu', 'it','no', 'pt','ru','es','sv','tr'], stopwords.fileids()))
    AVAILABLE_LANGUAGES['da']= 'danish'
    AVAILABLE_LANGUAGES['nb']='norwegian'
    AVAILABLE_LANGUAGES['nn']='norwegian'
    AVAILABLE_LANGUAGES['se']='swedish'


    def __init__(self, filename=None, language="no"):
        if not language in self.AVAILABLE_LANGUAGES:
            raise ValueError("The stopword for this language is not available")
        self.__language = language.lower()
        self.__initializeStopwords()

    def __initializeStopwords(self):
        """
        Initialize the stopwords for a given language
        """
        language = self.AVAILABLE_LANGUAGES[self.__language]
        # Ge the stopwords for this language
        self.stopwords = list(set(stopwords.words(language)))

    def getStopwords(self):
        """
        It returns a new list of words
        """
    	return self.stopwords

    def filterStopWords(self, to_filter=[]):
        """
        Filter a list of words based on the stopword list.
        It returns a new list of words

        Arguments:
        :to_filter:  A list of words to be filtered (default=[])
        """
        assert isinstance(to_filter, (list, tuple))
        if len(to_filter) <= 0:
            return []

        filtered_words = [filtered_word for filtered_word in to_filter if (filtered_word.lower() not in self.stopwords)]
        return filtered_words
