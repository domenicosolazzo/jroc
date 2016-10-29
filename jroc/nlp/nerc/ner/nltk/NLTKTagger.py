# -*- coding: utf-8 -*-
import os
from . import NERFinder

class NLTKTagger(object):
    """
    Wrapper for the NLTK NER Tagger
    """

    def __init__(self, language="en"):
        from nltk import pos_tag
        self.__tagger = pos_tag
        self.__namedEntitiesFinder = NERFinder(language=language)

    def __tags(self, raw_text):
        """
        Return the named entities tokens given a raw text
        :raw_text: Raw text
        """
        from nltk.tokenize import word_tokenize
        
        if isinstance(raw_text, str):
            # Decode to utf-8
            raw_text = raw_text.decode('utf-8')

        # Tokenize the string
        token_text = word_tokenize(raw_text)

        ne_tags = self.__tagger(token_text)
        return(ne_tags)

    def __generate_tree(self, tags):
        """
        Tranform a list of tags in a tree
        """
        from nltk import ne_chunk

        ne_tree = ne_chunk(tags)
        return ne_tree

    def getEntitiesByTags(self, tags):
        ne_entities = tags
        nlkt_tree = self.__generate_tree(ne_entities)
        entities = self.__namedEntitiesFinder.getEntities(nlkt_tree)
        return entities

    def getEntities(self, raw_text):
        """
        Get the entities from a raw text
        """
        ne_entities = self.__tags(raw_text=raw_text)
        nlkt_tree = self.__generate_tree(ne_entities)
        entities = self.__namedEntitiesFinder.getEntities(nlkt_tree)
        return entities
