from . import BasicPipeline
from . import NERPosNoTask
from . import EntityAnnotationTask
from . import PosTaggerPipeline
from collections import defaultdict

class NERPipeline(BasicPipeline):
    """
    NERPipeline Pipeline
    """
    def __init__(self, input, name="PosTagger Pipeline"):
        pass
        super(NERPipeline, self).__init__(input, name)
        # Pipelines to be run before the current one
        self.addPipelinesBefore([(PosTaggerPipeline, {"name":"Pos Tagger Pipeline", "input":{"source":"main", "data":input}, "output":{"type": "merge"}}) ])

        # Run these tasks
        self.addTask(( NERPosNoTask(name="PosTagger Task"), {"input":[{"key": "data", "source": "internal-output", "map-key": "pos-no"}], "output":{"key":"entities", "source": "internal-output", "type": "json" } } ))
        self.addTask(( EntityAnnotationTask(name="LinkedData TASK"), {  "input":[{ "key":"entities", "source":"internal-output", "map-key": "entities"}],
                                                                        "output": {"key":"entities-annotated", "source": "internal-output", "type": "json" }
                                                                      }))



    def execute(self):
        super(NERPipeline, self).execute()
