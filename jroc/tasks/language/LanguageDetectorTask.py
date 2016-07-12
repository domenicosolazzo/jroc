from . import BasicTask
from . import LanguageDetector

class LanguageDetectorTask(BasicTask):
    __kernel = None # Kernel for this loader
    __inputKey = 'main' # Expected input key

    def __init__(self, name, initial_task=False):
        super(LanguageDetectorTask, self).__init__(name=name, initial_task=initial_task)
        self.__kernel = LanguageDetector()
        self.setMetadataOutput({"key": "language", "source": "internal-output", "type":"json"})

    def execute(self, input):
        try:
            assert(isinstance(input, dict))
            super(LanguageDetectorTask, self).execute(input)

            inputText = input.get(self.__inputKey, None)
            if inputText is None:
                raise Exception("The input was invalid. Please check the input of the LanguageDetector task! ")

            # Classifying the language
            languageDetection = self.__kernel.classify(text=inputText)

            language = languageDetection[0]
            prediction = languageDetection[1]
            output = language
            self.finish(data=output, failed=False, error=None)
        except:
            output = "Error detecting the language"
            self.finish(data=None, failed=True, error=output)

        print("aaaaa", self.getOutput())
        return self.getOutput()
