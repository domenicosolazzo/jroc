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

    def removeAdditionalDoubleQuotes(self, text, is_json_string=True):
        """
        Remove additional number of quotes from text
        @text: The text to clean up
        @is_json_string: If it is a json string
        """
        # Check for double quotes inside the text.
        character = "\""


        if (is_json_string == True): # Check if the string is a json string
            # It should be a json in this format {"data": "<value>"}
            matches = text.split(character)
            minimum_json_parts = 5 # '{"data": "abc"}'
            if len(matches) <= minimum_json_parts:
                return text # Do not do anything
            # Filter empty elements
            matches = filter(None, matches)
            text = "%s\"%s\"%s" % ("\"".join(matches[0:3]), " ".join(matches[3:-1]), matches[-1])
        else:
            # Replace the character
            text = text.replace(character, " ")

        return text
