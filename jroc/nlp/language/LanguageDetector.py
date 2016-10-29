import langid

class LanguageDetector(object):
    def __init__(self):
        pass

    def classify(self, text):
        """
        Detect the language of a given text
        @param: text to be classified
        """
        return langid.classify(text)
