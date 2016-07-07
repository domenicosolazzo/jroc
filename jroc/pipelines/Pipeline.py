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
        'current_output':None
    }

    # Save to DB: True if you should save every step in the db
    __saveToDB = False
    # Pipeline type
    __type = PipelineType.get('in-memory', 'in-memory')

    def __init__(self):
        self.__id = uuid.uuid4()

    def setType(self, type):
        self.__type = PipelineType.get('in-memory', 'in-memory')

    def setName(self, name):
        self.__name = name

    def setInput(self, input):
        self.__input = input

    def setOutput(self, key, output):
        self.__output[key] = output

    def getOutput(self, current=False):
        if current == True:
            return self.__output.get('current_output', None)
        return self.__output


    def addTask(self, task):
        raise Exception("Not implemented yet")

    def execute(self):
        raise Exception("Not implemented yet")
