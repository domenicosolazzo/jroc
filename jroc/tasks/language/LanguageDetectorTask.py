from . import BasicTask
from . import LanguageDetector

class LanguageDetectorTask(BasicTask):
    __kernel = None # Kernel for this loader

    def __init__(self, name, initial_task=False):
        super(LanguageDetectorTask, self).__init__(name=name, initial_task=initial_task)
        self.__kernel = LanguageDetector()

    def execute(self, input):
        try:
            assert(isinstance(input, str))
            assert(len(input) > 0)
            assert(input is not None)
            super(LanguageDetectorTask, self).execute(input)

            # Classifying the language
            languageDetection = self.__kernel.classify(text=input)

            language = languageDetection[0]
            prediction = languageDetection[1]
            output = {
                "language": language,
                "prediction": prediction
            }
            self.finish(data=output, failed=False, error=None)
        except:
            output = "Error detecting the language"
            self.finish(data=None, failed=True, error=output)

        print(output)

        return output
