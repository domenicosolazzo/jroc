from . import Pipeline
import Queue

class BasicPipeline(Pipeline):
    """
    Basic pipeline with in-memory storage
    """
    # Task list
    __tasks = Queue.Queue()

    def __init__(self, input, name="Basic pipeline"):
        super(BasicPipeline, self).__init__()
        self.setName(name)
        self.setInput(input)

    def addTask(self, taskInfo):
        """
        Add a task to the pipeline.
        @taskinfo: A tuple containing the current task, and information about its input and output.
        """
        if not isinstance(taskInfo, tuple):
            raise Exception("Wrong type of task. This pipeline accepts only a tuple. (Task instance, options)")

        self.__tasks.put(taskInfo)

    def runTask(self, task, input, metadataOutput):
        """
        Run the task given an input. It receives information where to store the output.
        @task: The task
        @input: Input for the task
        @metadataOutput: Information about the task.
        """
        task.setMetadataOutput(metadataOutput)
        task.execute(input)
        return task.getOutput()

    def execute(self):
        """
        Execute the pipeline
        """
        # Until the queue is empty
        while not self.__tasks.empty():
            # Get the task tuple
            nextStep = self.__tasks.get()

            # Get the task
            task = nextStep[0]
            # Get the metadata for the task
            metadata = nextStep[1]
            metadataIn = metadata.get("input", {})
            metadataOut = metadata.get("output", {})

            # Fetch input data
            input = self.getInputData(metadataIn)

            # Get the output from the previous task
            output = self.runTask(task, input, metadataOut)
            if task.hasFailed():
                raise Exception("Pipeline has failed. The current task returned an error: %s" % task.getName())

            # Set the output
            outputKey = metadataOut.get('key', '%s-output' % task.getPrefix())
            outputData = output.get(outputKey, None)
            self.setOutput(outputKey, outputData)
            self.setOutput("current-output", outputData)

            # Set the task as done
            self.__tasks.task_done()

        # Return the result
        finalOutput = self.getOutput()
        return finalOutput


    def wait(self):
        """
        Blocks until the tasklist is empty
        """
        self.__tasks.join()
