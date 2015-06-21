from flask import Flask, Response, request, jsonify
import traceback
import sys
import json
from modules.tagger.Obt import OBTManager

# Flask app
app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({
        "welcome":"Welcome to OBT Api",
        "api":{
            "analyze": "/analyze",
            "tags": "/tags",
            "entities": "/entities",
            "ee": "/ee",
            "demo":{
                "base": "/demo",
                "analyze": "/demo/analyze",
                "entities": "/demo/entities",
                "ee": "/demo/ee",
                "tags": "/demo/tags",
                "text": "/demo/text"
            }
        }

    })

@app.route('/analyze', methods=["POST"])
def analyze():
    try:
        json_result = json.loads(request.data)
        obtManager = OBTManager(json_result)

        obt_result = obtManager.analyzeText()
        tags = obtManager.findTags()
        entities = obtManager.findEntities()

        data_result = {
            "obt": obt_result,
            "tags": tags,
            "entities": entities
        }

        obt_json_result = json.dumps(data_result)
        return Response(obt_json_result, mimetype="application/json")
    except Exception as e:
        ex_value = traceback.format_exception(*sys.exc_info())
        return jsonify(errors = ex_value)

@app.route('/tags', methods=["POST"])
def tags():
    try:
      json_result = json.loads(request.data)
      obtManager = OBTManager(json_result)
      tags = obtManager.findTags()
      data_result = {"tags": tags}

      obt_json_result = json.dumps(data_result)
      return Response(obt_json_result, mimetype="application/json")
    except Exception as e:
        ex_value = traceback.format_exception(*sys.exc_info())
        return jsonify(errors = ex_value)

@app.route('/entities', methods=["POST"])
def entities():
    try:
      json_result = json.loads(request.data)
      obtManager = OBTManager(json_result)
      entities =  obtManager.findEntities()

      data_result = {"entities": entities}

      obt_json_result = json.dumps(data_result)
      return Response(obt_json_result, mimetype="application/json")
    except Exception as e:
        ex_value = traceback.format_exception(*sys.exc_info())
        return jsonify(errors = ex_value)

@app.route('/ee', methods=["POST"])
def ee():
    try:
      json_result = json.loads(request.data)
      obtManager = OBTManager(json_result)
      data_result = obtManager.entityExtraction();

      obt_json_result = json.dumps(data_result)
      return Response(obt_json_result, mimetype="application/json")
    except Exception as e:
        ex_value = traceback.format_exception(*sys.exc_info())
        return jsonify(errors = ex_value)

@app.route('/demo')
def demo():
    result = {
        "text": "/demo/text",
        "analyze": "/demo/analyze",
        "entities": "/demo/entities",
        "tags": "/demo/tags"
    }
    return jsonify(result)

@app.route('/demo/analyze')
def demo_analyze():
    obtManager = OBTManager(None, filename="TEXTFILE", deleteFiles=False)
    obt_result = obtManager.analyzeText()
    tags = obtManager.findTags()
    entities = obtManager.findEntities()

    data_result = {
        "obt": obt_result,
        "tags": tags,
        "entities": entities
    }

    obt_json_result = json.dumps(data_result)
    return Response(obt_json_result, mimetype="application/json")

@app.route('/demo/tags')
def demo_tags():
    try:
      obtManager = OBTManager(None, filename="TEXTFILE", deleteFiles=False)
      tags = obtManager.findTags()
      data_result = {
        "tags": tags
      }

      obt_json_result = json.dumps(data_result)
      return Response(obt_json_result, mimetype="application/json")
    except Exception as e:
        ex_value = traceback.format_exception(*sys.exc_info())
        return jsonify(errors = ex_value)

@app.route('/demo/entities')
def demo_entities():
    try:
      obtManager = OBTManager(None, filename="TEXTFILE", deleteFiles=False)
      entities = obtManager.findEntities()
      data_result = {
        "entities": entities
      }

      obt_json_result = json.dumps(data_result)
      return Response(obt_json_result, mimetype="application/json")
    except Exception as e:
        ex_value = traceback.format_exception(*sys.exc_info())
        return jsonify(errors = ex_value)

@app.route('/demo/ee')
def demo_ee():
    try:
      obtManager = OBTManager(None, filename="TEXTFILE", deleteFiles=False)
      data_result = obtManager.entityExtraction()

      obt_json_result = json.dumps(data_result)
      return Response(obt_json_result, mimetype="application/json")
    except Exception as e:
        ex_value = traceback.format_exception(*sys.exc_info())
        return jsonify(errors = ex_value)

@app.route('/demo/text')
def demo_text():
    try:
      file_object = open('TEXTFILE', 'r')
      text = file_object.read().decode('utf8')
      file_object.close()
      return Response(text)
    except Exception as e:
        ex_value = traceback.format_exception(*sys.exc_info())
        return jsonify(errors = ex_value)


if __name__ == '__main__':
   app.debug = True
   app.run()
