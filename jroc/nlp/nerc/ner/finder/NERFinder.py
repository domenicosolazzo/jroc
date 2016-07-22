# -*- coding: utf-8 -*-
import nltk
import os
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
from nltk.chunk import conlltags2tree
from nltk.tree import Tree
from nltk import pos_tag

class NERFinder(object):
    """
    Wrapper for the NER Finder
    """
    __language = "en"
    def __init__(self, language="en"):
        self.__language = language

    def getLanguage(self):
        """
        Return the language
        """
        return self.__language

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

    def __parse_entities(self, ne_tree):
        """
        Parse named entities from the Tree
        :ne_tree: Named entities tree
        """
        ne = []
    	for subtree in ne_tree:
    		if type(subtree) == Tree: # If subtree is a noun chunk, i.e. NE != "O"
    			ne_label = subtree.label()
    			ne_string = " ".join([token for token, pos in subtree.leaves()])
    			ne.append((ne_string, ne_label))
    	return ne

    def getEntities(self, ne_entities_tokens):
        """
        Get entities given named entities tokens
        """
        bio_tags = self.__bio_tagger(ne_entities_tokens)
        tree = self.__generate_tree(bio_tags)
        entities = self.__parse_entities(tree)
        return entities
