# -*- coding: utf-8 -*-
from flask import request, Response
from jroc.pipelines.language.LanguageDetectionPipeline import LanguageDetectionPipeline
import json

@language.route("/detect", methods=["POST"])
def languageDetection():
    data = request.data

    # Loading a language pipeline
    pipeline = LanguageDetectionPipeline(input=data, name="Language detection pipeline")
    pipeline.execute()

    output = pipeline.getOutput()

    language = output.get('language', None)
    result = {}
    result["language"] = language

    json_response = json.dumps(result)
    return Response(json_response, mimetype="application/json")
