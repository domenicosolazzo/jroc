from datetime import datetime
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
    __output = None
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

    def __init__(self, name, initial_task=False):
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

    def setOutput(self, output):
        """
        Set the output of a task
        """
        self.__output = output

    def setError(self, error):
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
        self.__failed = failed
        self.__finished = datetime.utcnow()
        self.setError(error)
        self.setOutput(data)
