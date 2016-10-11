from . import BasicTask
from . import PosManager

class PosTaggerTask(BasicTask):
    """
    PosTaggerTask: Part-of-Speech task
    """
    __kernel = None # Kernel for this loader

    __inputKey = 'data' # Expected input key
    __language = None

    def __init__(self, name, initial_task=False, language="no"):
        super(PosTaggerTask, self).__init__(name, initial_task)
        self.__kernel = PosManager(language=language)
        self.__language = language

    def execute(self, input):
        try:
            assert(isinstance(input, dict))
            super(PosTaggerTask, self).execute(input)

            # Language key
            languageKey = 'language'
            if languageKey in input:
                self.__language = input.get(languageKey, "no")
                self.__kernel = PosManager(language=self.__language)

            inputText = input.get(self.__inputKey, None)
            if inputText is None:
                raise Exception("The text given in input is not valid. Please that input of this task! ")

            output = self.__kernel.analyze(input=inputText)

            self.finish(data=output, failed=False, error=None)
        except:
            output = "Error analyzing the text with the pos tagger"
            self.finish(data=None, failed=True, error=output)

        return self.getOutput()


class PosTaggerTagsTask(BasicTask):
    __kernel = None # Kernel for this loader
    __inputKey = 'pos' # Expected input key

    def __init__(self, name, initial_task=False, language="no", filterStopwords=True):
        super(PosTaggerTagsTask, self).__init__(name, initial_task)
        self.__kernel = PosManager(language=language)

    def execute(self, input):
        try:
            assert(isinstance(input, dict))
            super(PosTaggerTagsTask, self).execute(input)

            languageKey = 'language'
            if languageKey in input:
                self.__language = input.get(languageKey, "no")
                self.__kernel = PosManager(language=self.__language)
                
            # Retrieve the stopwords
            stopwordKey = 'stopwords'
            stopwords = input.get(stopwordKey, [])
            if not isinstance(stopwords, list):
                raise Exception("The retrieved stopwords have an invalid format.")

            # Retrieve the text analysis
            textAnalysis = input.get(self.__inputKey, None)
            if textAnalysis is None:
                raise Exception("The input for PosTagger Tags Task was not available. Please that input of this task! ")

            tags = self.__kernel.findTags(input=textAnalysis)

            output = [tag for tag in tags if not tag in stopwords]
            self.finish(data=output, failed=False, error=None)
        except:
            output = "Error finding the tags"
            self.finish(data=None, failed=True, error=output)

        return self.getOutput()
