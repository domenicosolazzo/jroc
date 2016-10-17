# -*- coding: utf-8 -*-

class StanfordTagger(object):
    """
    Wrapper for the Stanford NER Tagger
    """
    __classifier = ""
    __stanfordJar = ""
    def __init__(self, data=None):
        from nltk.tag import StanfordNERTagger

        self.__tagger = StanfordNERTagger(self.__classifier, self.__stanfordJar, encoding="utf-8")

    def tags(self, raw_text):
        """
        Extract named entities from a raw text
        :raw_text: The raw text
        """
        from nltk.tokenize import word_tokenize

        token_text = word_tokenize(raw_text)
        ne_tags = self.__tagger.tags(token_text)
        return(ne_tags)
