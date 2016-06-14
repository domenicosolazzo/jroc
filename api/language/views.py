# -*- coding: utf-8 -*-

from . import language
from flask import request, Response
from api.utils.input import DataCleaner
from api.language.detector import LanguageDetector
import json

@language.route("/detect", methods=["POST"])
def languageDetection():
    data = request.data

    # Cleaning the input data
    dataCleaner = DataCleaner()
    data = dataCleaner.filterCharacters(data)

    # TODO: Add check if the data is in json
    jsonData = json.loads(data)

    # TODO: Add check if the data key is present
    text = jsonData.get("data", None)
    languageResult = LanguageDetector().classify(text)

    result = {}
    result["language"] = languageResult[0]
    result["estimate"] = languageResult[1]

    json_response = json.dumps(result)
    return Response(json_response, mimetype="application/json")
