from . import Pipeline
import Queue

class BasicPipeline(Pipeline):
    """
    Basic pipeline with in-memory storage
    """
    # Task list
    __tasks = Queue.Queue()
    __pipelines = {
        "pre": Queue.Queue(),
        "post": Queue.Queue()
    }

    def __init__(self, input, name="Basic pipeline"):
        super(BasicPipeline, self).__init__()
        self.__tasks = Queue.Queue()
        self.__pipelines = {
            "pre": Queue.Queue(),
            "post": Queue.Queue()
        }
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

    def addPipelinesBefore(self, pipelines):
        """
        Run these pipelines before the current pipeline will start. The pipeline will be run sequentially
        @pipelines: A list of pipelines
        """
        assert(isinstance(pipelines, list))
        # You need to add at least a pipeline
        assert(len(pipelines) > 0)
        r = [self.__pipelines["pre"].put(pipeline) for pipeline in pipelines]


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

    def __before_execute(self):
        """
        Execute all the pipelines before the current one
        """
        count = 0
        isEmpty = self.__pipelines.get("pre").empty()
        try:
            while not isEmpty:
                count = count + 1

                # Get next pipeline
                pipeline = self.__pipelines.get("pre").get(block=False)
                pipelineInfo = pipeline[1]
                assert(isinstance(pipelineInfo, dict))
                assert('name' in pipelineInfo)
                assert('input' in pipelineInfo)
                assert('output' in pipelineInfo)

                pipelineName = pipelineInfo.get('name', '')
                pipelineInput = pipelineInfo.get('input', None)
                assert(isinstance(pipelineInput, dict))
                pipelineOutput = pipelineInfo.get('output', None)
                assert(isinstance(pipelineOutput, dict))

                source = pipelineInput.get('source', 'main')
                data = None
                if source == "main":
                    data = pipelineInput.get('data', None)
                elif source == "internal-output":
                    assert('key' in pipelineInput)
                    data = self.getInputData(pipelineInput)
                else:
                    raise Exception("Source not implemented for this Pipeline. Requested source: %s" % source)

                pipelineInstance = pipeline[0](input=data, name=pipelineName)
                # Get the output and merge it
                pipelineInstance.execute()
                self.__pipelines.get("pre").task_done()

                output = pipelineInstance.getOutput(current=False)
                self.mergeOutput(output)


        except Queue.Empty:
            # All the pre-pipeline tasks have been executed. Pipeline is ready to start...
            pass
        except:
            self.finish(message="Error executing the pre-pipeline tasks", hasFailed=True)
            return False
        return True

    def execute(self):
        """
        Execute the pipeline
        """
        # Run pre-pipeline
        resultBefore = self.__before_execute()
        if resultBefore == False:
            return

        # Until the queue is empty
        isTasksEmpty = self.__tasks.empty()
        while not isTasksEmpty:
            try:
                # Get the task tuple
                nextStep = self.__tasks.get(block=False)

                # Get the task
                task = nextStep[0]
                print("TAsk", task.getName())
                # Get the metadata for the task
                metadata = nextStep[1]
                metadataIn = metadata.get("input", {})
                metadataOut = metadata.get("output", {})

                # Fetch input data
                input = self.getInputData(metadataIn)
                # Get the output from the previous task
                output = self.runTask(task, input, metadataOut)
                # Set the task as done
                self.__tasks.task_done()
                if task.hasFailed():
                    taskError = task.getError()
                    self.finish(message=taskError, hasFailed=True)
                    self.setOutput("current-error", taskError)
                    print("Task Error:", task.getName(), taskError)
                    return
                    #raise Exception("Pipeline has failed. The current task returned an error: %s" % task.getName())

                # Set the output
                outputKey = metadataOut.get('key', '%s-output' % task.getPrefix())
                outputData = output.get(outputKey, None)
                self.setOutput(outputKey, outputData)
                self.setOutput("current-output", outputData)


            except Queue.Empty:
                # All the tasks  for the pipeline have been executed
                isTasksEmpty = True
            except:
                pipelineError = self.getError()
                self.finish(message="Error executing the pipeline", hasFailed=True)
                self.setOutput("current-error", pipelineError)
                print("Pipeline Error:", pipelineError)
                return


        # Return the result
        self.finish(message="All good", hasFailed=False)
        finalOutput = self.getOutput()
        return finalOutput


    def wait(self):
        """
        Blocks until the tasklist is empty
        """
        self.__tasks.join()
