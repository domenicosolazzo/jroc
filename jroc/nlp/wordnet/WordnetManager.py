# -*- coding: utf-8 -*-
import itertools
"""
Languages           | ShortCode     | Wordnet
Albanian            |   sq          |   als
Arabic              |   ar          |   arb
Bulgarian           |   bg          |   bul
Catalan             |   ca          |   cat
Chinese             |   zh          |   cmn
Chinese (Taiwan)    |   qn          |   qcn
Greek               |   el          |   ell
Basque              |   eu          |   eus
Persian             |   fa          |   fas
Finish              |   fi          |   fin
French              |   fr          |   fra
Galician            |   gl          |   glg
Hebrew              |   he          |   heb
Croatian            |   hr          |   hrv
Indonesian          |   id          |   ind
Italian             |   it          |   ita
Japanese            |   ja          |   jpn
Norwegian NyNorsk   |   nn          |   nno
Norwegian Bokmål    |   nb/no       |   nob
Polish              |   pl          |   pol
Portuguese          |   pt          |   por
Slovenian           |   sl          |   slv
Spanish             |   es          |   spa
Swedish             |   sv          |   swe
Thai                |   tt          |   tha
Malay               |   ms          |   zsm
"""

"""
Language short codes => Wordnet Code
"""
AVAILABLE_LANGUAGES = dict([('sq','als'), ('ar', 'arb'), ('bg', 'bul'), ('ca', 'cat'), ('da', 'dan'), ('zh', 'cmn'),
                            ('el','ell'), ('eu', 'eus'), ('fa', 'fas'), ('fi', 'fin'), ('fr', 'fra'),
                            ('gl','glg'), ('he', 'heb'), ('hr', 'hrv'), ('id', 'ind'), ('it', 'ita'),
                            ('ja','jpn'),
                            ('nn', 'nno'), ('nb', 'nob'),
                            ('no', 'nob'), ('pl', 'pol'),
                            ('pt', 'por'),
                            ('qn','qcn'), ('sl', 'slv'), ('es', 'spa'), ('sv', 'swe'), ('tt', 'tha'),
                            ('ms', 'zsm'),
                            ('en', 'eng')])
"""
Language names => Short Code
"""
AVAILABLE_LANGUAGES_NAMES = dict([
                                ('albanian', 'sq'), ('arabic', 'ar'),('bulgarian', 'bg'), ('catalan', 'cat'), ('danish', 'da'),
                                ('chinese', 'zh'), ('basque', 'eu'), ('persian', 'fa'), ('finnish', 'fi'), ('france', 'fr'),
                                ('galician', 'gl'), ('hebrew', 'he'), ('croatian', 'hr'), ('indonesian', 'id'), ('italian', 'it'),
                                ('japanese', 'ja'), ('norwegian_nynorsk', 'nn'), ('norwegian', 'no'), ('norwegian_bokmal', 'nb'),
                                ('polish', 'pl'), ('portuguese', 'pt'), ('slovenian', 'sl'), ('spanish', 'es'),
                                ('swedish', 'sv'), ('thai', 'sv'), ('malay', 'ms'), ('english', 'en')
                                ])


