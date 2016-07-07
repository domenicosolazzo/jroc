import Queue
class BasicPipeline(Pipeline):
    # Task list
    __tasks = Queue.Queue()

    def __init__(self, input, name="Basic pipeline"):
        super(BasicPipeline, self).__init__()
        self.setName(name)
        self.setInput(input)

    def addTask(self, task):
        if not isinstance(task, BasicTask):
            raise Exception("Wrong type of task. This pipeline accepts only BasicTask")

        self.__tasks.put(task)

    def runTask(self, task, input):
        taskResult =  task.execute()
        return taskResult

    def execute(self):
        # Until the queue is empty
        while not self.__tasks.empty():
            # Get the task
            task = self.__tasks.get()
            input = None
            # Retrieve the input
            if task.isInitialTask() == True:
                input = self.getInput(current=True)
            else:
                input = self.getOutput()
            # Get the output from the previous task
            output = self.runTask(task, input)
            # Set the output
            self.setOutput('current_output', output)
            self.setOutput('%s-output', output)
            # Set the task as done
            self.__tasks.task_done()
        # Return the result
        return self.getOutput()

    def wait(self):
        """
        Blocks until the tasklist is empty
        """
        self.__tasks.join()
