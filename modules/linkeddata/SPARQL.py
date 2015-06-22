from SPARQLWrapper import SPARQLWrapper, JSON
from queries import Queries

class SPARQLAdapter(object):

    def __init__(self):
        print("Initializing the SPARQL Adapter")
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

    def getProperties(self, entityName, fetchValues=False):
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

    def findDisambiguates(self, entityName):
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
        query = self.queries.QUERY_SPARQL_URI_STARTWITH
        result = self.__prepareAndExecute(query, (entityName, entityName))

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
        query = self.queries.QUERY_ENTITY_TYPES
        result = self.__prepareAndExecute(query, (entityName, ) )

        entityTypes = [entityType["type"]["value"] for entityType in result]

        data = {
            "type": entityTypes
        }
        return data

    def entityExtraction(self, entity):
        uri = self.getUniqueURI(entity)
        if uri.get('uri', None):
            entityName = uri.get('uri', None).replace("http://dbpedia.org/resource/", "")
        else:
            entityName =  entity.replace(" ", "_")

        info = self.getBasicInfo(entityName)
        synomyms = self.findDisambiguates(entityName)
        properties = self.getProperties(entityName, fetchValues=True)
        thumbnail = self.getThumbnail(entityName)
        types = self.getEntityTypes(entityName)

        entityData = {
            "uri": uri.get("uri", None),
            "name": entity,
            "entityName": entityName,
            "info": info,
            "synonyms": synomyms.get("synonyms",[]),
            "properties": properties.get("properties"),
            "thumbnail": thumbnail.get("thumbnail", ""),
            "types": types.get("type")
        }

        return entityData
