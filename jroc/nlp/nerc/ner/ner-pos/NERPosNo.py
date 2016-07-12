
class NERPosNo(object):

    def __init__(self):
        pass

    def findNER(self, textAnalysis, stopwords=[]):
        assert(isinstance(textAnalysis, dict))
        assert('obt' in textAnalysis)

        data = textAnalysis.get('obt')

        entities = []
        last_entity = ""
        for entity in data:
            word = entity.get("word")
            if len(stopwords) > 0 and word.lower() in stopwords:
                if last_entity is not "":
                    entities.append(last_entity)
                last_entity = ""
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
