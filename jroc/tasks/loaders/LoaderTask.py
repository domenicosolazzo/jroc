from . import BasicTask
from . import JSONLoader

class LoaderTask(BasicTask):
    __kernel = None # Kernel for this loader

    __inputKey = 'json' # Expected input key
    def __init__(self, name, initial_task=False):
        super(LoaderTask, self).__init__(name, initial_task)


    def execute(self, input):
        """
        Execute a task
        """

        output = None
        try:
            assert(isinstance(input, dict))
            super(LoaderTask, self).execute(input)

            inputText = input.get(self.__inputKey, None)
            if inputText is None:
                raise Exception("The json string is invalid. Please that input of this task! ")

            self.__kernel = JSONLoader(json_string=inputText)
            output = self.__kernel.getData()
            
            self.finish(data=output, failed=False, error=None)
        except:
            output = "Error loading the json string"
            self.finish(data=None, failed=True, error=output)

        return self.getOutput()
