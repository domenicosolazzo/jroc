from . import BasicTask
from . import NERPosNo

class NERPosNoTask(BasicTask):
    """
    NERPosNoTask: Name Entity retrieval task
    """
    __kernel = None # Kernel for this loader
    __inputKey = 'pos-no' # Expected input key.

    def __init__(self, name, initial_task=False):
        super(NERPosNoTask, self).__init__(name, initial_task)
        self.__kernel = NERPosNo()


    def execute(self, input):
        """
        Execute a task
        """
        output = None
        try:
            assert(isinstance(input, dict))
            super(NERPosNoTask, self).execute(input)

            # Retrieve the stopwords
            stopwordKey = 'stopwords'
            stopwords = input.get(stopwordKey, [])
            textAnalysis = input.get(self.__inputKey, None)

            if not isinstance(stopwords, list) or textAnalysis is None:
                self.finish(data=None, failed=False, error=None)
                return self.getOutput()
                
            if not isinstance(stopwords, list):
                raise Exception("The retrieved stopwords have an invalid format.")

            # Retrieve the text analysis
            textAnalysis = input.get(self.__inputKey, None)
            if textAnalysis is None:
                raise Exception("The input for NERPosNo was not available. Please that input of this task! ")

            output = self.__kernel.findNER(textAnalysis=textAnalysis, stopwords=stopwords)

            self.finish(data=output, failed=False, error=None)
        except:
            output = "Error retrieving the named entities"
            self.finish(data=None, failed=True, error=output)

        return self.getOutput()
