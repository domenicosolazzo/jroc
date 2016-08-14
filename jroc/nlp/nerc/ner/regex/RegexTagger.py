import nltk
from nltk.tokenize import RegexpTokenizer
import re

class RegexTagger(object):
    __regex_sentence = r'((?<=[^\w\s])\w(?=[^\w\s])|(\w+#)|((\w*)(-|/)(SQL))|(\W))+'
    def __init__(self, json, regex_sentence=None, gaps=True):
        """
        RegexTagger
        """
        patterns = [(re.compile(r'Moody\'s',re.IGNORECASE), 'ORGANIZATION'),
            (re.compile(r'(Javascript|Java|C#|Python|(.*SQL))',re.IGNORECASE), 'LANGUAGE'),
            (re.compile(r'(tokyo|japan)',re.IGNORECASE), 'LOCATION'),
            (re.compile(r'(monday|tuesday|wednesday|thursday|friday|saturday|sunday)',re.IGNORECASE), 'DATE')]

        if not 'entities' in json:
            raise Exception("The entities' file for the RegexTagger is invalid")
        # Take the additional tags
        additional_tags = json.get('additional_tags', [])

        entities = json.get('entities', [])
        patterns=[]
        for item in entities:
            tags = item.get('tags', [])
            tags.extend(additional_tags)
            pattern_tags = ";".join(tags)
            entity = r'%s' % item.get('entity', '')
            patterns.append((re.compile(entity,re.IGNORECASE), pattern_tags))

        self.tagger = nltk.RegexpTagger(patterns)
        if not regex_sentence is None:
            self.__regex_sentence = regex_sentence
        self.__gaps = gaps
        self.__tokenizer = RegexpTokenizer(self.__regex_sentence, gaps=self.__gaps)

    def getEntities(self, text):
        segmented_lines=nltk.sent_tokenize(text)
        for line in segmented_lines:
            words = self.__tokenizer.tokenize(line)
            tags = self.tagger.tag(words)
            entities = [ dict([("entity", w[0]), ("tags", w[1].split(";"))]) for w in tags if not w[1] is None ]

            return entities
