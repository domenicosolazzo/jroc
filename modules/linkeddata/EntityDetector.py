import EntityTypes
class EntityDetector(object):

    def __init__(self):
        pass

    def detect(types):
        entityType = {
            "is_person": False,
            "is_org": False,
            "is_event": False,
            "is_work": False,
            "is_location": False,
            "other": False,
            "type": "other"
        }

        if not set(types).isdisjoint(EntityTypes.PERSON):
            entityType["is_person"] = True
            entityType["type"] = "Person"
            return entityType

        return None
