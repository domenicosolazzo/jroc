from . import BasicTask
from . import NLTKTokenizer

class SentenceTokenizerTask(BasicTask):
    """
    SentenceTokenizerTask: Take a text and tokenize it in sentences
    """
    __kernel = None # Kernel for this loader

    __inputKey = 'data' # Expected input key
    def __init__(self, name, initial_task=False):
        super(SentenceTokenizerTask, self).__init__(name, initial_task)
        self.__kernel = NLTKTokenizer()

    def execute(self, input):
        try:
            super(SentenceTokenizerTask, self).execute(input)
            assert(isinstance(input, dict))

            # Fetch the language
            language = input.get('language', 'en')
            if language != 'en':
                self.__kernel = NLTKTokenizer(language=language)

            # Fetch data text
            data = input.get(self.__inputKey, None)
            if data is None:
                raise Exception("Error retrieving the input for this task. Task: %s" % self.getName())

            output = self.__kernel.tokenizeText(data)
            self.finish(data=output, failed=False, error=None)
        except:
            output = "Error tokenizing the text"
            self.finish(data=None, failed=True, error=output)
        return self.getOutput()

class WordTokenizerTask(BasicTask):
    """
    WordTokenizerTask: Take a list of sentences and tokenize them in single words
    """
    __kernel = None # Kernel for this loader

    __inputKey = 'sentences' # Expected input key

    def __init__(self, name, initial_task=False):
        super(WordTokenizerTask, self).__init__(name, initial_task)
        self.__kernel = NLTKTokenizer()

    def execute(self, input=None):
        try:
            super(WordTokenizerTask, self).execute(input)
            assert(isinstance(input, dict))

            # Fetch data text
            data = input.get(self.__inputKey, None)
            if data is None:
                raise Exception("Error retrieving the input for this task. Task: %s" % self.getName())

            if not isinstance(data, list):
                raise Exception("The data in input is invalid. Task: %s" % self.getName())


            output = [self.__kernel.tokenizeSentence(sentence) for sentence in data]
            self.finish(data=output, failed=False, error=None)
        except:
            output = "Error tokenizing some of the sentences in input"
            self.finish(data=None, failed=True, error=output)
        return self.getOutput()
