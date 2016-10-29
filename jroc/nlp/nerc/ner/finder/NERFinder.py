# -*- coding: utf-8 -*-
import os

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

    def __parse_entities(self, ne_tree):
        """
        Parse named entities from the Tree
        :ne_tree: Named entities tree
        """
        from nltk.tree import Tree

        ne = []
    	for subtree in ne_tree:
    		if type(subtree) == Tree: # If subtree is a noun chunk, i.e. NE != "O"
    			ne_label = subtree.label()
    			ne_string = " ".join([token for token, pos in subtree.leaves()])
    			ne.append((ne_string, ne_label))
    	return ne

    def getEntities(self, tree):
        """
        Get entities given a tree
        """
        entities = self.__parse_entities(tree)
        return entities
