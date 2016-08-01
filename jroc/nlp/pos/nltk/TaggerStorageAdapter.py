"""
Class for loading and storing a trained tagger.

Some pickle files that you can use: (They are in the folder /data/nltk/taggers)
- treebank_NaiveBayes.pickle: Use a classifier for retrieving the correct POS
- treebank_aubt.pickle: Use a combination of Affix + Unigram + Bigram + Trigram taggers
"""
from pickle import dump, load
import os

MODELS = dict([
    ('aubt', "%s/../../../../data/nltk/taggers/%s" % (os.path.dirname(os.path.realpath(__file__)),"treebank_aubt.pickle")),
    ('classifier', "%s/../../../../data/nltk/taggers/%s" % (os.path.dirname(os.path.realpath(__file__)),"treebank_NaiveBayes.pickle"))
])
class TaggerStorageAdapter(object):

    DEFAULT_PICKLE_NAME = MODELS.get('classifier', None)

    __tagger = None

    def __init__(self, tagger=None, model=None, fileName=None):
        if not tagger is None:
            self.__tagger = tagger

        elif not model is None:
            modelPickleFile = MODELS.get(model, None)
            if modelPickleFile is None:
                raise Exception("Model does not exist")
            self.load(modelPickleFile)

        elif not fileName is None:
            self.load(fileName)

        else:
            self.load(self.DEFAULT_PICKLE_NAME)

    def load(self, pickleFile):
        """
        Load a tagger from a pickle file
        """
        if pickleFile is None:
            pickleFile = DEFAULT_PICKLE_NAME
        input = open(pickleFile, 'rb')
        tagger = load(input)
        input.close()
        # Store the tagger internally
        self.__tagger = tagger
        return tagger

    def save(self, pickleFileTo=None):
        """
        Save a trained tagger to a pickle file
        """
        if pickleFileTo is None:
            pickleFileTo = DEFAULT_PICKLE_NAME
        output = open(pickleFileTo, 'wb')
        dump(self.__tagger, output, -1)
        output.close()
        return True

    def getTagger(self):
        """
        Get a tagger
        """
        return self.__tagger
