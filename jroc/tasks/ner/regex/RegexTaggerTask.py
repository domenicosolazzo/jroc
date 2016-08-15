from . import BasicTask
from . import RegexTagger
import requests

class RegexTaggerTask(BasicTask):
    """
    RegexTaggerTask: Name Entity retrieval task using RegexTagger
    """
    __kernel = None # Kernel for this loader
    __inputKey = 'data' # Expected input key.
    __dataAvailable = False

    def __init__(self, name, data=None, initial_task=False, optionals={}):
        if data is not None:
            self.__dataAvailable = True
            self.__kernel = RegexTagger(json=data, optionals=optionals)
        super(RegexTaggerTask, self).__init__(name, initial_task)



    def execute(self, input):
        """
        Execute a task
        """
        output = None
        try:
            assert(isinstance(input, dict))
            super(RegexTaggerTask, self).execute(input)

            if self.__kernel is None:
                patterns = input.get('patterns', {})
                gaps = input.get('gaps', True)
                optionals = {"gaps":gaps}

                regexSentence = input.get('regex_sentence', None)
                if regexSentence is not None:
                    optionals["regex_sentence"] = regexSentence

                self.__kernel = RegexTagger(json=patterns, optionals=optionals)
    
            # Retrieve the text analysis
            raw_text = input.get(self.__inputKey, None)

            if raw_text is None:
                raise Exception("The input for RegexTagger was not available. Please that input of this task! ")

            output = self.__kernel.getEntities(raw_text)


            self.finish(data=output, failed=False, error=None)
        except:
            output = "Error retrieving the named entities using the RegexTagger"
            self.finish(data=None, failed=True, error=output)

        return self.getOutput()
