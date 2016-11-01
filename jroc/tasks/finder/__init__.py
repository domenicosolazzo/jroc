from jroc.tasks.basic.BasicTask import BasicTask
from jroc.tasks.cleaning.DataCleanerTask import DataCleanerTask
from jroc.tasks.language.LanguageDetectorTask import LanguageDetectorTask
from jroc.tasks.loaders.LoaderTask import LoaderTask
from jroc.tasks.wordnet.WordnetTask import WordnetTask
from jroc.tasks.tokenizers.TokenizerTask import SentenceTokenizerTask, WordTokenizerTask
from jroc.tasks.stopwords.StopwordTask import StopwordFilteringTask, StopwordRetrievalTask
from jroc.tasks.reduce.MixDataTask import MixDataTask
from jroc.tasks.pos.PosTaggerTask import PosTaggerTask
from jroc.tasks.pos.PosTaggerTask import PosTaggerTagsTask
from jroc.tasks.sparql.dbpedia.EntityAnnotationTask import EntityAnnotationTask, EntityAnnotationURITask, EntityAnnotationTypesTask, EntityAnnotationPropertiesTask, EntityAnnotationThumbnailTask


# NER
from jroc.tasks.ner.NLTKTaggerTask import NLTKTaggerTask
from jroc.tasks.ner.StanfordTaggerTask import StanfordTaggerTask
from jroc.tasks.ner.TaggerTagsTask import TaggerTagsTask

# Regex
from jroc.tasks.ner.regex.RegexTaggerTask import RegexTaggerTask
from jroc.tasks.ner.regex.RegexTaggerMixerTask import RegexTaggerMixerTask


AVAILABLE_TASKS = {
    'BASIC': BasicTask,
    'DATA_CLEANER': DataCleanerTask,
    'LANGUAGE_DETECTOR': LanguageDetectorTask,
    'LOADER': LoaderTask,
    'NER_NLTK_TAGGING': NLTKTaggerTask,
    'NER_REGEX_TAGGING': RegexTaggerTask,
    'NER_REGEX_TAGGING_MIXING': RegexTaggerMixerTask,
    'NER_STANFORD_TAGGING': StanfordTaggerTask,
    'NER_POS_TAGGING': TaggerTagsTask,
    'MIXDATA': MixDataTask,
    'POS_TAGGING': PosTaggerTask,
    'POS_TAGGING_TAGS': PosTaggerTagsTask,
    'SPARQL_ANNOTATION': EntityAnnotationTask,
    'SPARQL_ANNOTATION_URI': EntityAnnotationURITask,
    'SPARQL_ANNOTATION_TYPES': EntityAnnotationTypesTask,
    'SPARQL_ANNOTATION_PROPERTIES': EntityAnnotationPropertiesTask,
    'SPARQL_ANNOTATION_THUMBNAIL': EntityAnnotationThumbnailTask,
    'STOPWORD_FILTERING': StopwordFilteringTask,
    'STOPWORD_RETRIEVAL': StopwordRetrievalTask,
    'TOKENIZER_SENTENCE': SentenceTokenizerTask,
    'TOKENIZER_WORD': WordTokenizerTask,
    'WORDNET': WordnetTask,
}
