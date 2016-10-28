# -*- coding: utf-8 -*-

from . import ner
from flask import request, Response
from jroc.pipelines.ner.NERPipeline import NERPipeline
import json


@ner.route("/analyze", methods=["POST"])
def nerDetection():
    data = request.data

    # Loading a language pipeline
    pipeline = NERPipeline(input=data, name="NER Detection pipeline", withStanfordTagging=True, withNERFormatting=True)
    pipeline.execute()

    output = pipeline.getOutput()

    entities = output.get('entities-formatted', [])

    #result["language"] = languageDetection

    json_response = json.dumps(entities)
    return Response(json_response, mimetype="application/json")
