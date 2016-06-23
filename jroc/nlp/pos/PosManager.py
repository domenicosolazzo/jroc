# List of Pos tagger
POS_TAGGERS = { "no" : OBTManager,
                "nn" : OBTManager,
                "nb" : OBTManager,
                "da" : OBTManager,
                "sv" : OBTManager
                "other": None}

class PosManager(object):
    __language = None
    __posTagger = None
    def __init__(self, language="en"):
        self.__language = language

    def getPosInstance(self, data):
        taggerClass = POS_TAGGERS.get(self.__language, None)
        if taggerClass is None:
            pass # Activate a default tagger
        else:
            tagger = taggerClass(data)
        return tagger

    def analyze(self, inputData):
        """
        Analyze the text and return a PosResult
        """
        data = inputData
        # Get the right instance of the pos tagger
        self.__posTagger = self.getPosInstance(data)

        # Analyze the data and return a PosResult
        posResult = self.__posTagger.analyze()

        return posResult
