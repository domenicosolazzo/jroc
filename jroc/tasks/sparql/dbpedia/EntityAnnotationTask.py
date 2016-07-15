from . import BasicTask
from . import SPARQLAdapter

class EntityAnnotationTask(BasicTask):
    __kernel = None # Kernel for this loader

    __inputKey = 'entities' # Expected input key
    def __init__(self, name, initial_task=False):
        super(EntityAnnotationTask, self).__init__(name, initial_task)


    def execute(self, input):
        """
        Execute a task
        """

        output = None
        try:
            assert(isinstance(input, dict))
            super(EntityAnnotationTask, self).execute(input)

            data = input.get(self.__inputKey, None)
            if data is None or not isinstance(data, list):
                raise Exception("Impossible to parse these entities. Please that input of this task! ")

            self.__kernel = SPARQLAdapter()

            output = [{"entity": word, "metadata": self.__kernel.entityExtraction(word, advancedSearch=True)} for word in data]
            self.finish(data=output, failed=False, error=None)
        except:
            raise
            output = "Error loading the json string"
            self.finish(data=None, failed=True, error=output)

        return self.getOutput()
