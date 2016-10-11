# -*- coding: utf-8 -*-
import nltk
import os
from . import NERFinder
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.chunk import conlltags2tree

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

    def __bio_tagger(self, ne_tagged):
        """
        Return BIO tags from named entities
        :ne_tagged: name_entities tokens
        """
        bio_tagged = []
        prev_tag = "O"
        for token, tag in ne_tagged:
            if tag == "O": #O
                bio_tagged.append((token, tag))
                prev_tag = tag
                continue
            if tag != "O" and prev_tag == "O": # Begin NE
                bio_tagged.append((token, "B-"+tag))
                prev_tag = tag
            elif prev_tag != "O" and prev_tag == tag: # Inside NE
                bio_tagged.append((token, "I-"+tag))
                prev_tag = tag
            elif prev_tag != "O" and prev_tag != tag: # Adjacent NE
                bio_tagged.append((token, "B-"+tag))
                prev_tag = tag
        return bio_tagged

    def __generate_tree(self, bio_tagged):
        """
        Tranform a list of tags in a tree
        """
        tokens, ne_tags = zip(*bio_tagged)
        pos_tags = [pos for token, pos in pos_tag(tokens)]

        conlltags = [(token, pos, ne) for token, pos, ne in zip(tokens, pos_tags, ne_tags)]
        ne_tree = conlltags2tree(conlltags)
        return ne_tree

    def __getEntities(self, taggedWords):
        """
        It returns the entities from a list of tagged words (NER or POS) after generating the syntax tree
        """
        bio_tagged = self.__bio_tagger(taggedWords)
        stanford_tree = self.__generate_tree(bio_tagged=bio_tagged)
        
        entities = self.__namedEntitiesFinder.getEntities(stanford_tree)
        return entities

    def getEntitiesByTags(self, pos_tagged_words):
        """
        Get entities from a list of word tagged with POS Tags.
        """
        entities = self.__getEntities(taggedWords=pos_tagged_words)
        return entities

    def getEntities(self, raw_text):
        """
        Get the entities from a raw text
        """
        ne_entities = self.__tags(raw_text=raw_text)
        entities = self.__getEntities(taggedWords=ne_entities)
        return entities
