from . import BasicTask

class MixDataTask(BasicTask):
    """
    PosTaggerTask: Part-of-Speech task
    """
    __kernel = None # Kernel for this loader

    __inputKey = 'data' # Expected input key
    __language = None

    def __init__(self, name, initial_task=False):
        super(MixDataTask, self).__init__(name, initial_task)
        self.__kernel = PosManager(language=language)
        self.__language = language

    def execute(self, input):
        try:
            assert(isinstance(input, dict))
            super(MixDataTask, self).execute(input)



            inputText = input.get(self.__inputKey, None)
            if inputText is None:
                raise Exception("The sources are not valid. Please that input of this task! ")

            output = self.__kernel.analyze(input=inputText)
            self.finish(data=output, failed=False, error=None)
        except:
            output = "Error analyzing the text with the pos tagger"
            self.finish(data=None, failed=True, error=output)

        return self.getOutput()
