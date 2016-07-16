from SPARQLWrapper import SPARQLWrapper, JSON
from EntityDetector import EntityDetector
from queries import Queries

class SPARQLAdapter(object):

    def __init__(self):
        self.sparql = SPARQLWrapper("http://dbpedia.org/sparql")
        self.queries = Queries()

    def __prepareAndExecute(self, query, parameters):
        query = query % parameters
        result = self.__executeQuery(query)
        return result

    def __executeQuery(self, query, format=JSON):
        self.sparql.setQuery(query)
        self.sparql.setReturnFormat(JSON)
        results = self.sparql.query().convert()
        return results["results"]["bindings"]

    def __normalizeEntityName(self, entityName):
        if entityName is None:
            return ""
        return entityName.strip().replace(" ", "_")

    def getProperties(self, entityName, fetchValues=False):
        entityName = self.__normalizeEntityName(entityName)
        query = self.queries.QUERY_PROPERTIES_VALUES if fetchValues else self.queries.QUERY_PROPERTIES
        result = self.__prepareAndExecute(query, (entityName, ))

        properties = {}
        for prop in result:
            propertyName = prop["property"]["value"]
            if not propertyName in properties:
                properties[propertyName] = []
            if fetchValues:
                propertyValue = prop["propValue"]["value"]
                properties[propertyName].append(propertyValue)

        data = {
            "properties": properties
        }

        return data

    def getProperty(self, entityName, propertyValue, lang=None):
        entityName = self.__normalizeEntityName(entityName)
        query = self.queries.QUERY_PROPERTIES_VALUES_EXACT_MATCH_WITH_LANG if lang is not None else self.queries.QUERY_PROPERTIES_VALUES_EXACT_MATCH
        result = self.__prepareAndExecute(query, (entityName, propertyValue, lang)) if lang is not None else self.__prepareAndExecute(query, (entityName, propertyValue))

        properties = {}
        for prop in result:
            propertyName = prop["property"]["value"]
            if not propertyName in properties:
                properties[propertyName] = []
            propertyValue = prop["propValue"]["value"]

            properties[propertyName].append(propertyValue)


        data = {
            "properties": properties
        }

        return data

    def findDisambiguates(self, entityName):
        entityName = self.__normalizeEntityName(entityName)
        query = self.queries.QUERY_WIKI_PAGE_DISAMBIGUATES
        result = self.__prepareAndExecute(query, (entityName, entityName))

        uri_list = []
        if len(result) > 0:
            uri_list = [res["syn"]["value"] for res in result]
        data = {
            "synonyms": uri_list
        }
        return data

    def getThumbnail(self, entityName):
        entityName = self.__normalizeEntityName(entityName)
        query = self.queries.QUERY_THUMBNAIL
        result = self.__prepareAndExecute(query, (entityName, ))

        thumbnail = ""
        if len(result):
            thumbnail = result[0]["thumbnail"]["value"]

        data = {
            "thumbnail": thumbnail
        }
        return data

    def getUniqueURI(self, entityName):
        entityName = self.__normalizeEntityName(entityName)
        query = self.queries.QUERY_SPARQL_URI
        result = self.__prepareAndExecute(query, (entityName, entityName))

        uri = ""
        if len(result) > 0:
            uri = result[0]["s"]["value"]
        data = {
            "uri": uri
        }
        return data

    def getUniqueURIStartWith(self, entityName):
        entityName = entityName.strip().replace(" ", "_")
        query = self.queries.QUERY_SPARQL_URI_STARTWITH
        result = self.__prepareAndExecute(query, (entityName, ))

        uri = [u["uri"]["value"] for u in result]

        data = {
            "uri": uri
        }
        return data

    def getBasicInfo(self, entityName):
        entityName = entityName.strip().replace(" ", "_")
        query = self.queries.QUERY_BASIC_INFO
        result = self.__prepareAndExecute(query, (entityName, ))

        data = {
            "name": result
        }
        return data

    def getEntityTypes(self, entityName):
        entityName = self.__normalizeEntityName(entityName)
        query = self.queries.QUERY_ENTITY_TYPES
        result = self.__prepareAndExecute(query, (entityName, ) )

        entityTypes = [entityType["type"]["value"] for entityType in result]

        data = {
            "type": entityTypes
        }
        return data

    def getEntityType(self, entityName):
        entityName = self.__normalizeEntityName(entityName)
        types = self.getEntityTypes(entityName)

        entityDetector = EntityDetector()
        entityTypeResult = entityDetector.detect(types.get("type", []))

        result = {
            "entity_detection": entityTypeResult,
            "types": types
        }
        return result

    def entityExtraction(self, entity, advancedSearch=True):
        entity = self.__normalizeEntityName(entity)
        uri = self.getUniqueURI(entity)
        if uri.get('uri', None):
            entityName = uri.get('uri', None).replace("http://dbpedia.org/resource/", "")
        else:
            entityName =  entity.replace(" ", "_")

        entityData = {}
        types = self.getEntityTypes(entityName)
        if advancedSearch:
            entityData["info"] = self.getBasicInfo(entityName)
            entityData["synomyms"] = self.findDisambiguates(entityName)
            entityData["properties"] = self.getProperties(entityName, fetchValues=True)
            entityData["thumbnail"] = self.getThumbnail(entityName)
            entityData["types"] = self.getEntityTypes(entityName)
            entityData["type"] = self.getEntityType(entityName)

        entityType = self.getEntityType(entityName)

        entityData["entityType"] = entityType if advancedSearch and entityType is not None else entityType.get("type", None)

        entityData["name"] = entity
        entityData["entityName"] = entityName

        return entityData
