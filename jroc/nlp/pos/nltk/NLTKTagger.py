"""
POS tag list:

CC	coordinating conjunction
CD	cardinal digit
DT	determiner
EX	existential there (like: "there is" ... think of it like "there exists")
FW	foreign word
IN	preposition/subordinating conjunction
JJ	adjective	'big'
JJR	adjective, comparative	'bigger'
JJS	adjective, superlative	'biggest'
LS	list marker	1)
MD	modal	could, will
NN	noun, singular 'desk'
NNS	noun plural	'desks'
NNP	proper noun, singular	'Harrison'
NNPS	proper noun, plural	'Americans'
PDT	predeterminer	'all the kids'
POS	possessive ending	parent's
PRP	personal pronoun	I, he, she
PRP$	possessive pronoun	my, his, hers
RB	adverb	very, silently,
RBR	adverb, comparative	better
RBS	adverb, superlative	best
RP	particle	give up
TO	to	go 'to' the store.
UH	interjection	errrrrrrrm
VB	verb, base form	take
VBD	verb, past tense	took
VBG	verb, gerund/present participle	taking
VBN	verb, past participle	taken
VBP	verb, sing. present, non-3d	take
VBZ	verb, 3rd person sing. present	takes
WDT	wh-determiner	which
WP	wh-pronoun	who, what
WP$	possessive wh-pronoun	whose
WRB	wh-abverb	where, when
"""
from collections import defaultdict
from TaggerStorageAdapter import TaggerStorageAdapter
import nltk
import itertools
class NLTKTagger(object):

    __storage = None
    def __init__(self, model=None, modelFileName=None, fileName=None, language="en"):
        self.__language = language
        if not model is None: # Use a different trained model
            self.__storage = TaggerStorageAdapter(model=model)
        elif not fileName is None: # Use a trained model from a separate file
            self.__storage = TaggerStorageAdapter(fileName=modelFileName)
        else: # Use the default trained model (classifier)
            self.__storage = TaggerStorageAdapter()


    def getTags(self, text):
        """
        It returns the POS tags for a given text
        """


        # Retrieve the tagger from the storage
        tagger = self.__storage.getTagger()

        # Tag the text
        pos = tagger.tag(text)

        # Result
        results = defaultdict(list)
        indexedPos = nltk.Index((value, key) for (key, value) in pos)
        results['pos'] = pos
        results['indexed'] = indexedPos

        results['JJ'].extend(itertools.chain.from_iterable([indexedPos[val] for val in indexedPos if val == 'JJ' or val == 'JJS' or val == 'JJR']))
        results['VB'].extend(itertools.chain.from_iterable([indexedPos[val]for val in indexedPos if val == 'VB' or
                                                                                                            val == 'VBD' or
                                                                                                            val == 'VBG' or
                                                                                                            val == 'VBN' or
                                                                                                            val == 'VBP' or
                                                                                                            val == 'VBZ']))
        results['NN'].extend(itertools.chain.from_iterable(sorted([indexedPos[val] for val in indexedPos if val == 'NN' or
                                                                                                            val == 'NNS'])))
        results['NNP'].extend(itertools.chain.from_iterable([indexedPos[val] for val in indexedPos if val == 'NNP' or
                                                                                                            val == 'NNPS']))
        results['RB'].extend(itertools.chain.from_iterable([indexedPos[val] for val in indexedPos if val == 'RB' or
                                                                                                            val == 'RBR' or
                                                                                                            val == 'RBS']))
        results['common'] = self.__commonWords(pos, number=100)
                                                                                                   
        return results

    def __commonWords(self, pos,  number=100):
        """
        Find common words in the text.
        """
        vocab = nltk.FreqDist(pos)
        common = [word[0] for (word, _) in vocab.most_common(100) if word[1] == 'NN' or word[1] == 'NNS'  or word[1] == 'NNP'  or word[1] == 'NNPS']
        return common
