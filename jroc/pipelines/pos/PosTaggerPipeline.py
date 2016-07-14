from . import BasicPipeline
from . import DataCleanerTask
from . import LanguageDetectorTask
from . import LoaderTask
from . import StopwordRetrievalTask
from . import PosTaggerTask
from . import LanguageDetectionPipeline
from collections import defaultdict

class PosTaggerPipeline(BasicPipeline):
    """
    PosTagger Pipeline
    """
    def __init__(self, input, name="PosTagger Pipeline"):

        super(PosTaggerPipeline, self).__init__(input, name)

        self.addTask(( DataCleanerTask(name="Data Cleaner"), { "input": [{ "source": "main"}], "output": { "key": "data-cleaner", "source":"internal-output", "type": "json"} } ))
        self.addTask(( LoaderTask(name="Loader"), { "input": [{ "key":"data-cleaner", "source": "internal-output", "map-key":"json"}], "output": { "key": "json-loader", "source":"internal-output", "type": "json"} } ))
        self.addTask(( LanguageDetectorTask(name="Language Detector"), { "input": [{ "key":"json-loader", "source": "internal-output", "map-key":"main"}], "output": { "key": "language", "source":"internal-output", "type": "json"} }))
        self.addTask(( StopwordRetrievalTask(name="Stopword Retrieval"), {"input":[{"key": "language-pipeline", "source": "internal-output", "mapping": "import"}], "output":{"key":"stopwords", "source": "internal-output", "type": "json" } } ))
        self.addTask(( PosTaggerTask(name="Pos Tagger"), {"input":[
                                                                    { "key":"language", "source":"internal-output", "map-key": "language"},
                                                                    {"key": "json-loader", "source": "internal-output", "map-key": "data"}
                                                                  ],
                                                          "output": {"key":"pos", "source": "internal-output", "type": "json" }
                                                          } ))



    def execute(self):
        super(PosTaggerPipeline, self).execute()
