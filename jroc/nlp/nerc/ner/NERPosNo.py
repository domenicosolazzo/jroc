class NERPosNo(object):
    """
    This class returns a set of entities from the output of the Norwegian POS Tagger (OBT)
    TODO: To be deprecated
    """
    def __init__(self):
        pass

    def findNER(self, textAnalysis, stopwords=[]):
        """
        It returns entities from the text analysis performed by the POS Tagger (OBT)
        @textAnalysis: The text analysis performed by OBT
        @stopwords: List of stopwords.
        """
        assert(textAnalysis is not None)
        assert(isinstance(textAnalysis, dict))
        assert('obt' in textAnalysis)

        if stopwords is None or isinstance(stopwords, dict):
            stopwords = []

        data = textAnalysis.get('obt')


        entities = []
        last_entity = ""
        for entity in data:
            # Retrieve the next word
            word = entity.get("word")
            # If the word is a stopword, return the previous entity as entity.
            if len(stopwords) > 0 and word.lower() in stopwords:
                if last_entity is not "":
                    entities.append(last_entity)
                last_entity = ""
            # If the word is_prop and is_subst, or it is a roman number, or it is as (used for companies)
            elif (entity.get("is_prop") == True and entity.get("is_subst") == True) or (entity.get("is_number").get('roman') == True) or word.lower() == "as":
                if last_entity is "":
                    last_entity = word
                else:
                    last_entity = "%s %s" % (last_entity, word)
            elif last_entity is not "":
                entities.append(last_entity)
                last_entity = ""
        entities = list(set(entities))

        return entities
