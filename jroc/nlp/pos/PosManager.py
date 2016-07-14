from . import OBTManager
from . import NTLKPosTagger

# List of Pos tagger
POS_TAGGERS = { "no" : OBTManager,
                "nn" : OBTManager,
                "nb" : OBTManager,
                "da" : OBTManager,
                "sv" : OBTManager,
                "en" : NTLKPosTagger,
                "other": None}

class PosManager(object):
    """
    It select the right pos tagger based on the language
    """
    __language = None
    __posTagger = None
    def __init__(self, language="en"):
        self.__language = language

    def getPosInstance(self, data):
        taggerClass = POS_TAGGERS.get(self.__language, None)
        if taggerClass is None:

            raise Exception("Pos tagger not available for this language: %s" % (self.__language, ) ) # Activate a default tagger
        else:
            tagger = taggerClass(data)
        return tagger

    def analyze(self, input):
        """
        Analyze the text and return a PosResult
        """
        data = input
        # Get the right instance of the pos tagger
        self.__posTagger = self.getPosInstance(data)

        # Analyze the data and return a PosResult
        posResult = self.__posTagger.analyze()

        return posResult
