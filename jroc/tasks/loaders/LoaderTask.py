from . import BasicTask
from . import JSONLoader
class LoaderTask(BasicTask):
    __kernel = None # Kernel for this loader
    def __init__(self, name, initial_task=False):
        super(LoaderTask, self).__init__(name, initial_task)


    def execute(self, input):
        """
        Execute a task
        """

        super(LoaderTask, self).execute(input)


        output = None
        try:
            self.__kernel = JSONLoader(json_string=input)
            output = self.__kernel.getData()
            self.finish(data=output, failed=False, error=None)
        except:
            output = "Error loading the json string"
            self.finish(data=None, failed=True, error=output)

        return output
