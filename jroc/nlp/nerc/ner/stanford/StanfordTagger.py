# -*- coding: utf-8 -*-
import nltk
import os
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
from nltk.chunk import conlltags2tree
from nltk.tree import Tree

class StanfordTagger(object):
    """
    Wrapper for the Stanford NER Tagger
    """
    __currentDirectory = os.path.dirname(os.path.realpath(__file__)) # Current directory
    __classifier = "%s/dist/classifiers/english.all.3class.distsim.crf.ser.gz"
    __stanfordJar = "%s/dist/stanford-ner.jar"

    def __init__(self):
        self.__stanfordJar = "%s/dist/stanford-ner.jar" % self.__currentDirectory
        self.__classifier = "%s/dist/classifiers/english.all.3class.distsim.crf.ser.gz" % self.__currentDirectory
        self.__tagger = StanfordNERTagger()

    def tags(self, raw_text):
        token_text = word_tokenize(raw_text)
        ne_tags = self.__tagger.tags(token_text)
        return(ne_tags)
