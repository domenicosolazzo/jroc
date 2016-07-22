# -*- coding: utf-8 -*-
import nltk
import os
from . import NERFinder
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize

class StanfordTagger(object):
    """
    Wrapper for the Stanford NER Tagger
    """
    __currentDirectory = os.path.dirname(os.path.realpath(__file__)) # Current directory
    __classifier = "%s/dist/classifiers/english.all.3class.distsim.crf.ser.gz"
    __stanfordJar = "%s/dist/stanford-ner.jar"

    def __init__(self, language="en"):
        self.__stanfordJar = "%s/dist/stanford-ner.jar" % self.__currentDirectory
        self.__classifier = "%s/dist/classifiers/english.all.3class.distsim.crf.ser.gz" % (self.__currentDirectory,)
        self.__tagger = StanfordNERTagger( self.__classifier,
                                           self.__stanfordJar,
                                           encoding="utf-8")
        self.__namedEntitiesFinder = NERFinder(language=language)

    def __tags(self, raw_text):
        """
        Return the named entities tokens given a raw text
        :raw_text: Raw text
        """
        if isinstance(raw_text, str):
            # Decode to utf-8
            raw_text = raw_text.decode('utf-8')
        # Tokenize the string
        token_text = word_tokenize(raw_text)
        # Retrieve the named entities from the tokens
        ne_tags = self.__tagger.tag(token_text)
        return(ne_tags)

    def getEntities(self, raw_text):
        """
        Get the entities from a raw text
        """
        ne_entities = self.__tags(raw_text=raw_text)
        entities = self.__namedEntitiesFinder.getEntities(ne_entities)
        return entities
