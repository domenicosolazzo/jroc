from . import Pipeline
import Queue

class BasicPipeline(Pipeline):
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

        self.__tasks.put(task)

    def runTask(self, task, input, metadataOutput):
        """
        Run the task given an input. It receives information where to store the output.
        @task: The task
        @input: Input for the task
        @metadataOutput: Information about the task.
        """
        task.setOutputMetadata(metadataOutput)
        taskResult =  task.execute()
        return taskResult

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

            # Set the output
            outputKey = metadataOut.get('key', '%s-output' % task.getPrefix())
            outputData = output.get(outputKey, None)
            self.setOutput(outputKey, outputData)

            # Set the task as done
            self.__tasks.task_done()
        # Return the result
        return self.getOutput()


    def wait(self):
        """
        Blocks until the tasklist is empty
        """
        self.__tasks.join()



"""
pipeline = BasicPipeline()
pipeline.addTask((DataCleanerTask, {
                        input: { "source": "main" },
                        output: { "key": "data-cleaner", "source": "output", "type": "text" }
                    }))
pipeline.addTask((
        LoaderTask, {
                        input: { "key":"data-cleaner", "source": "output" },
                        output: { "key": "json-loader", "source": "output", "type": "json" }
                    }))
pipeline.addTask((
        LanguageTask, {
                        input: { "key":"json-loader", "source": "output" },
                        output: { "key": "json-loader", "source": "output", "type": "json" }
                    }))

pipeline.addTask((
        StopwordRetrievalTask, {
                        input: { "key":"json-loader", "source": "output" },
                        output: { "key": "stopwords", "source": "output", "type": "json" }
                    }))

pipeline.addTask((
        PosTaggerTask, {
                        input: { "key":"json-loader", "source": "output" },
                        output: { "key": "pos-tagger-no", "source": "output", "type": "json" }
                    }))

pipeline.addTask((
        NERPosOBT, {
                        input: [{ "key":"pos-tagger-no", "source": "output" }, {"key":"stopwords", "source": "output", "map-key":"stopwords"}],
                        output: { "key": "ner-obt", "source": "output", "type": "json" }
                    }))

pipeline.addTask(
        FormatDataTask, {
                        input: [{ "key":"ner-obt", "source": "output", "map-key": "ner" }, {"key":"language", "source": "output", "map-key":"language"}],
                        output: { "key": "data", "source": "final", "type": "json" }
                    }))
)
"""
