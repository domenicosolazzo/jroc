import uuid
from datetime import datetime
import sys
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
    # Check if the pipeline has failed
    __failed = False

    # Error
    __error = {}

    # Save to DB: True if you should save every step in the db
    __saveToDB = False
    # Pipeline type
    __type = PipelineType.get('in-memory', 'in-memory')

    def __init__(self):
        # The id of the pipeline.
        self.__id = uuid.uuid4()
        self.__name = None
        self.__input = None
        self.__output = {
            'current-output':None
        }
        self.__failed = False
        # Created date for the task
        __created = datetime.utcnow()
        # Started date for the task
        __started = datetime.utcnow()
        # End date for the task
        __finished = datetime.utcnow()
        # Error
        self.__error = {
            'error': None,
            'error-stack': {}
        }
        self.__saveToDB = False
        # Pipeline type
        self.__type = PipelineType.get('in-memory', 'in-memory')

    def getName(self):
        """
        Get the name of the pipeline
        """
        return self.__name

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

    def setError(self, message):
        """
        Set the error message. Moreover, retrieve information about the last execption in the pipeline
        @message: error message
        """
        exctype, value = sys.exc_info()[:2]
        self.__error["error"] = message
        self.__error['error-stack'] = {
            'error-type':  exctype,
            'error-value':  value
        }

    def getError(self):
        """
        Get the last error in the pipeline
        """
        return self.__error

    def hasFailed(self):
        """
        Check if the pipeline has failed
        """
        self.__failed = True

    def finish(self, message="", hasFailed=False):
        """
        Set that the pipeline has finished.
        @message: Additional message.
        @hasFailed: Set if the pipeline has failed
        """
        if hasFailed == True:
            self.hasFailed()
            self.setError(message=message)
        self.__finished = datetime.utcnow()

    def mergeOutput(self, externalOutput):
        """
        Merge the output with the current pipeline output
        @externalOutput: Output that should be merged
        """
        assert(isinstance(externalOutput, dict))
        c = self.__output.copy()
        c.update(externalOutput)
        self.__output = c

    def getOutput(self, current=False):
        """
        Get the output of the pipeline. If current is True, it will return the output from the last tastk
        """
        if current == True:
            return self.__output.get('current_output', None)
        return self.__output

    def getInputData(self, metadata):
        """
        It returns the input object based on the metadata in input.
        Available input data:
        - Main: main input for the pipeline
        - external-input: You can set an external input for each item.
        - internal-output: The input is based on a given key of the internal output calculated during processing
        """
        assert(metadata is not None) # Metdata cannot be null
        assert(isinstance(metadata, list))  # Check that that we have a list in input
        assert(len(metadata) > 0) # Check the there is at least one input

        input = dict([('metadata', {})])
        if isinstance(metadata, list):
            for item in metadata:
                # Check source
                source = item.get('source', None)
                key = item.get('key', None)
                mapTo = item.get('map-key', 'main') # It will take key from 'map-key', otherwise it has 'main' as value
                if source is None:
                    raise Exception("Task input source cannot be null. Check the configuration of this pipeline.")

                if source == 'internal-output':
                    """
                    internal-output: Input is based on a given key of the internal calculated output.
                    """
                    if key is None:
                        raise Exception("The input key for this task is null. Check the configuration of this pipeline")

                    # Get Value
                    value = self.__output.get(key, None)

                    # set the input
                    input[mapTo] = value
                elif source == "main": # This is the main input
                    """
                    Main: This is the main input for the pipeline
                    """
                    input = self.__input
                elif source == "external-input":
                    """
                    External input: You can set an external input for a given input
                    """

                    data = item.get('data', None)
                    if data is None:
                        raise Exception("The external data is not present. Check the configuration of this pipeline")

                    input = data
                elif source == "remote-json":
                    """
                    It retrieves a json from a remote source
                    """
                    remoteSource = item.get('remote_source', None)
                    if remoteSource is None:
                        raise Exception("The remote source is invalid. Check the configuration of this pipeline")
                    r = requests.get(remoteSource)
                    if r.status_code != 200:
                        raise Exception("Error retrieving the data from the remote source. Status code: %d" % r.status_code)
                    json = r.json()
                    input[mapTo] = json
                else:
                    raise Exception("Source input is unavailable for this task")

                # Check if there is metadata for this item
                itemMetadata = item.get('metadata', None)
                if not itemMetadata is None:
                    input['metadata'][mapTo] = itemMetadata
        return input


    def addTask(self, task):
        """
        Add a task to the pipeline
        """
        pass

    def execute(self):
        """
        Execute the pipeline
        """
        self.__started = datetime.utcnow()
