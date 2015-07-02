from . import entities
from flask import request, Response, jsonify
from linkeddata.SPARQL import SPARQLAdapter
from werkzeug.exceptions import HTTPException
import urllib2
import json

@entities.route('/search')
def search():
    return "ciao"

@entities.route("/")
def main():
    uris = {
        "uri" : "%s" % (request.base_url,)
    }

    json_response = json.dumps(uris)
    return Response(json_response, mimetype="application/json")

@entities.route("/<entity_name>")
def entityMain(entity_name):
    basic_url = "%s" % (request.base_url)
    entity = {}
    sparqlAdapter = SPARQLAdapter()
    uniqueUri = sparqlAdapter.getUniqueURI(entity_name).get('uri')
    entityName = entity_name

    if uniqueUri:
        uniqueName = uniqueUri.replace("http://dbpedia.org/resource/", "")
        basic_url = "%sentities/%s" % (request.url_root, uniqueName)
        entityName = uniqueName
        entity["redirected_from"] = request.base_url

    entity["name"] = entityName
    entity["types_uri"] = "%s/%s" % (basic_url, "types")
    entity["properties_uri"] = "%s/%s" %  (basic_url, "properties")
    result = {
        "data": entity,
        "uri": basic_url
    }
    json_response = json.dumps(result)
    return Response(json_response, mimetype="application/json")

@entities.route("/<entity_name>/types")
def entityTypes(entity_name):
    sparqlAdapter = SPARQLAdapter()
    result = sparqlAdapter.getEntityType(entity_name)

    entity = {}
    entity["name"] = entity_name
    entity["uri"] = "%s" % (request.base_url)
    entity["entity_uri"] = "%sentities/%s" % (request.url_root, entity_name,)
    entity["data"] = result
    json_response = json.dumps(entity)
    return Response(json_response, mimetype="application/json")

@entities.route("/<entity_name>/properties")
def entityProperties(entity_name):
    entity = {}
    entity["name"] = entity_name
    entity["uri"] = "%s" % (request.url)
    entity["entity_uri"] = "%sentities/%s" % (request.url_root, entity_name,)

    sparqlAdapter = SPARQLAdapter()
    if request.args.get('name'):
        propertyName = request.args.get('name')
        lang = request.args.get('lang') if request.args.get('lang') else None
        result = sparqlAdapter.getProperty(entity_name, urllib2.unquote(propertyName).decode('utf8'), lang)
        if len(result) > 0:
            result = result.get('properties')
        entity["data"] = result
    else:
        sparqlResult = sparqlAdapter.getProperties(entity_name)
        properties = sparqlResult.get("properties") if "properties" in sparqlResult else []
        result = {}
        for propertyName in properties.keys():
            prop = {'uri': "", "name": propertyName}
            if not propertyName in result:
                result[propertyName] = prop
            prop["uri"] = "%s?name=%s" % (request.base_url, urllib2.quote(propertyName))
            result[propertyName] = prop
        entity["data"] = result

    json_response = json.dumps(entity)
    return Response(json_response, mimetype="application/json")
