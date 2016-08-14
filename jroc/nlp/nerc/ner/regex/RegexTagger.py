import nltk
from nltk.tokenize import RegexpTokenizer

class RegexTagger(object):

    def __init__(self, patterns):
        self.tagger = nltk.RegexpTagger(patterns)

    def getEntities(self, text):
        segmented_lines=nltk.sent_tokenize(given_text)
        tags = default_tagger.tag(words)
        entities = [ dict(("entity", w[0]), ("tags", w[1].split(";"))) for w in tags if not w[1] is None ]
        return entities