class WordnetManager(object):
    def __init__(self, language="en"):
        """
        Constructor for the wordnet manager.
        It takes a main language.
        """
        self.__language = language

    def __isLanguageAvailable(self, code=None, language_name=None):
        """
        Check if a language is available
        """
        if code is None and language_name is None:
            raise Exception("Error evaluating the correct language")

        if code is not None and code.lower() in AVAILABLE_LANGUAGES:

            return True

        if language_name is not None and language_name.lower() in AVAILABLE_LANGUAGES_NAMES:
            return True

        return False

    def __nameToWordnetCode(self, name):
        """
        It returns the wordnet code for a given language name
        """
        if not self.__isLanguageAvailable(language_name=name):
            raise Exception("Wordnet code not found for the language name %s " % name)
        name = name.lower()
        languageShortCode = AVAILABLE_LANGUAGES_NAMES[name]

        wordnetCode = self.__shortCodeToWordnetCode(code=languageShortCode)
        return wordnetCode

    def __shortCodeToWordnetCode(self, shortCode):
        """
        It returns the wordnet code from a given language short code
        """
        if not self.__isLanguageAvailable(code=shortCode):
            raise Exception("Wordnet code not found for the language short code %s " % shortCode)

        code = shortCode.lower()
        wordnetCode = AVAILABLE_LANGUAGES[code]
        return wordnetCode

    def __getSynsets(self, word, wordNetCode):
        """
        It returns the synsets given both word and language code
        """
        from nltk.corpus import wordnet as wn

        synsets = wn.synsets(word, lang=wordNetCode)
        return synsets

    def getLemmas(self, word, languageCode="en"):
        """
        Get the lemmas for a given word
        :word: The word
        :languageCode: The language for a given lemma
        """
        wnCode = self.__shortCodeToWordnetCode(shortCode=languageCode)
        synsets = self.__getSynsets(word, wnCode) #wn.synsets(word, lang=wnCode)
        lemmas = dict([('en', [])])

        for synset in synsets:
            enLemmas = synset.lemma_names()
            lemmas['en'].extend(enLemmas)

            if languageCode != "en" and self.__isLanguageAvailable(code=languageCode):
                langLemmas = list(sorted(set(synset.lemma_names(lang=wnCode))))
                lemmas[languageCode] = langLemmas
        lemmas['en'] = list(sorted(set(lemmas.get('en', []))))
        return lemmas

    def getSynonyms(self, words=[], language_code="en"):
        """
        Get the synonyms from a list of words.
        :words: A list of words
        :language_code: the language for the synonyms.
        """
        if words is None or not isinstance(words, list) or list(words) <= 0:
            return []

        if not self.__isLanguageAvailable(code=language_code):
            return []

        wnCode = self.__shortCodeToWordnetCode(language_code)
        result = {}
        for word in words:
            result[word] = dict([('lemmas', self.getLemmas(word,languageCode=language_code))])
        return result

    def getHyponyms(self, words, language_code="en"):
        """
        Get specific synsets from a given synset
        """
        wnCode = self.__shortCodeToWordnetCode(language_code)
        result = {}
        for word in words:
            synonyms = self.__getSynsets(word, wnCode)
            hyponyms = [hyp for synset in synonyms for hyp in synset.hyponyms()]
            engLemmas = [hyp.lemma_names() for hyp in  hyponyms]
            lemmas = dict([('en', list(sorted(set(itertools.chain.from_iterable(engLemmas)), key=lambda s: s.lower())))])
            if language_code != "en":
                languageLemmas = [hyp.lemma_names(lang=wnCode) for hyp in  hyponyms]
                languageLemmas = list(sorted(set(itertools.chain.from_iterable(languageLemmas)), key=lambda s: s.lower()))
                lemmas[language_code] = languageLemmas

            result[word] = dict([ ('lemmas', lemmas), ('language', language_code)])

        return result

    def getHypernyms(self, words, language_code="en"):
        """
        Get general synsets from a given synset
        """
        wnCode = self.__shortCodeToWordnetCode(language_code)
        result = {}
        for word in words:
            synonyms = self.__getSynsets(word, wnCode)
            hypernyms = [hyp for synset in synonyms for hyp in synset.hypernyms()]
            engLemmas = [hyp.lemma_names() for hyp in  hypernyms]
            lemmas = dict([('en', list(sorted(set(itertools.chain.from_iterable(engLemmas)), key=lambda s: s.lower())))])
            if language_code != "en":
                languageLemmas = [hyp.lemma_names(lang=wnCode) for hyp in  hypernyms]
                languageLemmas = list(sorted(set(itertools.chain.from_iterable(languageLemmas)), key=lambda s: s.lower()))
                lemmas[language_code] = languageLemmas

            result[word] = dict([ ('lemmas', lemmas), ('language', language_code)])

        return result
