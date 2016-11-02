from . import AVAILABLE_TASKS
class TaskFinder(object):
    """
    Task finder help you too lookup the correct Task based on his name.
    """

    def __init__(self):
        pass

    def __validate(self, taskName, description, taskInput, taskOutput):
        if taskName is None or len(taskName) <= 0:
            raise Exception("Task name cannot be null or empty.")

        if description is None or len(description) <= 0:
            raise Exception("Task description cannot be null or empty.")

        if taskInput is None:
            raise Exception("Task input cannot be null")

        if taskOutput is None:
            raise Exception("Task output cannot be null")

        return True

    def lookup(self, taskName, description, taskInput, taskOutput):
        """
        It retrieve the correct task entity given a task name.
        It returns a tuple with (TaskEntity, TaskInput, TaskOutput)
        """
        self.__validate(taskName, description, taskInput, taskOutput)

        taskNameUpper = taskName.upper()
        taskEntity = AVAILABLE_TASKS.get(taskNameUpper, None)

        if taskEntity is None:
            raise Exception("Error retrieving the correct task. The task name is not valid. Task Name: %s" % taskName)

        return (TaskEntity(name=description), taskInput, taskOutput)

    def getAvailableTasks(self):
        return AVAILABLE_TASKS
