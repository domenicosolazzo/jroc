import os
class StopwordManager(object):

    FILENAME_ENV_NAME = 'OBT_STOPWORDS_FILENAME'
    FILENAME = ''
    FILENAME_CUSTOM = "%s/data/stopwords_custom.txt" % (os.path.dirname(os.path.realpath(__file__)), )
    AVAILABLE_LANGUAGES = ["da", "de", "en", "fi", "fr", "it", "nb", "no", "nn", "sv"]

    def __init__(self, filename=None, language="no"):
        if language in self.AVAILABLE_LANGUAGES: # Check if the language is available
            currentDirectory = "%s" % (os.path.dirname(os.path.realpath(__file__)), )
            self.FILENAME = "%s/data/%s%s.txt"  % (currentDirectory, "stopwords_", language)

        self.__initializeStopwords()

    def __retrieveStopwords(self, filename=''):
        stopwords = []
        if filename:
            f = open(filename, 'r')
            lines = f.readlines()
            f.close()

            ## Parse each line
            stopwords = filter(None, map(lambda x: x.split('|')[0].strip().lower().decode('utf-8'), lines))
        return stopwords

    def __initializeStopwords(self):
        """
        Parse the stoplist file and return a list of stopwords
        """
        if self.FILENAME is None:
            raise Error("Error retrieving the stopword list. The filename is invalid or missing")

        languageStopwords = []
        if self.FILENAME:
            languageStopwords = self.__retrieveStopwords(self.FILENAME)
        customStopwords = self.__retrieveStopwords(self.FILENAME_CUSTOM)
        # Extend the stopword list
        languageStopwords.extend(customStopwords)
        self.stopwords = set(languageStopwords)

    def getStopWords(self):
        """
        It returns a new list of words
        """
    	return self.stopwords

    def filterStopWords(self, to_filter=[]):
        """
        Filter a list of words based on the stopword list.
        It returns a new list of words

        Arguments:
        to_filter - A list of words to be filtered (default=[])
        """
        assert isinstance(to_filter, (list, tuple))
        if len(to_filter) <= 0:
            return []

        filtered_words = [filtered_word for filtered_word in to_filter if (filtered_word.lower() not in self.stopwords)]
        return filtered_words
