from . import BasicTask
from . import SPARQLAdapter

class EntityAnnotationTask(BasicTask):
    """
    EntityAnnotationTask: Annotate a list of entities with information from a SPARQL Endpoint
    """
    __kernel = None # Kernel for this loader

    __inputKey = 'entities' # Expected input key
    def __init__(self, name, initial_task=False):
        super(EntityAnnotationTask, self).__init__(name, initial_task)


    def execute(self, input):
        """
        Execute a task
        """
        output = None
        try:
            assert(isinstance(input, dict))
            super(EntityAnnotationTask, self).execute(input)
            data = input.get(self.__inputKey, None)
            if data is None or not isinstance(data, list):
                raise Exception("Impossible to parse these entities. Please that input of this task! ")
            self.__kernel = SPARQLAdapter()
            output = [{"entity": word, "metadata": self.__kernel.entityExtraction(word, advancedSearch=False)} for word in data]
            self.finish(data=output, failed=False, error=None)
        except:
            output = "Error annotating the entities"
            self.finish(data=None, failed=True, error=output)

        return self.getOutput()

class EntityAnnotationURITask(BasicTask):
    __kernel = None # Kernel for this loader

    __inputKey = 'entity_name' # Expected input key
    def __init__(self, name, initial_task=False):
        super(EntityAnnotationURITask, self).__init__(name, initial_task)


    def execute(self, input):
        """
        Execute a task
        """
        output = None
        try:
            super(EntityAnnotationURITask, self).execute(input)

            data = input
            if data is None:
                raise Exception("Impossible to retrieve the URI of a given entity. Please that input of this task! ")

            self.__kernel = SPARQLAdapter()
            output = self.__kernel.getUniqueURI(data)
            self.finish(data=output, failed=False, error=None)
        except:
            output = "Error retrieving the URI of a given entity"
            self.finish(data=None, failed=True, error=output)

        return self.getOutput()

class EntityAnnotationTypesTask(BasicTask):
    __kernel = None # Kernel for this loader

    __inputKey = 'entity_name' # Expected input key
    def __init__(self, name, initial_task=False):
        super(EntityAnnotationTypesTask, self).__init__(name, initial_task)


    def execute(self, input):
        """
        Execute a task
        """
        output = None
        try:
            super(EntityAnnotationTypesTask, self).execute(input)

            data = input
            if data is None:
                raise Exception("Impossible to retrieve the types of a given entity. Please that input of this task! ")

            self.__kernel = SPARQLAdapter()
            output = self.__kernel.getEntityType(data)
            self.finish(data=output, failed=False, error=None)
        except:
            output = "Error retrieving the types of a given entity"
            self.finish(data=None, failed=True, error=output)

        return self.getOutput()


class EntityAnnotationPropertiesTask(BasicTask):
    __kernel = None # Kernel for this loader

    __inputKey = 'entity_name' # Expected input key
    __withPropertyValues = True
    __requestedProperties = []

    def __init__(self, name, initial_task=False, withPropertyValues=True, properties=[]):
        super(EntityAnnotationPropertiesTask, self).__init__(name, initial_task)
        self.__withPropertyValues = withPropertyValues
        self.__requestedProperties = properties


    def execute(self, input):
        """
        Execute a task
        """

        output = None
        try:
            super(EntityAnnotationPropertiesTask, self).execute(input)

            data = input
            if data is None:
                raise Exception("Impossible to retrieve the properties of a given entity. Please that input of this task! ")

            self.__kernel = SPARQLAdapter()
            output = None
            if not self.__requestedProperties is None and len(self.__requestedProperties) > 0:
                output = {
                    # Property[0] => Property name
                    # Property[1] => Language
                    'properties': [self.__kernel.getProperty(data, property[0], property[1]) for property in self.__requestedProperties]
                }

            else:
                output = self.__kernel.getProperties(data, fetchValues=self.__withPropertyValues)
            self.finish(data=output, failed=False, error=None)
        except:
            output = "Error retrieving the properties of a given entity"
            self.finish(data=None, failed=True, error=output)

        return self.getOutput()

class EntityAnnotationThumbnailTask(BasicTask):
    __kernel = None # Kernel for this loader

    __inputKey = 'entity_name' # Expected input key

    def __init__(self, name, initial_task=False):
        super(EntityAnnotationThumbnailTask, self).__init__(name, initial_task)


    def execute(self, input):
        """
        Execute a task
        """

        output = None
        try:
            super(EntityAnnotationThumbnailTask, self).execute(input)

            data = input
            if data is None:
                raise Exception("Impossible to retrieve the thumbnail of a given entity. Please that input of this task! ")

            self.__kernel = SPARQLAdapter()
            output = self.__kernel.getThumbnail(data)
            self.finish(data=output, failed=False, error=None)
        except:
            output = "Error retrieving the thumbnail of a given entity"
            self.finish(data=None, failed=True, error=output)

        return self.getOutput()
