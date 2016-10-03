from . import BasicTask
from . import StopwordManager

class StopwordFilteringTask(BasicTask):
    """
    StopwordFilteringTask: Filter a input using a given set of stopwords
    """
    __kernel = None # Kernel for this loader

    __inputKey = 'data' # Expected input key
    def __init__(self, name, initial_task=False, language="en"):
        super(StopwordFilteringTask, self).__init__(name, initial_task)


    def execute(self, input):
        try:
            super(StopwordFilteringTask, self).execute(input)
            assert(isinstance(input, dict))

            language = input.get('language', 'en')
            self.__kernel = StopwordManager(language=language)

            data = input.get(self.__inputKey, None)
            if data is None:
                raise Exception("Error retrieving the input for this task. Task: %s" % self.getName())

            output = self.__kernel.filterStopWords(to_filter=data)
            self.finish(data=output, failed=False, error=None)
        except:
            output = "Error filtering the stopwords"
            self.finish(data=None, failed=True, error=output)
        return self.getOutput()

class StopwordRetrievalTask(BasicTask):
    """
    StopwordRetrievalTask: Retrieve the stopwords for a given language
    """
    __kernel = None # Kernel for this loader

    __inputKey = 'data' # Expected input key

    def __init__(self, name, initial_task=False, language="en"):
        super(StopwordRetrievalTask, self).__init__(name, initial_task)

    def execute(self, input=None):
        try:
            assert(isinstance(input, dict))
            super(StopwordRetrievalTask, self).execute(input)

            # Retrieve the language
            language = input.get('language', 'en')
            self.__kernel = StopwordManager(language=language)

            stopwords = self.__kernel.getStopWords()
            print("Stopwords", stopwords)

            if stopwords is not None:
                stopwords = list(stopwords)
            self.finish(data=stopwords, failed=False, error=None)
        except:
            raise
            output = "Error retrieving the stopwords"
            self.finish(data=None, failed=True, error=output)
        return self.getOutput()
