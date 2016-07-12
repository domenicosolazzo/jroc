# -*- coding: utf-8 -*-
from . import BasicTask
from . import DataCleaner

class DataCleanerTask(BasicTask):
    __kernel = None # Kernel for this loader
    # The data cleaner task will filter a given set of characters
    __filterCharacters = True
    # The data cleaner task will remove double quotes
    __removeDoubleQuotes = True
    # It is a json string
    __isJsonString = True
    # Characters to be filtered
    __charactersToFilter = ["'","\n","«", "»", "*", "–", "•", "-"]
    # Replacement character
    __replacementCharacter = " "

    def __init__(self, name, initial_task=False):
        super(DataCleanerTask, self).__init__(name, initial_task)
        
    def setFilterCharacters(self, shouldFilter=True, characters=None):
        """
        Set the DataCleanerTask to filter a certain set of characters
        """
        assert(isinstance(shouldFilter, bool))
        self.__filterCharacters = shouldFilter

        if shouldFilter == True:
            assert(isinstance(characters, list))
            self.__charactersToFilter = characters

    def setRemoveDoubleQuotes(self, remove=True):
        """
        Set the DataCleanerTask to remove double quotes
        """
        # The input should be a boolean
        assert(isinstance(remove, bool))
        self.__removeDoubleQuotes = remove

    def setReplacementCharacter(self, replacementCharacter):
        """
        Set the replacemente character for the DataCleanerTask
        """
        # The input should be a string
        assert(isinstance(replacementCharacter, str))
        self.__replacementCharacter = replacementCharacter

    def setIsJson(self, isJsonString=False):
        """
        Set if the input is a json string
        """
        # The input should be a boolean
        assert(isinstance(isJsonString, bool))
        self.__isJsonString = isJsonString

    def execute(self, input):
        """
        Execute a data cleaner task
        """
        super(DataCleanerTask, self).execute(input)

        output = None
        try:
            self.__kernel = DataCleaner()
            output = input
            if self.__filterCharacters:
                output = self.__kernel.filterCharacters(characters=self.__charactersToFilter, replacement_character=self.__replacementCharacter, text=input)

            if self.__removeDoubleQuotes:
                output = self.__kernel.removeAdditionalDoubleQuotes(output, is_json_string=self.__isJsonString)
            self.finish(data=output, failed=False, error=None)
        except:
            output = "Error cleaning the string"
            self.finish(data=None, failed=True, error=output)

        #return self.getOutput()
