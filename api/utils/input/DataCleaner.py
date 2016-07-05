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

        # Check for double quotes inside the text.
        character = "\""
        matches = text.split(character)
        # It should be a json in this format {"data": "<value>"}
        if len(matches) <= 5:
            return text # Do not do anything

        replacedText = "%s\"%s\"%s" % ("\"".join(matches[0:3]), " ".join(matches[3:-1]), matches[-1])

        return replacedText
