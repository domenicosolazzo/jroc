from datetime import datetime
from collections import defaultdict

class Task(object):
    """
    Main Task class
    """
    # Task name
    __name = None
    # Task prefix
    __prefix = None
    # Input for the task
    __input = None
    # Output for the task
    __output = dict({})
    # Initial task
    __initial_task = False
    # Created date for the task
    __created = None
    # Started date for the task
    __started = None
    # End date for the task
    __finished = None
    # Failed: true if the task has failed
    __failed = False
    # Error: Last error in the task
    __error = None
    # Metadata
    __metadata = dict({'input':[{'key':'main'}], 'output': {'key': 'data'}})

    def __init__(self, name, initial_task=False):
        print("metadata task", self.__metadata)
        if name == None or len(name) <= 0:
            raise Exception("Wrong task name!")
        # Set the name of the task
        self.__name = name
        # Set the prefix for the task
        self.__prefix = name.replace(" ", "-").lower()
        # It is an initial task
        self.__initial_task = initial_task
        # Creation date
        self.__created = datetime.utcnow()
        # metadata
        self.__metadata = dict({'input':[{'key':'main'}], 'output': {'key': 'data'}})
        # output
        self.__output = dict({})


    def setMetadataOutput(self, metadata):
        """
        Set metadata output
        """
        assert(metadata is not None)
        assert(isinstance(metadata, dict))
        self.__metadata["output"] = metadata

    def setMetadataInput(self, metadata):
        """
        Set metadata input
        """
        assert(metadata is not None)
        assert(isinstance(metadata, dict))
        self.__metadata["input"] = metadata

    def setOutput(self, output):
        """
        Set the output of a task
        """
        print("metadata-output", self.__metadata, output)
        outputKey = self.__metadata.get('output', {}).get('key', 'data')
        print("key", outputKey)
        outputValue = output
        self.__output[outputKey] = outputValue
        print("output", self.__output)

    def setError(self, error):
        """
        Set the error
        """
        self.__error = error

    def getOutput(self):
        return self.__output

    def getName(self):
        """
        Get the name of the task
        """
        return self.__name

    def getPrefix(self):
        """
        Get the prefix of the task
        """
        return self.__prefix

    def isInitialTask(self):
        """
        Check if it is an initial task
        """
        return self.__initial_task == True

    def hasFailed(self):
        """
        Check if the task has failed
        """
        return self.__failed == True

    def execute(self, input=None):
        """
        Execute the task
        """
        if input is None:
            raise Exception("The task input is invalid.")
        self.__input = input
        self.__started = datetime.utcnow()
        return

    def finish(self, data, failed=False, error=None):
        """
        The task has finished
        """
        self.__failed = failed
        self.__finished = datetime.utcnow()
        self.setError(error)
        self.setOutput(data)
