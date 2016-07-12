import uuid
"""
Pipeline types
In-Memory: The pipeline will be executed sequentially in-memory
Kafka: The pipeline will spread the tasks on several queues
"""
PipelineType = {
    'in-memory': 'in-memory', # In-Memory pipeline
    'kafka': 'kafka', # Kafka Pipeline
    'redis': 'redis', # Redis Pipeline
}

class Pipeline(object):

    # Pipeline ID
    __id = None
    # Pipeline Name
    __name = None
    # Input for the Pipeline
    __input = None
    # Output for the Pipeline
    __output = {
        'current-output':None
    }

    # Save to DB: True if you should save every step in the db
    __saveToDB = False
    # Pipeline type
    __type = PipelineType.get('in-memory', 'in-memory')

    def __init__(self):
        # The id of the pipeline.
        self.__id = uuid.uuid4()

    def setType(self, type):
        """
        Set the type of the pipeline
        """
        self.__type = PipelineType.get('in-memory', 'in-memory')

    def setName(self, name):
        """
        Set the name for the pipeline
        """
        self.__name = name

    def setInput(self, input):
        """
        Set the input for the pipeline
        """
        self.__input = input

    def setOutput(self, key, output):
        """
        Set the output for the pipeline
        """
        self.__output[key] = output

    def getOutput(self, current=False):
        """
        Get the output of the pipeline. If current is True, it will return the output from the last tastk
        """
        if current == True:
            return self.__output.get('current_output', None)
        return self.__output

    def getInputData(self, metadata):
        """
        It returns the input object based on the metadata in input
        """
        assert(metadata is not None) # Metdata cannot be null
        assert(isinstance(metadata, list))  # Check that that we have a list in input
        assert(len(metadata) > 0) # Check the there is at least one input

        input = {}
        if isinstance(metadata, list):
            for item in metadata:
                # Check source
                source = item.get('source', None)
                if source is None:
                    raise Exception("Task input source cannot be null. Check the configuration of this pipeline.")

                if source == 'internal-output':

                    # Get Key
                    mapTo = item.get('map-key', 'main') # It will take key from 'map-key', otherwise it has 'main' as value
                    key = item.get('key', None)
                    if key is None:
                        raise Exception("The input key for this task is null. Check the configuration of this pipeline")

                    # Get Value
                    value = self.__output.get(key, None)

                    # set the input
                    input[mapTo] = value
                elif source == "main": # This is the main input
                    input = self.__input
                else:
                    raise Exception("Source input is unavailable for this task")
        return input


    def addTask(self, task):
        """
        Add a task to the pipeline
        """
        raise Exception("Not implemented yet")

    def execute(self):
        """
        Execute the pipeline
        """
        raise Exception("Not implemented yet")
