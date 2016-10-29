from . import BasicTask
from . import WordnetManager

class WordnetTask(BasicTask):
    """
    WordnetTask: Fetch synonyms, hyponyms and hyperyms of a set of word
    """
    __kernel = None # Kernel for this loader

    __inputKey = 'data' # Expected input key
    def __init__(self, name, initial_task=False, hyperyms=True, hyponyms=True):
        super(WordnetTask, self).__init__(name, initial_task)
        self.__kernel = WordnetManager()
        self.__searchHyperyms = hyperyms
        self.__searchHyponysm = hyponyms

    def execute(self, input):
        try:
            super(WordnetTask, self).execute(input)
            assert(isinstance(input, dict))

            data = input.get(self.__inputKey, None)
            if data is None:
                raise Exception("Error retrieving the input for this task. Task: %s" % self.getName())

            if not isinstance(data, list):
                raise Exception("Error validating the data in input. Data array: " % data)

            # Retrieving the language
            language =  input.get('language', 'en')

            # Retrieve Synonyms
            synonyms = self.__kernel.getSynonyms(words=data, language_code=language)

            hyperyms = {}
            if self.__searchHyperyms == True:
                # Retrieve Hyperyms
                hyperyms = self.__kernel.getHypernyms(words=data, language_code=language)

            hyponyms = {}
            if self.__searchHyponysm  == True:
                # Retrieve Hyponyms
                hyponyms = self.__kernel.getHyponyms(words=data, language_code=language)

            # Result dictionary
            output = {}

            # fetch the words
            for word in data:
                output[word] = dict([('synonyms', synonyms.get(word, None)),
                                     ('hyperyms', hyperyms.get(word, None)),
                                     ('hyponyms', hyponyms.get(word, None))])


            self.finish(data=output, failed=False, error=None)
        except:
            output = "Error fetching information from Wordnet"
            self.finish(data=None, failed=True, error=output)
        return self.getOutput()
