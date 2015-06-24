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
            "type": "Other"
        }

        if not set(types).isdisjoint(EntityTypes.PERSON):
            entityType["is_person"] = True
            entityType["type"] = "Person"
            return entityType

        if not set(types).isdisjoint(EntityTypes.ORGANIZATION):
            entityType["is_org"] = True
            entityType["type"] = "Organization"
            return entityType

        if not set(types).isdisjoint(EntityTypes.EVENT):
            entityType["is_event"] = True
            entityType["type"] = "Event"
            return entityType

        if not set(types).isdisjoint(EntityTypes.LOCATION):
            entityType["is_location"] = True
            entityType["type"] = "Location"
            return entityType

        entityType["Other"] = True
        return entityType
