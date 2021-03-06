from . import BasicPipeline
from . import NERPosNoTask
from . import TaggerTagsTask
from . import EntityAnnotationTask
from . import StanfordTaggerTask
from . import PosTaggerPipeline
from . import NERFormatTask
from collections import defaultdict

class NERPipeline(BasicPipeline):
    """
    NERPipeline Pipeline: It retrieves entities inside a given text.

    Entity annotation: If withEntityAnnotation is True, it will retrieve information for each retrieved entity from a SPARQL endpoint.
    It could take some time to perform this step.
    """
    # Use entity annotation
    __withEntityAnnotation = False
    __withStanfordTagging = False
    __withNERFormatting = False

    def __init__(self, input, name="NER Pipeline", withEntityAnnotation=False, withStanfordTagging=False, withNERFormatting=False):
        assert(isinstance(withEntityAnnotation, bool))
        super(NERPipeline, self).__init__(input, name)
        self.__withEntityAnnotation = withEntityAnnotation
        self.__withStanfordTagging = withStanfordTagging
        self.__withNERFormatting = withNERFormatting

        # Pipelines to be run before the current one
        self.addPipelinesBefore([(PosTaggerPipeline, {"name":"Pos Tagger Pipeline", "input":{"source":"main", "data":input}, "output":{"type": "merge"}}) ])

        # Run these tasks
        self.addTask(( TaggerTagsTask(name="NER Task"), {"input":[{"key": "pos", "source": "internal-output", "map-key": "data"}], "output":{"key":"entities", "source": "internal-output", "type": "json" } } ))
        if self.__withStanfordTagging == True:
            self.addTask(( StanfordTaggerTask(name="NER Task"), {"input":[{"key": "json-loader", "source": "internal-output", "map-key": "data"}], "output":{"key":"entities-stanford", "source": "internal-output", "type": "json" } } ))

        if self.__withNERFormatting == True:
            self.addTask(( NERFormatTask(name="NER Format Task"), {"input":[{"key": "entities", "source": "internal-output", "map-key": "entities"}, {"key": "entities-stanford", "source": "internal-output", "map-key": "entities-stanford"}], "output":{"key":"entities-formatted", "source": "internal-output", "type": "json" } } ))


        if self.__withEntityAnnotation == True:
            # Add the entity annotation task.
            # ISSUE when this pipeline is running from the api. It works from unittests
            self.addTask(( EntityAnnotationTask(name="LinkedData TASK"), {  "input":[{ "key":"entities", "source":"internal-output", "map-key": "entities"}],
                                                                        "output": {"key":"entities-annotated", "source": "internal-output", "type": "json" }
                                                                      }))



    def execute(self):
        super(NERPipeline, self).execute()
