import re

class RegexTagger(object):
    __regex_sentence = r'((?<=[^\w\s])\w(?=[^\w\s])|(\w+#)|((\w*)(-|/)(SQL))|(\W))+'
    def __init__(self, json, optionals={}):
        """
        RegexTagger
        """
        if json is not None:
            self.initialize(json, optionals)

    def initialize(self, data, optionals):
        """
        Initialize the RegexTagger
        """
        from nltk import RegexpTagger
        from nltk.tokenize import RegexpTokenizer

        json = data
        self.__gaps = True
        if not 'entities' in json:
            raise Exception("The entities' file for the RegexTagger is invalid")
        # Take the additional tags
        additional_tags = json.get('additional_tags', [])

        jsonEntities = []
        jsonEntities = json.get('entities', [])
        patterns=[]
        for item in jsonEntities:
            tags = []

            tags = item.get('tags', [])
            if len(additional_tags) > 0:
                tags.extend(additional_tags)
            tags = list(set(tags))
            tags = [tag.upper() for tag in tags]

            pattern_tags = ";".join(tags)
            entity = r'%s' % item.get('entity', '')
            patterns.append( (re.compile( entity, re.IGNORECASE ), pattern_tags) )

        self.tagger = nltk.RegexpTagger(patterns)
        if 'regex_sentence' in optionals:
            self.__regex_sentence = optionals.get('regex_sentence', self.__regex_sentence)
        if 'gaps' in optionals:
            self.__gaps = optionals.get('gaps', True)

        self.__tokenizer = RegexpTokenizer(self.__regex_sentence, gaps=self.__gaps)


    def getEntities(self, text):
        from nltk import sent_tokenize
        
        segmented_lines=nltk.sent_tokenize(text)
        for line in segmented_lines:
            words = self.__tokenizer.tokenize(line)
            tags = self.tagger.tag(words)
            entities = [ dict([("entity", w[0]), ("tags", sorted(w[1].split(";")))]) for w in tags if not w[1] is None ]

            return entities
