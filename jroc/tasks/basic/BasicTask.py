import Task
from datetime import datetime

class BasicTask(Task):
    """
    It defines a basic task for the pipeline
    """
    # Kernel for the task
    __kernel = None


    def __init__(self, name, initial_task):
        super(BasicTask, self).__init__(name, initial_task)

    def execute(self, input):
        """
        Execute a task
        """
        super(BasicTask, self).execute(input)
