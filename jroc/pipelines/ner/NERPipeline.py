from . import BasicPipeline
from . import NERPosNoTask
from . import EntityAnnotationTask
from . import PosTaggerPipeline
from collections import defaultdict

class NERPipeline(BasicPipeline):
    """
    NERPipeline Pipeline
    """
    def __init__(self, input, name="PosTagger Pipeline", withEntityAnnotation=True):
        assert(isinstance(withEntityAnnotation, bool))
        super(NERPipeline, self).__init__(input, name)
        # Pipelines to be run before the current one
        self.addPipelinesBefore([(PosTaggerPipeline, {"name":"Pos Tagger Pipeline", "input":{"source":"main", "data":input}, "output":{"type": "merge"}}) ])

        # Run these tasks
        self.addTask(( NERPosNoTask(name="NER Task"), {"input":[{"key": "pos", "source": "internal-output", "map-key": "pos-no"}], "output":{"key":"entities", "source": "internal-output", "type": "json" } } ))
        if withEntityAnnotation == True:
            self.addTask(( EntityAnnotationTask(name="LinkedData TASK"), {  "input":[{ "key":"entities", "source":"internal-output", "map-key": "entities"}],
                                                                        "output": {"key":"entities-annotated", "source": "internal-output", "type": "json" }
                                                                      }))



    def execute(self):
        super(NERPipeline, self).execute()
