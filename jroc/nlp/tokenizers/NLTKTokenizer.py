from nltk.tokenize import sent_tokenize, word_tokenize
import nltk.data
AVAILABLE_LANGUAGES = dict([
    ('cs', 'czech'), ('da', 'danish'), ('nl', 'dutch'), ('en', 'english'), ('et', 'estonian'),
    ('fi', 'finnish'),('fr', 'french'), ('de', 'german'), ('el', 'greek'), ('it', 'italian'),
    ('no', 'norwegian'), ('nn', 'norwegian'), ('nb', 'norwegian'), ('pl', 'polish'),
    ('pt', 'portuguese'), ('sl', 'slovene'), ('es', 'spanish'), ('sv', 'swedish'), ('tr', 'turkish')
])

class NLTKTokenizer(object):
    """
    It select the right pos tagger based on the language
    """
    __tokenizer = None
    def __init__(self, language="en"):
        self.__tokenizer = self.__loadTokenizer(language)

    def __loadTokenizer(self, language_code="en"):
        """
        Load the tokenizer for a given language. Default is English
        """
        languagePicklePath = "tokenizers/punkt/%s.pickle" % AVAILABLE_LANGUAGES.get(language_code, "en")
        tokenizer = nltk.data.load(languagePicklePath)
        return tokenizer

    def tokenizeText(self, text):
        """
        Tokenize a particular text
        """
        if not isinstance(text, unicode):
            text = text.decode('utf8')
        return self.__tokenizer.tokenize(text)

    def tokenizeSentence(self, sentence):
        """
        Tokenize a sentence in words
        """
        return word_tokenize(sentence)
