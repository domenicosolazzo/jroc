from . import BasicTask

class PosTaggerTask(BasicTask):
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

            output = self.__kernel.analyze()

            self.finish(data=output, failed=False, error=None)
        except:
            output = "Error analyzing the text with the pos tagger"
            self.finish(data=None, failed=True, error=output)

        return self.getOutput()
