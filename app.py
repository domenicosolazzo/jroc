from flask import Flask
import os
import json
import re
from flask import Response

regex = re.compile("<word>(?P<w>(.*?))</word>")
regex2 = re.compile("\"<(?P<w>[\w+]*)>\"")
app = Flask(__name__)

@app.route('/')
def hello_world():
    os.system('The-Oslo-Bergen-Tagger/tag-bm.sh TEXTFILE > OUTPUT')
    file_object = open('OUTPUT', 'r')
    text = file_object.read()
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
    json_result = json.dumps(result)
    return Response(json_result, mimetype='application/json')

if __name__ == '__main__':
   app.debug = True
   app.run()
