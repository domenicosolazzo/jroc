from . import BasicPipeline
from . import StopwordRetrievalTask
from . import PosTaggerTask, PosTaggerTagsTask
from . import LanguageDetectionPipeline
from collections import defaultdict

class PosTaggerPipeline(BasicPipeline):
    """
    PosTagger Pipeline
    """
    def __init__(self, input, name="PosTagger Pipeline"):
        pass
        super(PosTaggerPipeline, self).__init__(input, name)
        # Pipelines to be run before the current one
        self.addPipelinesBefore([(LanguageDetectionPipeline, {"name":"Language Pipeline", "input":{"source":"main", "data":input}, "output":{"type": "merge"}}) ])

        # Run these tasks
        self.addTask(( StopwordRetrievalTask(name="Stopword Retrieval"), {"input":[{"key": "language", "source": "internal-output", "map-key": "language"}], "output":{"key":"stopwords", "source": "internal-output", "type": "json" } } ))
        self.addTask(( PosTaggerTask(name="Pos Tagger"), {"input":[
                                                                    { "key":"language", "source":"internal-output", "map-key": "language"},
                                                                    {"key": "json-loader", "source": "internal-output", "map-key": "data"}
                                                                  ],
                                                          "output": {"key":"pos", "source": "internal-output", "type": "json" }
                                                          } ))
        self.addTask((PosTaggerTagsTask(name="Pos Tagger Tags Task"), {
                                                                        "input":[{"key": "pos", "source":"internal-output", "type": "json", "map-key": "pos"}, {"key": "language", "source": "internal-output", "map-key": "language"}],
                                                                        "output": {"key": "tags", "source": "internal-output", "type": "json"}
                                                                        }))



    def execute(self):
        super(PosTaggerPipeline, self).execute()
