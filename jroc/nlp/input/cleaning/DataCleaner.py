# -*- coding: utf-8 -*-
class DataCleaner(object):

    def __init__(self):
        pass

    def filterCharacters(self, characters=["'","\n","«", "»", "*", "–", "•", "-"], replacement_character=" ", text=""):
        """
        Filter a set of characters from the original text.
        """
        assert(isinstance(text, str))
        assert(isinstance(characters, list))

        replacementCharacter = " "
        if isinstance(replacement_character, str):
            replacementCharacter = replacement_character

        for character in characters:
            text = text.replace(character, replacementCharacter)
        return text
