# -*- coding: utf-8 -*-

from . import tagger
from flask import request, Response
from jroc.pipelines.ner.NERPipeline import NERPipeline
from jroc.pipelines.pos.PosTaggerPipeline import PosTaggerPipeline

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
    shouldFilterStopwords = True if request.args.get('stopwords') == 'true' else False
    shouldShowLanguage = True if request.args.get('language') == 'true' else False

    data = request.data

    pipeline = PosTaggerPipeline(input=data, name="PosTagger Pipeline")
    pipeline.execute()
    output = pipeline.getOutput()

    tags = output.get('tags', [])

    result = {}
    result["uri"] = "%s" % (request.base_url, )
    result["data"] = tags
    result["meta"] = {}
    if shouldShowLanguage == True:
        result["meta"]["language"] = languageResult[0]

    json_response = json.dumps(result)
    return Response(json_response, mimetype="application/json")

@tagger.route("/entities", methods=["POST"])
def taggerEntities():
    shouldFilterStopwords = True if request.args.get('stopwords') == 'true' else False
    shouldShowLanguage = True if request.args.get('language') == 'true' else False
    showAdvancedResult = True if request.args.get("advanced") == 'true' else False
    showCommonWords = True if request.args.get("common") == 'true' else False

    result = {}
    result["uri"] = "%s" % (request.base_url, )
    result["meta"] = {}
    result["data"] = {}

    data = request.data
    pipeline = NERPipeline(input=data, name="NER Pipeline", withEntityAnnotation=False)
    pipeline.execute()
    output = pipeline.getOutput()

    language = output.get('language', None)
    entities = output.get('entities-stanford', [])

    if showAdvancedResult and len(entities) > 0:
        # Advanced formatting for each entity
        temp = []
        for entity in entities:
            temp.append({
                "name": entity,
                "uri": "%sentities/%s"  % (request.url_root, entity.replace(" ", "_"))
            })
        entities = temp
    result["data"] = entities

    if showCommonWords == True:
        pos = output.get("pos", [])
        result["meta"]["common_words"] = output.get("common_words", [])

    if shouldShowLanguage == True:
        result["meta"]["language"] = language

    json_response = json.dumps(result)
    return Response(json_response, mimetype="application/json")

@tagger.route("/analyze", methods=["POST"])
def taggerAnalyze():
    shouldFilterStopwords = True if request.args.get('stopwords') == 'true' else False
    shouldShowLanguage = True if request.args.get('language') == 'true' else False
    showAdvancedResult = True if request.args.get("advanced") == 'true' else False
    showCommonWords = True if request.args.get("common") == 'true' else False
    rawOutput = True if request.args.get("raw") == 'true' else False

    result = {}
    result["uri"] = "%s" % (request.base_url, )
    result["data"] = {}
    result["meta"] = {}

    data = request.data
    pipeline = NERPipeline(input=data, name="NER Pipeline", withEntityAnnotation=False)

    pipeline.execute()
    output = pipeline.getOutput()

    if (rawOutput == True):
        json_response = json.dumps(output)
        return Response(json_response, mimetype="application/json")

    language = output.get('language', None)
    entities = output.get('entities', [])


    if showAdvancedResult and len(entities) > 0:
        # Advanced formatting for each entity
        temp = []
        for entity in entities:
            temp.append({
                "name": entity,
                "uri": "%sentities/%s"  % (request.url_root, entity.replace(" ", "_"))
            })
        entities = temp
    result["data"] = entities

    if showCommonWords == True:
        pos = output.get("pos", [])
        result["meta"]["common_words"] = pos.get("common_words", [])


    if shouldShowLanguage == True:
        result["meta"]["language"] = language


    json_response = json.dumps(result)
    return Response(json_response, mimetype="application/json")
