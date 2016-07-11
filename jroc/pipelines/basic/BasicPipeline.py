from . import Pipeline
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

    def runTask(self, task, input, metadataOutput):
        task.setOutputMetadata(metadataOutput)
        taskResult =  task.execute()
        return taskResult

    def execute(self):
        # Until the queue is empty
        while not self.__tasks.empty():
            # Get the task
            nextStep = self.__tasks.get()

            task = nextStep[0]
            metadataIn = nextStep[1]["input"]
            metadataOut = nextStep[1]["output"]

            input = self.getInputData(metadataIn)

            # Get the output from the previous task
            output = self.runTask(task, input, metadataOut)

            # Set the output
            outputKey = metadataOut.get('key', None)
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

    def getInputData(self, metadataIn):
        pass



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
