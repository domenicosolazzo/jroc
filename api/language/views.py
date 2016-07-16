# -*- coding: utf-8 -*-

from . import language
from flask import request, Response
from api.utils.input import DataCleaner
from jroc.pipelines.language.LanguageDetectionPipeline import LanguageDetectionPipeline
import json

@language.route("/detect", methods=["POST"])
def languageDetection():
    data = request.data

    pipeline = LanguageDetectionPipeline(input=data, name="Language detection pipeline")
    pipeline.execute()

    output = pipeline.getOutput()
    # Cleaning the input data
    #dataCleaner = DataCleaner()
    #data = dataCleaner.filterCharacters(data)

    # TODO: Add check if the data is in json
    #jsonData = json.loads(data)

    # TODO: Add check if the data key is present
    #text = jsonData.get("data", None)
    #languageResult = LanguageDetector().classify(text)
    language = output.get('language', None)
    result = {}
    result["language"] = language

    json_response = json.dumps(result)
    return Response(json_response, mimetype="application/json")
