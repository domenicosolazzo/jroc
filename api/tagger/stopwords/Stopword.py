import os
class StopwordManager(object):

    FILENAME_ENV_NAME = 'OBT_STOPWORDS_FILENAME'
    FILENAME = ''

    def __init__(self, filename=None):
        if filename is not None:
            self.FILENAME = filename
        elif os.environ.get('OBT_STOPWORDS_FILENAME', None) is None:
            currentDirectory = os.path.dirname(os.path.realpath(__file__))
            self.FILENAME = "%s/%s"  % (currentDirectory, "stopwords_list.txt")
        else:
            self.FILENAME = os.environ.get('OBT_STOPWORDS_FILENAME', None)

        self.__initializeStopwords()


    def __initializeStopwords(self):
        """
        Parse the stoplist file and return a list of stopwords
        """
        if self.FILENAME is None:
            raise Error("Error retrieving the stopword list. The filename is invalid or missing")

        file = self.FILENAME

        f = open(file, 'r')
        lines = f.readlines()
        f.close()
        ## Parse each line
        self.stopwords = filter(None, map(lambda x: x.split('|')[0].strip().lower().decode('utf-8'), lines))
        return lines

    #
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
        return filter(lambda x: not x.lower() in self.stopwords, to_filter)
