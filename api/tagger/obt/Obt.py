import sys
import os
import re
import time

class OBTManager(object):
    REGEX = re.compile("<word>(?P<w>(.*?))</word>")
    REGEX2 = re.compile("\"<(?P<w>[\w+]*)>\"")
    _outputData = None
    _filename = None
    _deleteFiles = True

    def __init__(self, data, filename=None, deleteFiles=True):
        self._filename = filename
        self._deleteFiles = deleteFiles
        if not self._filename:
            self._filename = self.__saveContent(data)
            print(self._filename)

        self._outputData = None

    def __deleteFile(self, filename):
        try:
            os.remove(filename)
            return True
        except:
            raise

    def __saveContent(self, data):
        try:
            if not isinstance(data, dict) or not 'data' in data.keys():
                raise Exception("Invalid data in input")

            data = data.get('data')

            currentDirectory = os.path.dirname(os.path.realpath(__file__))
            filename = "%s/../../../tmp/TEXTFILE_%s" % (currentDirectory, int(time.time()), )
            file = open(filename,'w+')
            file.write(data.encode('utf8'))
            file.close()
            return filename

        except:
            raise

    def __isNumber(self, tagging):
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

    def obtAnalyze(self):
        if self._outputData:
            return self._outputData
        currentDirectory = os.path.dirname(os.path.realpath(__file__))
        output_filename = "%s_OUTPUT" % (self._filename,)
        tagger_type = os.environ.get('OBT_TYPE', 'tag-nostat-bm.sh')
        os.system('%s/../../../The-Oslo-Bergen-Tagger/%s %s > %s' % (currentDirectory, tagger_type, self._filename, output_filename))
        file_object = open(output_filename, 'r')

        text = file_object.read().decode('utf8')
        text = text.split("\n")
        result = []
        new_obj = {}
        for word in text:
            if not word:
               continue
            is_match = self.REGEX.match(word)
            if self.REGEX.match(word):
                new_obj = {"word": is_match.groups(0)[0]}
                result.append(new_obj)
            elif self.REGEX2.match(word.lower()):
               continue
            else:
               word = word.replace("\"", "").replace("\t", "")
               tagging = [w for w in word.split(" ") if w]

               new_obj["tagging"] = tagging
               new_obj["options"] = word
               new_obj["is_verb"] = True if len([tag for tag in tagging if tag == 'verb']) > 0 else False
               new_obj["is_subst"] = True if len([tag for tag in tagging if tag == 'subst']) > 0 else False
               new_obj["is_prop"] = True if len([tag for tag in tagging if tag == 'prop']) > 0 else False
               new_obj["is_adj"] = True if len([tag for tag in tagging if tag == 'adj']) > 0 else False
               new_obj["is_conj"] = True if len([tag for tag in tagging if tag == 'konj']) > 0 else False
               new_obj["is_number"] = self.__isNumber(tagging)
               new_obj["is_unknown"] = True if len([tag for tag in tagging if tag == 'ukjent']) > 0 else False
               new_obj["is_det"] = True if len([tag for tag in tagging if tag == 'det']) > 0 else False
               new_obj["is_inf_merke"] = True if len([tag for tag in tagging if tag == 'inf-merke']) > 0 else False
               new_obj["is_sbu"] = True if len([tag for tag in tagging if tag == 'sub']) > 0 else False
               new_obj["is_interj"] = True if len([tag for tag in tagging if tag == 'interj']) > 0 else False

        if self._deleteFiles:
            self.__deleteFile(self._filename)
            self.__deleteFile(output_filename)

        self._outputData = result
        return result

    def findTags(self):
        obtData = self._outputData
        if not obtData:
            obtData = self.obtAnalyze()
        entities = []
        for entity in obtData:
            if (entity.get("is_prop") == True and entity.get("is_subst") == True):
                entities.append(entity.get("word"))

        unique_tags = set(entities)
        return list(unique_tags)

    def findEntities(self, stopwords=[]):
        data = self._outputData
        if not data:
            data = self.obtAnalyze()

        entities = []
        last_entity = ""
        for entity in data:
            word = entity.get("word")
            if len(stopwords) > 0 and word.lower() in stopwords:
                if last_entity is not "":
                    entities.append(last_entity)
                last_entity = ""
            elif (entity.get("is_prop") == True and entity.get("is_subst") == True) or (entity.get("is_number").get('roman') == True) or word.lower() == "as":
                if last_entity is "":
                    last_entity = word
                else:
                    last_entity = "%s %s" % (last_entity, word)
            elif last_entity is not "":
                entities.append(last_entity)
                last_entity = ""
        entities = list(set(entities))

        return entities

    def analyzeText(self):
        data = self.obtAnalyze()

        textAnalyze = {}

        verbs = list(set([unicode(tag.get("word")) for tag in data  if tag.get("is_verb") == True]))
        substs = list(set([unicode(tag.get("word")) for tag in data  if tag.get("is_subst") == True]))
        props = list(set([unicode(tag.get("word")) for tag in data  if tag.get("is_prop") == True]))
        numbers = list(set([unicode(tag.get("word")) for tag in data  if tag.get("is_number") == True]))
        adjs = list(set([unicode(tag.get("word")) for tag in data  if tag.get("is_adj") == True]))
        conjs = list(set([unicode(tag.get("word")) for tag in data  if tag.get("is_conj") == True]))
        unknowns = list(set([unicode(tag.get("word")) for tag in data  if tag.get("is_unknown") == True]))
        dets = list(set([unicode(tag.get("word")) for tag in data  if tag.get("is_det") == True]))
        inf_merks = list(set([unicode(tag.get("word")) for tag in data  if tag.get("is_inf_merke") == True]))
        sbus = list(set([unicode(tag.get("word")) for tag in data  if tag.get("is_sbu") == True]))
        interjs = list(set([unicode(tag.get("word")) for tag in data  if tag.get("is_interj") == True]))

        textAnalyze['verbs'] = verbs
        textAnalyze['substs'] = substs
        textAnalyze['props'] = props
        textAnalyze['numbers'] = numbers
        textAnalyze['adj'] = adjs
        textAnalyze['conjs'] = conjs
        textAnalyze['unknowns'] = unknowns
        textAnalyze['dets'] = dets
        textAnalyze['inf_merks'] = inf_merks
        textAnalyze['sbus'] = sbus
        textAnalyze['interjs'] = interjs

        return textAnalyze
