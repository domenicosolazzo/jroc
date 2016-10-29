from . import BasicTask
from . import StanfordTagger

class StanfordTaggerTask(BasicTask):
    """
    StanfordTaggerTask: Name Entity retrieval task
    """
    __kernel = None # Kernel for this loader
    __inputKey = 'data' # Expected input key.

    def __init__(self, name, initial_task=False):
        super(StanfordTaggerTask, self).__init__(name, initial_task)
        self.__kernel = StanfordTagger()


    def execute(self, input):
        """
        Execute a task
        """
        output = None
        try:
            assert(isinstance(input, dict))
            super(StanfordTaggerTask, self).execute(input)

            # Retrieve the text analysis
            raw_text = input.get(self.__inputKey, None)
            if raw_text is None:
                raise Exception("The input for Stanford NERTagger was not available. Please that input of this task! ")

            output = self.__kernel.getEntities(raw_text)

            self.finish(data=output, failed=False, error=None)
        except:
            output = "Error retrieving the named entities"
            self.finish(data=None, failed=True, error=output)

        return self.getOutput()
