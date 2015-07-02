from . import tagger
from flask import request, Response
from obt import OBTManager
import json

@tagger.route("/")
def taggerMain():
    uris = {
        "tags": "/tags",
        "entities": "/entities"
    }
    json_response = json.dumps(uris)
    return Response(json_response, mimetype="application/json")

@tagger.route("/tags", methods=["POST"])
def taggerTags():
    tags = {}


    json_result = json.loads(request.data)
    obtManager = OBTManager(json_result)

    tags = obtManager.findTags()

    data = {}
    data["uri"] = "%s" % (request.base_url, )
    data["data"] = tags

    json_response = json.dumps(data)
    return Response(json_response, mimetype="application/json")

@tagger.route("/entities", methods=["POST"])
def taggerEntities():
    json_result = json.loads(request.data)
    obtManager = OBTManager(json_result)

    entities = obtManager.findEntities()
    is_advanced = request.args.get("advanced")
    if is_advanced:
        temp = []
        for entity in entities:
            temp.append({
                "name": entity,
                "uri": "%sentities/%s"  % (request.url_root, entity.replace(" ", "_"))
            })
        entities = temp

    data = {}
    data["uri"] = "%s" % (request.base_url, )
    data["data"] = entities
    json_response = json.dumps(data)
    return Response(json_response, mimetype="application/json")

@tagger.route("/analyze", methods=["POST"])
def taggerAnalyze():
    json_result = json.loads(request.data)
    obtManager = OBTManager(json_result)

    obt_result = obtManager.analyzeText()
    tags = obtManager.findTags()
    entities = obtManager.findEntities()

    result = {}
    result["uri"] = "%s" % (request.base_url, )

    data = {}
    data["obt"] = obt_result
    data["tags"] = tags
    data["entities"] = entities

    result["data"] = data
    json_response = json.dumps(result)

    return Response(json_response, mimetype="application/json")
