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
            filename = "%s/../../../temp/TEXTFILE_%s" % (currentDirectory, int(time.time()), )
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

    def analyzeText(self):
        if self._outputData:
            return self._outputData
        currentDirectory = os.path.dirname(os.path.realpath(__file__))
        output_filename = "%s_OUTPUT" % (self._filename,)
        tagger_type = os.environ.get('OBT_TYPE', 'tag-bm.sh')
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
               new_obj["is_number"] = self.__isNumber(tagging)
        if self._deleteFiles:
            self.__deleteFile(self._filename)
            self.__deleteFile(output_filename)

        self._outputData = result
        return result

    def findTags(self):
        obtData = self._outputData
        if not obtData:
            obtData = self.analyzeText()
        unique_tags = set([tag.get("word") for tag in obtData if tag.get("is_prop") == True and tag.get("is_subst") == True])
        return list(unique_tags)

    def findEntities(self):
        data = self._outputData
        if not data:
            data = self.analyzeText()

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
