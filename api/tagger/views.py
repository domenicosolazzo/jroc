# -*- coding: utf-8 -*-

from . import tagger
from flask import request, Response
from obt import OBTManager
from stopwords import StopwordManager
from api.utils.input import DataCleaner
from api.language.detector import LanguageDetector

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

    # Cleaning the input data
    dataCleaner = DataCleaner()
    data = dataCleaner.filterCharacters(data)

    json_result = json.loads(data)

    # Language Detection
    text = json_result.get("data", None)
    languageResult = LanguageDetector().classify(text)
    language = languageResult[0]

    # Oslo-Bergen Tagger
    obtManager = OBTManager(json_result)

    tags = {}

    # Find the tags
    tags = obtManager.findTags()
    if shouldFilterStopwords == True:
        # Applying the stopwords
        stopwordManager = StopwordManager(language=language)
        tags = stopwordManager.filterStopWords(tags)

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
    showAdvancedResult = True if request.args.get("advanced") else False

    data = request.data

    # Cleaning the data in input
    dataCleaner = DataCleaner()
    data = dataCleaner.filterCharacters(data)

    json_result = json.loads(data)

    # Language Detection
    text = json_result.get("data", None)
    languageResult = LanguageDetector().classify(text)
    language = languageResult[0]

    # Oslo-Bergen Tagger
    obtManager = OBTManager(json_result)

    # Applying the stopwords
    stopwordManager = StopwordManager(language=language)
    stopwords = stopwordManager.getStopWords() if shouldFilterStopwords == True else []
    entities = obtManager.findEntities(stopwords=stopwords)

    if showAdvancedResult and len(entities) > 0:
        # Advanced formatting for each entity
        temp = []
        for entity in entities:
            temp.append({
                "name": entity,
                "uri": "%sentities/%s"  % (request.url_root, entity.replace(" ", "_"))
            })
        entities = temp

    result = {}
    result["uri"] = "%s" % (request.base_url, )
    result["data"] = entities
    result["meta"] = {}
    if shouldShowLanguage == True:
        result["meta"]["language"] = languageResult[0]

    json_response = json.dumps(result)
    return Response(json_response, mimetype="application/json")

@tagger.route("/analyze", methods=["POST"])
def taggerAnalyze():
    requestObt = True if request.args.get('obt') == 'true' else False
    requestEntities = True if request.args.get('entities') == 'true' else False
    requestTags = True if request.args.get('tags') == 'true' else False

    data = request.data
    data = data.replace("'","\"").replace("\n", "")
    json_result = json.loads(data)
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
