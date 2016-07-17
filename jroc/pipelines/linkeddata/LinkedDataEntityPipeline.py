from . import BasicPipeline
from . import EntityAnnotationTask, EntityAnnotationURITask, EntityAnnotationTypesTask, EntityAnnotationThumbnailTask, EntityAnnotationPropertiesTask

class LinkedDataEntityPipeline(BasicPipeline):
    """
    LinkedData Entity Pipeline
    """
    # Use entity annotation
    __withEntityAnnotation = False
    __withTypesAnnotation = False
    __withPropertiesAnnotation = False
    __withPropertyValuesAnnotation = False

    def __init__(self, input, name="LinkedData Entity Pipeline",
                withTypesAnnotation=False, withPropertiesAnnotation=False,
                withPropertyValuesAnnotation=False, withThumbnailAnnotation=False, withEntityAnnotation=False):
        assert(isinstance(withEntityAnnotation, bool))
        super(LinkedDataEntityPipeline, self).__init__(input, name)
        self.__withTypesAnnotation = withTypesAnnotation
        self.__withPropertiesAnnotation = withPropertiesAnnotation
        self.__fetchPropertyValues = withPropertyValuesAnnotation
        self.__withEntityAnnotation = withEntityAnnotation
        self.__withThumbnailAnnotation = withThumbnailAnnotation

        # Run these tasks
        self.addTask(( EntityAnnotationURITask(name="LinkedData - Entity URI Task") , {"input":[{"key": "pos", "source": "main", "map-key": "entity_name"}], "output": {"key":"entity-uri", "source": "internal-output", "type": "json" }}))

        if self.__withTypesAnnotation == True:
            self.addTask(( EntityAnnotationTypesTask(name="LinkedData - Entity Types Task") , {"input":[{"key": "pos", "source": "main", "map-key": "entity_name"}], "output": {"key":"entity-types", "source": "internal-output", "type": "json" }}))

        if self.__withThumbnailAnnotation == True:
            self.addTask(( EntityAnnotationThumbnailTask(name="LinkedData - Entity Types Task") , {"input":[{"key": "pos", "source": "main", "map-key": "entity_name"}], "output": {"key":"entity-thumbnail", "source": "internal-output", "type": "json" }}))


        if self.__withPropertiesAnnotation == True:
            self.addTask(( EntityAnnotationPropertiesTask(name="LinkedData - Entity Properties Task", withPropertyValues=self.__fetchPropertyValues) , {"input":[{"key": "pos", "source": "main", "map-key": "entity_name"}], "output": {"key":"entity-properties", "source": "internal-output", "type": "json" }}))
        """
        if self.__withEntityAnnotation == True:
            self.addTask(( EntityAnnotationTask(name="LinkedData - Entity Task") , {"input":[{"key": "pos", "source": "main", "map-key": "entities", data:[input]}], "output": {"key":"entities-annotated", "source": "internal-output", "type": "json" }}))
        """

    def execute(self):
        super(LinkedDataEntityPipeline, self).execute()
