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

    deleteFile(filename)
    deleteFile(output_filename)
    return result

def deleteFile(filename):
    try:
        os.remove(filename)
        return True
    except:
        raise

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


@app.route('/last')
def last():
    result = analyze_text("TEXTFILE")
    obt_json_result = json.dumps(obt_result)
    return Response(obt_json_result, mimetype="application/json")


if __name__ == '__main__':
   app.debug = True
   app.run()
