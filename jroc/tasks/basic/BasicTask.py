import Task
from datetime import datetime

class BasicTask(Task):
    """
    It defines a basic task for the pipeline
    """
    # Kernel for the task
    __kernel = None


    def __init__(self, input):
        super(BasicTask, self).__init__(input)

    def execute(self, input):
        """
        Execute a task
        """
        super(BasicTask, self).execute(input)
        
