from . import AVAILABLE_TASKS
class TaskFinder(object):
    """
    Task finder help you too lookup the correct Task based on his name.
    """

    def __init__(self):
        pass

    def __validateTaskInput(self, taskInput):
        # Check if the task input is a dictionary
        if not isinstance(taskInput, dict):
            raise Exception("The task input has an invalid format. Requested a dictionary. Current format: %s" % type(taskInput))

        # Check the mandatory keys
        mandatoryKeys = ['key', 'source', 'map-key']

        for key in mandatoryKeys:
            if not key in taskInput:
                raise Exception("Key %s is not present in the task input" % key)

            # Check if the key has a value
            keyValue = taskInput.get(key, None)
            if keyValue is None or len(keyValue) <= 0:
                raise Exception("Key %s cannot have null or empty value. Current value: %s" % (key, keyValue) )

    def __validate(self, taskName='', description='', taskInput=[], taskOutput={}):
        if taskName is None or len(taskName) <= 0:
            raise Exception("Task name cannot be null or empty.")

        if description is None or len(description) <= 0:
            raise Exception("Task description cannot be null or empty.")

        # Test taskInput
        print(taskName, description, taskInput)
        if taskInput is None or len(taskInput) <= 0:
            raise Exception("Task input cannot be null or empty")


        # Check if the task input is an array
        if not isinstance(taskInput, list):
            raise Exception("Task input is not an array")

        [self.__validateTaskInput(task) for task in taskInput]

        if taskOutput is None:
            raise Exception("Task output cannot be null")

        if not isinstance(taskOutput, dict):
            raise Exception("Task output has wrong format. Excepted a dictionary. Current format: %s" % type(taskOutput))

        return True

    def lookup(self, taskName, description, taskInput, taskOutput):
        """
        It retrieve the correct task entity given a task name.
        It returns a tuple with (TaskEntity, TaskInput, TaskOutput)
        """
        self.__validate(taskName, description, taskInput, taskOutput)

        taskNameUpper = taskName.upper()
        TaskEntity = AVAILABLE_TASKS.get(taskNameUpper, None)

        if TaskEntity is None:
            raise Exception("Error retrieving the correct task. The task name is not valid. Task Name: %s" % taskName)

        return (TaskEntity(name=description), taskInput, taskOutput)

    def getAvailableTasks(self):
        return AVAILABLE_TASKS
