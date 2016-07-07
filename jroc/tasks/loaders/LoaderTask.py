import BasicTask
import JSONLoader
class LoaderTask(BasicTask):
    __kernel = None # Kernel for this loader
    def __init__(self, name, initial_task=False):
        super(LoaderTask, self).__init__(name, initial_task)


    def execute(self, input):
        """
        Execute a task
        """
        super(LoaderTask, self).execute(input)

        try:
            self.__kernel = JSONLoader(json_string=input)
            jsonData = self.__kernel.getData()
            self.finish(data=jsonData, failed=False, error=None)
        except:
            self.finish(data=None, failed=True, error="Error loading the json string")

        return jsonData
