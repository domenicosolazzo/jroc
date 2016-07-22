# -*- coding: utf-8 -*-
import nltk
import os
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
from nltk.chunk import conlltags2tree
from nltk.tree import Tree
from nltk import pos_tag

CLASSIFIERS_MODELS = {
    'en': ['english.all.3class.distsim.crf.ser.gz'],
    'es': ['stanford-spanish-corenlp-2015-10-14-models.jar'],
    'de': []
}
class StanfordTagger(object):
    """
    Wrapper for the Stanford NER Tagger
    """
    __currentDirectory = os.path.dirname(os.path.realpath(__file__)) # Current directory
    __classifier = "%s/dist/classifiers/english.all.3class.distsim.crf.ser.gz"
    __stanfordJar = "%s/dist/stanford-ner.jar"

    def __init__(self, language='en'):
        self.__stanfordJar = "%s/dist/stanford-ner.jar" % self.__currentDirectory
        classifierByLanguage = CLASSIFIERS_MODELS.get(language, None)
        if classifierByLanguage is None:
            raise Exception("Language is not available")
        if not isinstance(classifierByLanguage, list) or len(classifierByLanguage) <= 0:
            raise Exception("The classifier model have an invalid format")

        classifier = classifierByLanguage[0]
        self.__classifier = "%s/dist/classifiers/%s" % (self.__currentDirectory, classifier)
        self.__tagger = StanfordNERTagger( self.__classifier,
                                           self.__stanfordJar,
                                           encoding="utf-8")

    def tags(self, raw_text):
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

    def bio_tagger(self, ne_tagged):
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

    def stanford_tree(self, bio_tagged):
        """
        Tranform a list of tags in a tree
        """
        tokens, ne_tags = zip(*bio_tagged)
        pos_tags = [pos for token, pos in pos_tag(tokens)]

        conlltags = [(token, pos, ne) for token, pos, ne in zip(tokens, pos_tags, ne_tags)]
        ne_tree = conlltags2tree(conlltags)
        return ne_tree

    def stanford_ne(self, ne_tree):
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
