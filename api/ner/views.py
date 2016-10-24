# -*- coding: utf-8 -*-

from . import ner
from flask import request, Response
from jroc.pipelines.ner.NERPipeline import NERPipeline
import json


@ner.route("/analyze", methods=["POST"])
def nerDetection():
    data = request.data

    # Loading a language pipeline
    pipeline = NERPipeline(input=data, name="NER Detection pipeline")
    pipeline.execute()

    output = pipeline.getOutput()

    entities = output.get('entities', [])
    stanford = output.get('entities-stanford', [])
    result = {}
    result['entities'] = entities
    result['entities-stanford'] = stanford
    from sets import Set
    stanford_set = Set([entity[0] for index, entity in enumerate(stanford)])
    entities_set = Set(entities)

    difference = entities_set.difference_update(stanford_set)

    if len(stanford) > 0:
        temp = {}
        temp['OTHERS'] = list(entities_set)
        for index, entity in enumerate(stanford):
            entityType = entity[1]
            entityName = entity[0]
            if entityType in temp:
                if not entityName in temp[entityType]:
                    temp[entityType].append(entityName)
            else:
                temp[entityType] = [entityName]

        result['entities-by-type'] = temp

    #result["language"] = languageDetection

    json_response = json.dumps(result)
    return Response(json_response, mimetype="application/json")
