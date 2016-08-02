from . import BasicTask
from . import StanfordTagger

class TaggerTagsTask(BasicTask):
    """
    TaggerTask: It returns the tags given some POS tags
    """
    __kernel = None # Kernel for this loader
    __inputKey = 'data' # Expected input key.

    def __init__(self, name, initial_task=False):
        super(TaggerTagsTask, self).__init__(name, initial_task)
        self.__kernel = StanfordTagger()


    def execute(self, input):
        """
        Execute a task
        """
        output = None
        try:
            assert(isinstance(input, dict))
            super(TaggerTagsTask, self).execute(input)

            # Stopwords
            stopwordKey = 'stopwords'
            stopwords = input.get(stopwordKey, None)
            
            # Retrieve the text analysis
            text_analysis = input.get(self.__inputKey, None)
            if text_analysis is None:
                raise Exception("The input for StanfordTaggerTagsTask was not available. Please that input of this task! ")

            if not pos in text_analysis:
                raise Exception("The text analysis does not contain POS information for this task. Please check the input of this task")

            posTags = text_analysis.get('pos', None)
            output = self.__kernel.getEntitiesByTags(posTags)

            self.finish(data=output, failed=False, error=None)
        except:
            output = "Error retrieving the tags from a the POS tags"
            self.finish(data=None, failed=True, error=output)

        return self.getOutput()
