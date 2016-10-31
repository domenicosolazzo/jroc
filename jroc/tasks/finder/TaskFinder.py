from . import AVAILABLE_TASKS
class TaskFinder(object):
    """
    Task finder help you too lookup the correct Task based on his name.
    """

    def __init__(self):
        pass

    def lookup(self, taskName, description, taskInput, taskOutput):
        """
        It retrieve the correct task entity given a task name.
        It returns a tuple with (TaskEntity, TaskInput, TaskOutput)
        """
        taskNameUpper = taskName.upper()
        taskEntity = AVAILABLE_TASKS.get(taskNameUpper, None)

        if taskEntity is None:
            raise Exception("Error retrieving the correct task. The task name is not valid. Task Name: %s" % taskName)

        return (TaskEntity(name=description), taskInput, taskOutput)
