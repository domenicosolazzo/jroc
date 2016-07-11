from . import BasicTask
from . import StopwordManager

class StopwordFilteringTask(BasicTask):
    __kernel = None # Kernel for this loader

    def __init__(self, name, initial_task=False, language="en"):
        super(StopwordTask, self).__init__(name, initial_task)
        self.__kernel = StopwordManager(language=language)

    def execute(self, input):
        try:
            super(StopwordTask, self).execute(input)
            assert(isinstance(input, list))

            output = self.__kernel.filterStopwords(input)
            self.finish(data=output, failed=False, error=None)
        except:
            output = "Error filtering the stopwords"
            self.finish(data=None, failed=True, error=output)

class StopwordRetrievalTask(BasicTask):
    __kernel = None # Kernel for this loader

    def __init__(self, name, initial_task=False, language="en"):
        super(StopwordTask, self).__init__(name, initial_task)
        self.__kernel = StopwordManager(language=language)

    def execute(self, input):
        try:
            output = self.__kernel.getStopWords()
            self.finish(data=output, failed=False, error=None)
        except:
            output = "Error retrieving the stopwords"
            self.finish(data=None, failed=True, error=output)
