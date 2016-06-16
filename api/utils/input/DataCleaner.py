# -*- coding: utf-8 -*-
class DataCleaner(object):

    def __init__(self):
        pass

    def filterCharacters(self, text=""):
        """
        Filter a set of characters from the original text.
        Characters that will be filtered: ', \n, «, », *, –, -
        """
        characters = ["'","\n","«", "»", "*", "–", "•", "-"]
        for character in characters:
            replacingCharacter = " "
            text = text.replace(character, replacingCharacter)
        return text
