
class BasicTask(object):
    """
    It defines a basic task for the pipeline
    """

    # Input for the task
    __input = None
    # Output for the task
    __output = None
    # Start date for the task
    __created = None
    # End date for the task
    __finished = None
    # Failed: true if the task has failed
    __failed = False

    # Kernel for the task
    __kernel = None

    def __init__(self):
        pass

    def execute(self):
        """
        Execute a task
        """
        raise Exception("Not implemented yet")
