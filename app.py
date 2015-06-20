from flask import Flask, Response, request, jsonify
import traceback
import sys
import os
import json
import re
import time


regex = re.compile("<word>(?P<w>(.*?))</word>")
regex2 = re.compile("\"<(?P<w>[\w+]*)>\"")


# Flask app
app = Flask(__name__)

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

def analyze_text(filename):
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

    deleteFile(filename)
    deleteFile(output_filename)
    return result

def deleteFile(filename):
    try:
        os.remove(filename)
        return True
    except:
        raise

def fetchEntities(data):
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
        obt_json_result = json.dumps(obt_result)
        return Response(obt_json_result, mimetype="application/json")
    except Exception as e:
        ex_value = traceback.format_exception(*sys.exc_info())
        return jsonify(errors = ex_value)


@app.route('/demo')
def demo():
    obt_result = analyze_text("TEXTFILE")
    obt_json_result = json.dumps(obt_result)
    return Response(obt_json_result, mimetype="application/json")

@app.route('/tags', methods=["POST"])
def tags():
    try:
      json_result = json.loads(request.data)
      filename = saveContent(json_result)
      obt_result = analyze_text(filename)
      unique_tags = set([tag.get("word") for tag in obt_result if tag.get("is_prop") == True and tag.get("is_subst") == True])
      data_result = {"tags": list(unique_tags), "entities":fetchEntities(obt_result)}
      obt_json_result = json.dumps(data_result)
      return Response(obt_json_result, mimetype="application/json")
    except Exception as e:
        ex_value = traceback.format_exception(*sys.exc_info())
        return jsonify(errors = ex_value)

if __name__ == '__main__':
   app.debug = True
   app.run()
