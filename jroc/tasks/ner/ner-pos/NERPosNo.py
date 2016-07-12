from . import BasicTask
from . import NERPosNo
class NERPosNo(BasicTask):
    __kernel = None # Kernel for this loader

    def __init__(self, name, initial_task=False):
        super(NERPosNo, self).__init__(name, initial_task)
        self.__kernel = NERPosNo()


    def execute(self, input):
        try:
            assert(isinstance(input, dict))
            # POS key
            posKey = "pos-no"
            if not posKey in input:
                raise Exception("The text analysis from the Norwegian POS Tagger is not present. This step cannot be completed")
            # Stopword key
            stopwordKey = "stopwords"
            if not stopwordKey in input:
                raise Exception("The stopwords have not been retrieved before starting this task. This step cannot be completed")

            textAnalysis = input.get(posKey, None)
            stopwords = input.get(stopwordKey, [])

            entities = self.__kernel.findNER(textAnalysis, stopwords)
            self.finish(data=entities, failed=False, error=None)
        except:
            output = "Error loading the json string"
            self.finish(data=None, failed=True, error=output)

        return self.getOutput()
