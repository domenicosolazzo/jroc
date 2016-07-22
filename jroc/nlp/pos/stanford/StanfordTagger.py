# -*- coding: utf-8 -*-
import nltk
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
from nltk.chunk import conlltags2tree
from nltk.tree import Tree

class StanfordTagger(object):
    """
    Wrapper for the Stanford NER Tagger
    """
    __classifier = ""
    __stanfordJar = ""
    def __init__(self):
        self.__tagger = StanfordNERTagger(self.__classifier, self.__stanfordJar, encoding="utf-8")

    def tags(self, raw_text):
        """
        Extract named entities from a raw text
        :raw_text: The raw text
        """
        token_text = word_tokenize(raw_text)
        ne_tags = self.__tagger.tags(token_text)
        return(ne_tags)
