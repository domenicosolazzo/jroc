from . import BasicPipeline
from . import DataCleanerTask
from . import LanguageDetectorTask
from . import LoaderTask
from collections import defaultdict

class LanguageDetectionPipeline(BasicPipeline):
    """
    Language Detection Pipeline
    """
    def __init__(self, input, name="Language Detection Pipeline"):

        super(LanguageDetectionPipeline, self).__init__(input, name)

        self.addTask(( DataCleanerTask(name="Data Cleaner"), { "input": [{ "source": "main"}], "output": { "key": "data-cleaner", "source":"internal-output", "type": "json"} } ))
        self.addTask(( LoaderTask(name="Loader"), { "input": [{ "key":"data-cleaner", "source": "internal-output", "map-key":"json"}], "output": { "key": "json-loader", "source":"internal-output", "type": "json"} } ))
        self.addTask(( LanguageDetectorTask(name="Language Detector"), { "input": [{ "key":"json-loader", "source": "internal-output", "map-key":"main"}], "output": { "key": "language", "source":"internal-output", "type": "json"} }))


    def execute(self):
        super(LanguageDetectionPipeline, self).execute()
