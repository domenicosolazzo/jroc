
class BasicNER(object):
    """
    Basic Name Entity recognition
    """
    def __init__(self):
        pass

    def tags(self, posResult):
        """
        Find the tags within the text
        It takes all the words that are both "is_prop" and "is_subst"
        """
        data = posResult.posTags()
        for entity in data:
            if (entity.get("is_prop") == True and entity.get("is_subst") == True):
                entities.append(entity.get("word"))

        unique_tags = set(entities)
        return list(unique_tags)

    def entities(self, posResult):
        """
        Find the entities within the text
        """
        data = posResult.posTags()

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
