from flask import Flask, Response, request, jsonify
import traceback
import sys
import os
import json
import re
import time
from SPARQLWrapper import SPARQLWrapper, JSON


regex = re.compile("<word>(?P<w>(.*?))</word>")
regex2 = re.compile("\"<(?P<w>[\w+]*)>\"")


# Flask app
app = Flask(__name__)

def findSPARQLUri(entity):
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    sparql.setQuery("""
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX foaf: <http://xmlns.com/foaf/0.1/>
        PREFIX dbo: <http://dbpedia.org/ontology/>

        SELECT ?s WHERE {
          {
            ?s rdfs:label "%s"@en ;
               a owl:Thing .
          }
          UNION
          {
            ?altName rdfs:label "%s"@en ;
                     dbo:wikiPageRedirects ?s .
          }
        }
    """ % (entity, entity))
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    bindings = results["results"]["bindings"]

    uri = ""
    if len(bindings) > 0:
        uri = bindings[0]["s"]["value"]
    data = {
        "uri": uri
    }
    return data

def executeSPARQLQuery(entity):
    name = entity.strip().replace(" ", "_")
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    sparql.setQuery("""
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        SELECT ?comment, ?label, ?thumbnail, ?abstract, ?name
        WHERE {
          <http://dbpedia.org/resource/%s>  rdfs:label ?label; rdfs:comment ?comment; dbpedia-owl:thumbnail ?thumbnail; dbpedia-owl:abstract ?abstract; foaf:name ?name .
          FILTER(langMatches(lang(?name), "EN"))
          FILTER(langMatches(lang(?comment), "EN"))
          FILTER(langMatches(lang(?abstract), "EN"))
          FILTER(langMatches(lang(?label), "EN"))
        }
        LIMIT 5
    """ %(entity.strip().replace(" ", "_"),))
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    bindings = results["results"]["bindings"]


    data = {
        name: bindings
    }
    return data

def saveContent(json_data):
    try:
        if not isinstance(json_data, dict) or not 'data' in json_data.keys():
            raise Exception("Invalid data in input")

        data = json_data.get('data')

        filename = "TEXTFILE_%s" % (int(time.time()), )
        print(filename)
        file = open(filename,'w')
        file.write(data.encode('utf8'))
        file.close()
        return filename
    except:
        raise

def analyze_text(filename, delete_files=True):
    output_filename = "%s_OUTPUT" % (filename,)

    os.system('The-Oslo-Bergen-Tagger/tag-bm.sh %s > %s' % (filename, output_filename))
    file_object = open(output_filename, 'r')
    text = file_object.read().decode('utf8')
    text = text.split("\n")
    result = []
    new_obj = {}
    for word in text:
        if not word:
           continue
        is_match = regex.match(word)
        if regex.match(word):
            new_obj = {"word": is_match.groups(0)[0]}
            result.append(new_obj)
        elif regex2.match(word.lower()):
           continue
        else:
           word = word.replace("\"", "").replace("\t", "")
           tagging = [w for w in word.split(" ") if w]

           new_obj["tagging"] = tagging
           new_obj["options"] = word
           new_obj["is_verb"] = True if len([tag for tag in tagging if tag == 'verb']) > 0 else False
           new_obj["is_subst"] = True if len([tag for tag in tagging if tag == 'subst']) > 0 else False
           new_obj["is_prop"] = True if len([tag for tag in tagging if tag == 'prop']) > 0 else False
           new_obj["is_number"] = isNumber(tagging)
    if delete_files:
        deleteFile(filename)
        deleteFile(output_filename)
    return result

def deleteFile(filename):
    try:
        os.remove(filename)
        return True
    except:
        raise

def findEntities(data):
    entities = []
    last_entity = ""
    for entity in data:
        if (entity.get("is_prop") == True and entity.get("is_subst") == True) or (entity.get("is_number").get('roman') == True):
            if last_entity is "":
                last_entity = entity.get("word")
            else:
                last_entity = "%s %s" % (last_entity, entity.get("word"))
        elif last_entity is not "":
            entities.append(last_entity)
            last_entity = ""
    entities = list(set(entities))
    return entities

def entityExtraction(entities):
    data = []
    for entity in entities:
        sparqlEntity = executeSPARQLQuery(entity)
        uri = findSPARQLUri(entity)
        print(uri)
        data.append({"name": entity, "sparql": sparqlEntity})
    return data

def findTags(obt_data):
    unique_tags = set([tag.get("word") for tag in obt_data if tag.get("is_prop") == True and tag.get("is_subst") == True])
    return list(unique_tags)

def isNumber(tagging):
    is_quantity =  True if len([tag for tag in tagging if tag == 'kvant']) > 0 else False
    is_ordinal = True if len([tag for tag in tagging if tag == '<ordenstall>']) > 0 else False
    is_roman = True if len([tag for tag in tagging if tag == '<romertall>']) > 0 else False
    is_number  = True if is_quantity or is_ordinal or is_roman else False
    return {
        "is_number": is_number,
        "quantity": is_quantity,
        "ordinal": is_ordinal,
        "roman": is_roman
    }



@app.route('/')
def index():
    return jsonify({"welcome":"Welcome to OBT Api"})

@app.route('/analyze', methods=["POST"])
def analyze():
    try:
        json_result = json.loads(request.data)
        filename = saveContent(json_result)
        obt_result = analyze_text(filename)
        tags = findTags(obt_result)
        entities = findEntities(obt_result)

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
      filename = saveContent(json_result)
      obt_result = analyze_text(filename)

      tags = findTags(obt_result)
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
      filename = saveContent(json_result)
      obt_result = analyze_text(filename)

      entities = findEntities(obt_result)
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
      filename = saveContent(json_result)
      obt_result = analyze_text(filename)

      entities = findEntities(obt_result)
      sparqlEntities = entityExtraction(entities);

      data_result = {"entities": entities, "sparql": sparqlEntities }

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
    obt_result = analyze_text("TEXTFILE", delete_files=False)
    tags = findTags(obt_result)
    entities = findEntities(obt_result)

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
      obt_result = analyze_text("TEXTFILE", delete_files=False)

      tags = findTags(obt_result)
      data_result = {"tags": tags}

      obt_json_result = json.dumps(data_result)
      return Response(obt_json_result, mimetype="application/json")
    except Exception as e:
        ex_value = traceback.format_exception(*sys.exc_info())
        return jsonify(errors = ex_value)

@app.route('/demo/entities')
def demo_entities():
    try:
      obt_result = analyze_text("TEXTFILE", delete_files=False)

      entities = findEntities(obt_result)
      data_result = {"entities": entities}

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
