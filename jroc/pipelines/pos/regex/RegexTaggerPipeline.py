from . import BasicPipeline
from . import RegexTaggerTask, RegexTaggerMixerTask
from . import LanguageDetectionPipeline
from collections import defaultdict

class RegexTaggerPipeline(BasicPipeline):
    """
    RegexTagger Pipeline: it extracts entities using regex
    """
    def __init__(self, input, name="RegexTagger Pipeline"):
        pass
        super(RegexTaggerPipeline, self).__init__(input, name)
        # Pipelines to be run before the current one
        self.addPipelinesBefore([(LanguageDetectionPipeline, {"name":"Language Detection Pipeline", "input":{"source":"main", "data":input}, "output":{"type": "merge"}}) ])

        # Run these tasks
        self.addTask(( RegexTaggerTask(name="Regex Tagger"), {"input":[
                                                                {"key": "json-loader", "source": "internal-output", "map-key": "data"},
                                                                {   "key": "patterns",
                                                                    "source":"remote-json",
                                                                    "map-key": "patterns",
                                                                    "remote_source": "https://gist.githubusercontent.com/domenicosolazzo/670cad541808f6960f161fa4e47dc59a/raw/d4f79cf6e2050f3d1b934cbfaae5b40bb73db969/Json"}
                                                            ],
                                                            "output": {"key":"regex", "source": "internal-output", "type": "json" }
                                                          } ))
        self.addTask(( RegexTaggerTask(name="Regex2 Tagger"), {"input":[
                                                                {
                                                                    "key": "json-loader",
                                                                    "source": "internal-output",
                                                                    "map-key": "data"
                                                                },
                                                                {
                                                                    "key": "patterns",
                                                                    "source":"remote-json",
                                                                    "map-key": "patterns",
                                                                    "remote_source": "https://gist.githubusercontent.com/domenicosolazzo/a8dbbd953b70364a7c491c134dc96056/raw/18623f09f3627716f701abd09eec9bb2219e34db/JSON2"}
                                                            ],
                                                            "output": {"key":"regex2", "source": "internal-output", "type": "json" }
                                                          } ))
        self.addTask(( RegexTaggerMixerTask(name="Regex Mixer Tagger"), {"input":[
                                                                {"key": "regex", "source": "internal-output", "map-key": "regex"},
                                                                {"key": "regex2",  "source": "internal-output", "map-key": "regex2"}
                                                            ],
                                                            "output": {"key":"final regex", "source": "internal-output", "type": "json" }
                                                          } ))




    def execute(self):
        super(RegexTaggerPipeline, self).execute()
