from . import tagger
from flask import request, Response
from obt import OBTManager
from stopwords import StopwordManager
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
    requestStopwords = True if request.args.get('stopwords') == 'true' else False
    tags = {}

    json_result = json.loads(request.data)
    obtManager = OBTManager(json_result)
    stopwordManager = StopwordManager()

    tags = obtManager.findTags()
    if requestStopwords == True:
        tags = stopwordManager.filterStopWords(tags)

    data = {}
    data["uri"] = "%s" % (request.base_url, )
    data["data"] = tags

    json_response = json.dumps(data)
    return Response(json_response, mimetype="application/json")

@tagger.route("/entities", methods=["POST"])
def taggerEntities():

    requestStopwords = True if request.args.get('stopwords') == 'true' else False

    data = request.data
    data = data.replace("'","\"")
    json_result = json.loads(data)
    obtManager = OBTManager(json_result)
    stopwordManager = StopwordManager()

    entities = obtManager.findEntities()
    if requestStopwords == True:
        entities = stopwordManager.filterStopWords(entities)

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
    requestObt = True if request.args.get('obt') == 'true' else False
    requestEntities = True if request.args.get('entities') == 'true' else False
    requestTags = True if request.args.get('tags') == 'true' else False

    json_result = json.loads(request.data)
    obtManager = OBTManager(json_result)

    result = {}
    result["uri"] = "%s" % (request.base_url, )

    data = {}
    if(requestObt == True):
        obt_result = obtManager.obtAnalyze()
        data["obt"] = obt_result

    if(requestTags == True):
        tags = obtManager.findTags()
        data["tags"] = tags

    if(requestEntities == True):
        entities = obtManager.findEntities()
        data["entities"] = entities

    text_analyze_result = obtManager.analyzeText()
    data["text_analyze"] = text_analyze_result
    result["data"] = data

    json_response = json.dumps(result)

    return Response(json_response, mimetype="application/json")
