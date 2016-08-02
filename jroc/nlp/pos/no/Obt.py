# -*- coding: utf-8 -*-
import sys
import os
import re
import time
import codecs

class OBTManager(object):
    """
    This class takes care to analyze the text using the Oslo-Bergen Tagger
    """
    REGEX = re.compile("<word>(?P<w>(.*?))</word>")
    REGEX2 = re.compile("\"<(?P<w>[\w+]*)>\"")
    _outputData = None
    _filename = None
    _outputFilename = None
    _deleteFiles = True

    def __init__(self, data=None):
        #assert(isinstance(data, str))

        self._outputData = None
        # Check if the data is not empty
        if data is not None and (isinstance(data, str) or isinstance(data, unicode)):
            print("DATA", data)
            # Save the content in a temp file
            self.__saveContent(data)



    def __deleteFile(self, filename):
        if filename is not None:
            try:
                os.remove(filename)
                return True
            except:
                raise

    def __saveContent(self, data):
        """
        Save the content in a temporary file
        """
        #assert(isinstance(data, str))

        currentDirectory = os.path.dirname(os.path.realpath(__file__)) # Current directory
        filename = "%s/../../../../tmp/TEXTFILE_%s" % (currentDirectory, int(time.time()), )
        with codecs.open(filename, "w", encoding='utf-8') as file:
            if isinstance(data, str):
                data = data.decode('utf8')
            file.write(data)

        self._filename = filename

    def __isNumber(self, tagging):
        """
        Check if it is a number
        """
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

    def __getUniversalTag(self, taggingInfo):
        """
        Get the universal tag that can used between multiple taggers
        Based on this page: http://www.tekstlab.uio.no/obt-ny/morfosyn.html
        """
        # Adverbs
        RBS_TAGGING = set('adj komp <adv>'.split())
        RBR_TAGGING = set('adj sup <adv>'.split())
        # Adjectives
        JJS_TAGGING = set('adj sup'.split())
        JJR_TAGGING = set('adj komp'.split())
        # WH-Determiners
        WP_TAGGING = set('pron hum sp'.split()) # Hva, Hvem
        WDT_TAGGING = set('det sp'.split()) # WH-Determiner: Hvilken, Hvilket, Hvilke
        WPP_TAGGING = set('pron poss hum sp'.split()) # possessive wh-pronoun: Hvis
        VBP_TAGGING = set('verb pres'.split()) # Verb present
        VBD_TAGGING = set('verb pret'.split()) # Verb Preteritum
        VBN_TAGGING = set('verb perf-part'.split()) # Verb past participle
        # VBG
        VBG_TAGGING = set('adj <pres-part>'.split())
        VBG_TAGGING_2 = set('adj <perf-part>'.split())

        # Pronoum
        PRP_TAGGING = set('pron pers hum nom'.split())
        # VBG: adj <pres-part>, adj <perf-part>
        PRPP_TAGGING = set('det poss'.split())
        PRPP_TAGGING_2 = set('pron poss'.split())

        # NNP
        NNP_TAGGING = set('subst appell nøyt ub be ent fl fork'.split())
        NNP_TAGGING_2 = set('subst appell mask ub be ent fork'.split())
        NNP_TAGGING_3 = set('subst appell fork'.split())

        NNS_TAGGING = set('subst fl'.split())

        obtWordTagging = set(taggingInfo['options'].split()) if taggingInfo is not None and len(taggingInfo) > 0 else set([])
        word = taggingInfo['word'].lower() if taggingInfo['word'] is not None and len(taggingInfo) > 0 else ""
        if set(obtWordTagging).issubset(WP_TAGGING):
            return 'WP'
        elif WDT_TAGGING.issubset(obtWordTagging):
            return 'WDT'
        elif WPP_TAGGING.issubset(obtWordTagging):
            return 'WP$'
        elif RBS_TAGGING.issubset(obtWordTagging):
            return 'RBS'
        elif RBR_TAGGING.issubset(obtWordTagging):
            return 'RBR'
        elif JJS_TAGGING.issubset(obtWordTagging):
            return 'JJS'
        elif JJR_TAGGING.issubset(obtWordTagging):
            return 'JJR'
        elif VBP_TAGGING.issubset(obtWordTagging):
            return 'VBT'
        elif VBD_TAGGING.issubset(obtWordTagging):
            return 'VBD'
        elif VBN_TAGGING.issubset(obtWordTagging):
            return 'VBN'
        elif VBG_TAGGING.issubset(obtWordTagging) or VBG_TAGGING_2.issubset(obtWordTagging):
            return 'VBG'
        elif PRP_TAGGING.issubset(obtWordTagging):
            return 'PRP'
        elif PRPP_TAGGING.issubset(obtWordTagging) or PRPP_TAGGING_2.issubset(obtWordTagging):
            return 'PRP$'
        elif NNP_TAGGING.issubset(obtWordTagging) or NNP_TAGGING_2.issubset(obtWordTagging) or NNP_TAGGING_3.issubset(obtWordTagging):
            return 'NNP'
        elif word == u'når' or word == 'hvor':
            return 'WRB'
        elif word == u'til':
            return 'TO'
        elif taggingInfo['is_prop'] == True and taggingInfo['is_subst'] == True:
            return 'NNP'
        elif NNS_TAGGING.issubset(obtWordTagging):
            return 'NNS'
        elif taggingInfo['is_subst'] == True:
            return 'NN'
        elif taggingInfo['is_interj'] == True:
            return 'UH'
        elif taggingInfo['is_prep'] == True:
            return 'IN'
        elif taggingInfo['is_verb'] == True:
            return 'VB'
        elif taggingInfo['is_adj'] == True:
            return 'JJ'
        elif taggingInfo['is_adv'] == True:
            return 'RB'
        elif taggingInfo['is_konj'] == True:
            return 'CC'
        elif taggingInfo['is_det'] == True:
            return 'DT'
        elif taggingInfo['is_pron'] == True:
            return 'PRP'
        elif taggingInfo['is_number']['is_number'] == True:
            return 'CD'
        else:
            return 'UKN'

    def cleanUp(self):
        """
        Clean up the created files
        """
        self.__deleteFile(self._filename)
        self.__deleteFile(self._outputFilename)

    def obtAnalyze(self):
        """
        Analyze the text using the Oslo-Bergen tagger.
        """
        if self._outputData: # If the text has been already analyzed...
            return self._outputData

        # Current directory
        currentDirectory = os.path.dirname(os.path.realpath(__file__))
        # Output filename
        output_filename = "%s_OUTPUT" % (self._filename,)
        self._outputFilename = output_filename
        # Get the type of tagger that you want to use with the Oslo-Bergen tagger
        tagger_type = os.environ.get('OBT_TYPE', 'tag-nostat-bm.sh')
        # Run the tagger
        obtCmd = '%s/../../../../The-Oslo-Bergen-Tagger/%s %s > %s' % (currentDirectory, tagger_type, self._filename, output_filename)

        os.system(obtCmd)

        # Read the output file
        file_object = open(output_filename, 'r')
        text = file_object.read().decode('utf8')
        text = text.split("\n")
        # Parsing the result
        result = []
        new_obj = {}
        for word in text:
            if not word:
               continue # word is empty

            is_match = self.REGEX.match(word)
            if self.REGEX.match(word): # Check if the word matches the regex <word>(?P<w>(.*?))</word>
                new_obj = {"word": is_match.groups(0)[0]}
                result.append(new_obj)
            elif self.REGEX2.match(word.lower()): # Check if the word matches the regex <(?P<w>[\w+]*)>
               continue
            else:
               word = word.replace("\"", "").replace("\t", "")
               tagging = [w for w in word.split(" ") if w]
               # Analyze the word
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
               new_obj["is_adv"] = True if len([tag for tag in tagging if tag == 'adv']) > 0 else False
               new_obj["is_konj"] = True if len([tag for tag in tagging if tag == 'konj']) > 0 else False
               new_obj["is_prep"] = True if len([tag for tag in tagging if tag == 'prep']) > 0 else False
               new_obj["is_pron"] = True if len([tag for tag in tagging if tag == 'pron']) > 0 else False

               tag = self.__getUniversalTag(new_obj)

               new_obj['tag'] = tag
               new_obj['tagged_word'] = (new_obj.get('word',''), tag)

        self._outputData = result
        return result

    def findTags(self, text_analysis=None):
        """
        Find the tags within the text
        It takes all the words that are both "is_prop" and "is_subst"
        """
        if text_analysis is None or not isinstance(text_analysis, dict) or not 'obt' in text_analysis:
            raise Exception("The text analysis is not available")

        # Obt text analysis
        obtData = text_analysis.get('obt', [])

        entities = []
        for entity in obtData:
            if (entity.get("is_prop") == True and entity.get("is_subst") == True):
                entities.append(entity.get("word"))

        unique_tags = set(entities)
        return list(unique_tags)

    def findEntities(self, stopwords=[]):
        """
        Find the entities within the text
        """
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

    def analyze(self):
        """
        Analyze the text
        """
        # Run the Oslo-Bergen tagger analysis
        data = self.obtAnalyze()

        # Format the result returned from the Oslo-Bergen Tagger
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
        advs = list(set([unicode(tag.get("word")) for tag in data  if tag.get("is_adv") == True]))

        textAnalyze['VB'] = verbs
        textAnalyze['NN'] = substs
        textAnalyze['NNP'] = props
        textAnalyze['CD'] = numbers
        textAnalyze['JJ'] = adjs
        textAnalyze['CC'] = conjs
        textAnalyze['unknowns'] = unknowns
        textAnalyze['DT'] = dets
        textAnalyze['inf_merks'] = inf_merks
        textAnalyze['sbus'] = sbus
        textAnalyze['interjs'] = interjs
        textAnalyze['RB'] = advs
        textAnalyze["obt"] = data
        textAnalyze["pos"] = [entity["tagged_word"] for entity in data]

        return textAnalyze
