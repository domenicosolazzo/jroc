from . import NLTKStopwords as StopwordManager
import unittest
import os

class StopwordsTestCase(unittest.TestCase):
    languageDetector = None
    currentDirectory = "%s" % (os.path.dirname(os.path.realpath(__file__)), )
    stopwordsDirectory = "%s/../../../../jroc/nlp/stopwords/data/" % (currentDirectory,)

    def setUp(self):
        self.stopwordManager = None

    def tearDown(self):
        self.stopwordManager = None

    def test_norwegian_stopwords(self):
        """
        Test the stopwords for the norwegian language
        """
        self.stopwordManager = StopwordManager(language="no")
        expected = [u'vart', u'over', u'skal', u'ikkje', u'deires', u'hennes', u'dere',
                    u'henne', u'alle', u'han', u'begge', u'f\xf8r', u'ved', u'hvor', u'har', u'korso',
                    u'oss', u'ditt', u'meget', u'opp', u'di', u'noe', u'de', u'mot', u'vere', u'noko',
                    u'du', u'din', u'hossen', u'mykje', u'denne', u'etter', u'upp', u'ville', u'blitt',
                    u'en', u'hvem', u'kunne', u'mi', u'skulle', u'nokon', u'kvifor', u'seg', u'bare',
                    u'et', u'v\xe6re', u'blei', u'somt', u'inni', u'er', u'hvorfor', u'v\xe5r', u'ingi',
                    u'for', u'ned', u'kun', u'bli', u'ble', u'deim', u'med', u'meg', u'd\xe5', u'mitt',
                    u'men', u'fordi', u'hoss', u'nokre', u'hadde', u'sidan', u'ja', u'om', u'ett', u'og',
                    u'ein', u'hennar', u'samme', u'hva', u'sj\xf8l', u'som', u'korleis', u'vil', u'dykkar',
                    u'hvordan', u'fra', u'sine', u'kom', u'her', u'kven', u'ingen', u'n\xe5', u'varte',
                    u'ikke', u'deira', u'noen', u'jeg', u'var', u'n\xe5r', u'v\xe6rt', u'mellom', u'uten',
                    u'hun', u'honom', u'mine', u'hvilken', u'ho', u'ha', u'kvar', u'me', u'hj\xe5', u'inkje',
                    u'verte', u'\xe5', u'eit', u'b\xe5de', u'ut', u'der', u'det', u'um', u'dei', u'dykk',
                    u'dem', u'den', u's\xe5', u'deg', u'eg', u'vors', u'vi', u'slik', u'vort', u'inn',
                    u'blir', u'at', u'av', u'sitt', u'vore', u'hver', u's\xe5nn', u'min', u'elles', u'eller',
                    u'deres', u'enn', u'hvilke', u'til', u'sia', u'disse', u'p\xe5', u'nokor', u'selv', u'sin',
                    u'hvis', u'siden', u'eitt', u'ogs\xe5', u'kva', u'dette', u'kan', u'kvi', u'hoe', u'hans',
                    u'kvarhelst', u'da', u'medan', u'man', u'somme', u'i', u'no', u'b\xe5e', u'si', u'so', u'noka',
                    u'mange']
        actual = self.stopwordManager.getStopwords()
        self.assertEqual(sorted(expected), sorted(actual))

    def test_english_stopwords(self):
        """
        Test the stopwords for the english language
        """
        self.stopwordManager = StopwordManager(language="en")
        expected = [u'all', u'just', u'being', u'over', u'both', u'through', u'yourselves', u'its',
                    u'before', u'o', u'hadn', u'herself', u'll', u'had', u'should', u'to', u'only',
                    u'won', u'under', u'ours', u'has', u'do', u'them', u'his', u'very', u'they', u'not',
                    u'during', u'now', u'him', u'nor', u'd', u'did', u'didn', u'this', u'she', u'each',
                    u'further', u'where', u'few', u'because', u'doing', u'some', u'hasn', u'are', u'our',
                    u'ourselves', u'out', u'what', u'for', u'while', u're', u'does', u'above', u'between',
                    u'mustn', u't', u'be', u'we', u'who', u'were', u'here', u'shouldn', u'hers', u'by',
                    u'on', u'about', u'couldn', u'of', u'against', u's', u'isn', u'or', u'own', u'into',
                    u'yourself', u'down', u'mightn', u'wasn', u'your', u'from', u'her', u'their', u'aren',
                    u'there', u'been', u'whom', u'too', u'wouldn', u'themselves', u'weren', u'was', u'until',
                    u'more', u'himself', u'that', u'but', u'don', u'with', u'than', u'those', u'he', u'me',
                    u'myself', u'ma', u'these', u'up', u'will', u'below', u'ain', u'can', u'theirs', u'my',
                    u'and', u've', u'then', u'is', u'am', u'it', u'doesn', u'an', u'as', u'itself', u'at',
                    u'have', u'in', u'any', u'if', u'again', u'no', u'when', u'same', u'how', u'other',
                    u'which', u'you', u'shan', u'needn', u'haven', u'after', u'most', u'such', u'why',
                    u'a', u'off', u'i', u'm', u'yours', u'so', u'y', u'the', u'having', u'once']
        actual = self.stopwordManager.getStopwords()
        self.assertEqual(expected, actual)

    def test_danish_stopwords(self):
        """
        Test the stopwords for the danish language
        """
        self.stopwordManager = StopwordManager(language="da")
        expected = [u'over', u'skal', u'alt', u'bliver', u'alle', u'ham', u'han', u'under',
                    u'hvor', u'har', u'hos', u'meget', u'de', u'da', u's\xe5dan', u'du', u'mod', u'din',
                    u'dig', u'hendes', u'nu', u'denne', u'ville', u'en', u'kunne', u'skulle', u'blive',
                    u'et', u'v\xe6re', u'er', u'for', u'ned', u'med', u'men', u'jo', u'sine', u'om', u'og',
                    u'anden', u'os', u'op', u'noget', u'som', u'vil', u'blev', u'havde', u'ad', u'jer',
                    u'fra', u'her', u'ikke', u'jeg', u'var', u'n\xe5r', u'hun', u'der', u'det', u'dem',
                    u'den', u'ud', u'nogle', u'hvad', u'have', u'af', u'vi', u'mine', u'efter', u'at', u'vor',
                    u'ind', u'end', u'sit', u'eller', u'deres', u'mig', u'til', u'sig', u'disse', u'p\xe5',
                    u'selv', u'mit', u'hvis', u'ogs\xe5', u'dette', u'mange', u'hans', u'hende', u'man', u'i',
                    u'min', u'v\xe6ret', u'dog', u'thi', u'sin']
        actual = self.stopwordManager.getStopwords()
        self.assertEqual(expected, actual)

    def test_german_stopwords(self):
        """
        Test the stopwords for the german language
        """
        self.stopwordManager = StopwordManager(language="de")
        expected = [u'andere', u'unseres', u'anderm', u'andern', u'das', u'w\xfcrde', u'w\xe4hrend', u'sollte', u'selbst', u'anderr', u'anders',
            u'einer', u'wollte', u'unserem', u'als', u'unseren', u'alle', u'dessen', u'dazu', u'auf', u'dich', u'hab', u'sondern', u'demselben',
            u'aus', u'einige', u'derselbe', u'sonst', u'hatte', u'hat', u'bin', u'musste', u'waren', u'mein', u'deine', u'ihnen', u'deinem',
            u'deinen', u'deines', u'deiner', u'einmal', u'ich', u'dasselbe', u'du', u'bis', u'hin', u'wenn', u'viel', u'war', u'keiner', u'keines',
            u'die', u'warst', u'wird', u'w\xfcrden', u'haben', u'weil', u'nichts', u'ihn', u'keinen', u'dir', u'wir', u'kann', u'solcher', u'nur',
            u'hinter', u'manche', u'solchen', u'es', u'er', u'will', u'ohne', u'f\xfcr', u'und', u'meinen', u'diesem', u'diesen', u'meinem',
            u'meiner', u'meines', u'dieser', u'dieses', u'indem', u'werde', u'dein', u'jede', u'denselben', u'wollen', u'dort', u'soll',
            u'jeden', u'jedem', u'diese', u'wo', u'seine', u'wirst', u'auch', u'jenen', u'keinem', u'jedes', u'jeder', u'habe', u'weiter',
            u'zur', u'uns', u'hatten', u'welcher', u'bist', u'werden', u'ob', u'ist', u'k\xf6nnte', u'ander', u'hier', u'einig', u'da\xdf',
            u'zum', u'solches', u'wie', u'aber', u'eines', u'ihr', u'nach', u'gewesen', u'desselben', u'damit', u'eine', u'ihm', u'einen',
            u'wieder', u'einem', u'jene', u'sind', u'jenem', u'welches', u'eurem', u'einiger', u'einiges', u'oder', u'weg', u'einigem',
            u'einigen', u'euer', u'dieselbe', u'was', u'von', u'jenes', u'jener', u'durch', u'unsere', u'mich', u'muss', u'ins', u'solchem',
             u'nun', u'bei', u'welchem', u'der', u'des', u'nicht', u'um', u'dann', u'dem', u'den', u'welchen', u'sein', u'ein', u'ihre', u'seinem',
             u'seinen', u'keine', u'alles', u'aller', u'noch', u'vom', u'unter', u'gegen', u'am', u'an', u'\xfcber', u'im', u'zwischen', u'vor',
             u'in', u'allen', u'allem', u'welche', u'seiner', u'seines', u'anderer', u'anderes', u'euch', u'manchem', u'derer', u'manchen',
             u'k\xf6nnen', u'also', u'manches', u'mancher', u'dieselben', u'sich', u'sie', u'zu', u'so', u'mir', u'anderen', u'mit', u'anderem',
             u'eurer', u'eures', u'zwar', u'dies', u'sehr', u'jetzt', u'etwas', u'derselben', u'eure', u'euren', u'da', u'solche', u'man',
             u'ihrem', u'kein', u'ihren', u'meine', u'doch', u'machen', u'denn', u'unser', u'ihres', u'ihrer']
        actual = self.stopwordManager.getStopwords()
        self.assertEqual(sorted(expected), sorted(actual))

    def test_spanish_stopwords(self):
        """
        Test the stopwords for the spanish language
        """
        self.stopwordManager = StopwordManager(language="es")
        expected = [u'son', u'estar\xe1', u'estadas', u'tengamos', u'hubieras', u'sentidos',
                    u'nuestra', u'teng\xe1is', u'\xe9l', u'tuvi\xe9semos', u'estos', u'tuvimos',
                    u'tuviste', u'nuestro', u'otro', u'tuvieron', u'antes', u'le', u'han', u'la',
                    u'estar\xedamos', u'lo', u'estar\xedas', u'tu', u'ten\xedamos', u'quienes',
                    u'otra', u'hubi\xe9semos', u'hay', u'suyas', u'tendr\xe9', u'ti', u'estar', u'te',
                    u'ten\xe9is', u'habr\xedas', u'tendr\xe1', u'porque', u'estuvimos', u'ser\xedais',
                    u'estaba', u'esa', u'yo', u'\xe9ramos', u'ya', u'cuando', u'nada', u'de', u'est\xe1is',
                    u'tuyos', u'hayan', u'tendr\xe9is', u'estuve', u'algunos', u'hayas', u'tanto', u'qu\xe9',
                    u'seas', u'vosostros', u'm\xeda', u'tuvieras', u'nos', u'hubimos', u'est\xe9is', u'estoy',
                    u'estaremos', u'hubieran', u'una', u'tuvieran', u'estar\xe9is', u'somos', u'fu\xe9semos',
                    u'desde', u'sentida', u'habr\xe9', u'nosotras', u'estados', u'sentido', u'habr\xe1', u'el',
                    u'fuera', u'en', u'habr\xeda', u'esos', u'tendr\xe1n', u'otras', u'habr\xe9is', u'ten\xedas',
                    u'fuesen', u'fue', u'hubieseis', u'tenida', u'soy', u'fueseis', u'seamos', u'hube', u'sea',
                    u'tendr\xedamos', u'estamos', u'todo', u'es', u'eres', u'estad', u'tuya', u't\xfa', u'tuvieseis',
                    u'fueses', u'hab\xedas', u'm\xedas', u'tenido', u'muy', u'tuyo', u'algunas', u'poco', u'ese',
                    u'haya', u'sus', u'estas', u'sobre', u'ser\xedamos', u'eso', u'hab\xedais', u'tened', u'estar\xe9',
                    u'era', u'fuerais', u'habr\xedan', u'estuvieran', u'tienen', u'fuiste', u'tuvo', u'tus',
                    u'fu\xe9ramos', u'estar\xedais', u'les', u'que', u'como', u'estuvieras', u'habido', u'tengan',
                    u'tendr\xe1s', u'tenidas', u'ser\xedas', u'estar\xe1s', u'estuvierais', u'ten\xeda', u'hab\xeda',
                    u'estuvo', u'eras', u'estuviera', u'estuvisteis', u'tuvierais', u'o', u'ser\xe1s', u'est\xe1bamos',
                    u'tambi\xe9n', u'ser\xe1n', u'nosotros', u'algo', u'quien', u'fui', u'os', u'ser\xe9is', u'uno',
                    u'hab\xedan', u'hubiera', u'habiendo', u'est\xe1', u'teniendo', u'fuisteis', u'por', u'est\xe9',
                    u'durante', u'mucho', u'suya', u'donde', u'estuvieron', u'tendremos', u'erais', u'ante',
                    u'tuvisteis', u'otros', u'estaban', u'suyo', u'tienes', u'fueron', u'tenemos', u'tuvieses',
                    u'contra', u'esas', u'estado', u'pero', u'est\xe9s', u'estemos', u'est\xe9n', u'los', u'estabas',
                    u'nuestros', u'se\xe1is', u'est\xe1s', u'ellos', u'tuvi\xe9ramos', u'estar\xe1n', u'fueran', u'suyos',
                    u'habidos', u'hubiese', u'tendr\xedais', u'm\xe1s', u'vuestros', u'm\xedos', u'estabais', u'para',
                    u'fuese', u'fuimos', u'estar\xedan', u'tendr\xedas', u'fueras', u'estuvieseis', u'tendr\xedan',
                    u'vuestro', u'vuestra', u'ha', u'ten\xedais', u'he', u'me', u'has', u'hubo', u'seremos', u'hab\xe9is',
                    u'hubi\xe9ramos', u'mi', u'tengo', u'est\xe1n', u'ten\xedan', u'sintiendo', u'un', u'del', u'hemos',
                    u's\xed', u'tuviera', u'tengas', u'sean', u'habr\xedais', u'este', u'unos', u'esta', u'habr\xe1n',
                    u'estando', u'eran', u'esto', u'al', u'hayamos', u'hab\xedamos', u'estuviese', u'hay\xe1is',
                    u'hubieses', u'sois', u'tenidos', u'tuviese', u'habr\xe1s', u'tenga', u'ni', u'tuviesen', u'no',
                    u'estuvieses', u'ellas', u'sentidas', u'tiene', u'habr\xedamos', u'estuviesen', u'cual',
                     u'nuestras', u'mis', u'sin', u'todos', u'vosostras', u'hubisteis', u'tuyas', u'habremos',
                     u'tuve', u'hubiste', u'ella', u'sentid', u'hubierais', u'hubieron', u'estada', u'siente',
                     u'ser\xeda', u'estar\xeda', u'las', u'a', u'vuestras', u'estuvi\xe9ramos', u'e', u'entre',
                     u'habida', u'm\xed', u'ser\xedan', u'muchos', u'm\xedo', u'su', u'hasta', u'estuvi\xe9semos',
                     u'hubiesen', u'ser\xe1', u'y', u'habidas', u'tendr\xeda', u'con', u'estuviste', u'se', u'ser\xe9']
        actual = self.stopwordManager.getStopwords()
        self.assertEqual(sorted(expected), sorted(actual))

    def test_italian_stopwords(self):
        """
        Test the stopwords for the spanish language
        """
        self.stopwordManager = StopwordManager(language="it")
        expected = [u'all', u'fanno', u'ebbi', u'stettero', u'stessi', u'sarei', u'faccia',
                    u'nostra', u'facesse', u'avr\xe0', u'nostre', u'negl', u'farai', u'nostri',
                    u'nostro', u'farei', u'hai', u'alle', u'le', u'alla', u'la', u'allo', u'lo',
                    u'quelli', u'tu', u'quello', u'sia', u'li', u'starebbe', u'loro', u'faresti',
                    u'ti', u'fareste', u'fossimo', u'stiate', u'cui', u'non', u'avesti', u'noi',
                    u'di', u'dal', u'avr\xf2', u'nell', u'dell', u'avete', u'da', u'starai', u'fai',
                    u'stando', u'facevo', u'stette', u'aveste', u'steste', u'avendo', u'pi\xf9', u'tra',
                    u'sarete', u'l', u'ero', u'avremo', u'quella', u'facendo', u'stava', u'avrai', u'fece',
                    u'starebbero', u'facessi', u'ed', u'feci', u'stemmo', u'stiamo', u'sarebbe', u'stesse',
                    u'facevamo', u'facessimo', u'siano', u'sei', u'avrebbero', u'miei', u'nel', u'stiano',
                    u'sua', u'dei', u'dagl', u'facciano', u'sul', u'suoi', u'per', u'stessero', u'avrete',
                    u'lei', u'lui', u'facevi', u'starei', u'sugl', u'faceva', u'dalla', u'sareste', u'eravamo',
                    u'nello', u'saresti', u'nella', u'faremo', u'eravate', u'anche', u'nelle', u'agli', u'avuti',
                    u'foste', u'avuto', u'tuo', u'tua', u'negli', u'come', u'tue', u'avute', u'fummo', u'gli',
                    u'c', u'avreste', u'quelle', u'stavate', u'\xe8', u'stavano', u'questo', u'questi', u'o',
                    u'avresti', u'una', u'chi', u'coi', u'fui', u'staranno', u'col', u'dalle', u'con',
                    u'star\xe0', u'ci', u'questa', u'stanno', u'avrebbe', u'furono', u'avevamo', u'perch\xe9',
                    u'tuoi', u'stavamo', u'degl', u'avuta', u'staremo', u'tutto', u'degli', u'che', u'fossero',
                    u'tutti', u'dove', u'sarai', u'avremmo', u'facciate', u'quante', u'facesti', u'starete',
                    u'quanta', u'abbiate', u'quanto', u'quanti', u'contro', u'avessi', u'faranno', u'far\xe0',
                    u'queste', u'ebbero', u'voi', u'siamo', u'agl', u'ho', u'farete', u'far\xf2', u'abbiamo',
                    u'farebbe', u'ha', u'sarebbero', u'abbia', u'quale', u'avessimo', u'facessero', u'saranno',
                    u'ma', u'sta', u'abbiano', u'dagli', u'avrei', u'sto', u'mi', u'ebbe', u'dello', u'facevate',
                    u'un', u'del', u'era', u'avevano', u'stareste', u'delle', u'eri', u'della', u'facevano',
                    u'faremmo', u'faceste', u'ad', u'stavi', u'ai', u'vi', u'stetti', u'in', u'al', u'avesse',
                    u'sull', u'vostri', u'saremmo', u'il', u'io', u'vostro', u'vostra', u'avevate', u'vostre',
                    u'staremmo', u'faccio', u'fosti', u'avemmo', u'mio', u'fossi', u'mia', u'sar\xe0', u'mie',
                    u'ne', u'stia', u'dallo', u'star\xf2', u'sar\xf2', u'siete', u'avessero', u'staresti', u'avevo',
                    u'avevi', u'fu', u'facciamo', u'dall', u'aveva', u'sue', u'erano', u'dai', u'essendo', u'stesti',
                    u'sullo', u'sulla', u'sono', u'sulle', u'stai', u'a', u'sugli', u'e', u'avranno', u'i', u'hanno',
                    u'farebbero', u'nei', u'saremo', u'su', u'sui', u'suo', u'si', u'facemmo', u'fecero', u'stavo',
                    u'stessimo', u'uno', u'dov', u'fosse', u'se', u'siate']
        actual = self.stopwordManager.getStopwords()

        self.assertEqual(expected, actual)

    def test_finnish_stopwords(self):
        """
        Test the stopwords for the finnish language
        """
        self.stopwordManager = StopwordManager(language="fi")
        expected = [u't\xe4ksi', u'josta', u'olisitte', u'kenelle', u'noilta', u'keill\xe4',
                    u'n\xe4ilt\xe4', u'noissa', u'meiss\xe4', u'niiss\xe4', u'niill\xe4', u'silt\xe4',
                    u'olisin', u'keneen', u'kun', u'joissa', u'sinusta', u'teid\xe4n', u'niilt\xe4',
                    u'niiden', u'teid\xe4t', u'olisit', u'olivat', u'te', u'keihin', u'olimme', u'minun',
                    u'sinulta', u'joina', u'sinun', u'sinua', u'n\xe4ill\xe4', u'keist\xe4', u'kenest\xe4',
                    u'keit\xe4', u'me', u'kenelt\xe4', u'jossa', u'sit\xe4', u'sin\xe4', u'kanssa', u'sinut',
                    u'emme', u'ket\xe4', u'sinulla', u'tuosta', u'joista', u'meille', u'sinulle', u'jota', u'olin',
                    u'heihin', u'niit\xe4', u'n\xe4iss\xe4', u't\xe4lle', u'en', u'ei', u'ole', u'mihin', u'mukaan',
                    u'oli', u'kenell\xe4', u'mist\xe4', u'minulla', u'nuo', u'olemme', u'olit', u'et', u'sinussa',
                    u'jotka', u'ketk\xe4', u'minulta', u'meist\xe4', u'tuolta', u'siin\xe4', u'olette', u't\xe4n\xe4',
                    u'milt\xe4', u'mink\xe4', u'jolla', u'joilla', u'joille', u'teihin', u'kenen', u'olisivat',
                    u'jolle', u'meilt\xe4', u'n\xe4ille', u'tuolle', u'noista', u't\xe4st\xe4', u'mutta', u'tuo',
                    u'kenet', u'meihin', u'niille', u'ja', u'jolta', u'on', u'koska', u'noilla', u'olisi', u'joka',
                    u'meill\xe4', u'n\xe4iksi', u't\xe4t\xe4', u'heille', u'h\xe4n', u'noiden', u'jos', u'yli',
                    u'ovat', u'kuka', u'kein\xe4', u'h\xe4nelle', u'joihin', u't\xe4h\xe4n', u'olla', u'noin',
                    u'min\xe4', u'ett\xe4', u'siihen', u'n\xe4ihin', u'teill\xe4', u'n\xe4m\xe4', u'tuon',
                    u'niihin', u'n\xe4iden', u'vai', u'niist\xe4', u'teiss\xe4', u'eiv\xe4t', u'niin', u'keille',
                    u'keiksi', u'h\xe4nt\xe4', u'keneksi', u'minusta', u'kuin', u'teit\xe4', u'ollut', u'mill\xe4',
                    u'teilt\xe4', u'tuossa', u'noille', u'johon', u'keness\xe4', u'joiden', u'he', u'sinuun', u'olet',
                    u'teist\xe4', u'olisimme', u'joilta', u'sille', u'minulle', u'siksi', u'heid\xe4n', u'minua', u'tuolla',
                    u'keilt\xe4', u'minussa', u'olen', u'niiksi', u'minut', u'sek\xe4', u'heilt\xe4', u'h\xe4nell\xe4',
                    u't\xe4ss\xe4', u'heid\xe4t', u'vaan', u'h\xe4nen', u'heit\xe4', u'tuoksi', u'ette', u'h\xe4net',
                    u'joiksi', u'minuun', u'teille', u'noita', u'sen', u'h\xe4nelt\xe4', u't\xe4m\xe4', u'miksi',
                    u'tai', u'vaikka', u'noiksi', u'heill\xe4', u'miss\xe4', u'meit\xe4', u'ne', u'nyt', u'jona',
                    u'n\xe4in\xe4', u'keiss\xe4', u'mille', u'itse', u'olitte', u'mik\xe4', u'keiden', u'olleet',
                    u't\xe4lt\xe4', u'kenen\xe4', u'n\xe4ist\xe4', u'meid\xe4t', u'noina', u'tuohon', u'tuona',
                    u'meid\xe4n', u'tall\xe4', u'heiss\xe4', u'joksi', u'h\xe4nest\xe4', u'jonka', u'h\xe4neen',
                    u'poikki', u'joita', u'sill\xe4', u't\xe4m\xe4n', u'niin\xe4', u'h\xe4ness\xe4', u'mitk\xe4',
                    u'heist\xe4', u'n\xe4it\xe4', u'mit\xe4', u'tuot\xe4', u'siit\xe4', u'noihin', u'se']
        actual = self.stopwordManager.getStopwords()
        self.assertEqual(expected, actual)

    def test_french_stopwords(self):
        """
        Test the stopwords for the french language
        """
        self.stopwordManager = StopwordManager(language="fr")
        expected = [u'e\xfbtes', u'\xeates', u'aient', u'auraient', u'aurions', u'auras', u'serait',
                    u'le', u'serais', u'mais', u'la', u'eue', u'tu', u'ayante', u'eux', u'aux', u'te',
                    u'eus', u'ta', u'aurais', u'aviez', u'de', u'ayantes', u'f\xfbtes', u'moi', u'sont',
                    u'mon', u'ayant', u'serez', u'du', u'nos', u'aurez', u'eussiez', u'qu', u'd', u'furent',
                    u'f\xfbt', u'\xe9t\xe9e', u'soient', u'leur', u't', u'\xe9t\xe9s', u'seriez', u'en',
                    u'ses', u'avons', u'l', u'eu', u'et', u'sommes', u'tes', u'aurait', u'es', u'est',
                    u'eurent', u'serions', u'sur', u'lui', u'soyons', u'ayants', u'\xe9tais', u'soyez',
                    u'que', u'mes', u'qui', u'je', u'm\xeame', u'\xe0', u'c', u'ayons', u's', u'e\xfbmes',
                    u'une', u'ou', u'\xe9tait', u'\xe9t\xe9', u'\xe9tants', u'\xe9t\xe9es', u'ce', u'son',
                    u'auriez', u'des', u'\xe9tante', u'ont', u'avez', u'f\xfbmes', u'avait', u'avec',
                    u'fussions', u'seraient', u'suis', u'eussions', u'toi', u'ton', u'eues', u'vous', u'aies',
                    u'on', u'auront', u'aurons', u'avions', u'eut', u'me', u'fut', u'ma', u'fus', u'fussent',
                    u'ait', u'j', u'dans', u'pour', u'n', u'seras', u'un', u'serai', u'sera', u'aie', u'ayez',
                    u'avaient', u'aurai', u'votre', u'\xe9tiez', u'ai', u'eusse', u'\xe9taient', u'eussent',
                    u'eusses', u'\xe9tantes', u'soit', u'as', u'au', u'il', u'sois', u'vos', u'\xe9tions',
                    u'par', u'pas', u'fusses', u'fussiez', u'ne', u'\xe9tant', u'seront', u'serons', u'aura',
                    u'avais', u'e\xfbt', u'notre', u'elle', u'nous', u'fusse', u'm', u'y', u'ces', u'sa', u'se']
        actual = self.stopwordManager.getStopwords()
        self.assertEqual(expected, actual)

    def test_swedish_stopwords(self):
        """
        Test the stopwords for the swedish language
        """
        self.stopwordManager = StopwordManager(language="sv")
        expected = [u'vart', u'vars', u'oss', u'vara', u'och', u's\xe5dant', u'alla',
                    u'd\xe4r', u'hade', u's\xe5dana', u'allt', u'under', u'jag', u'har', u'vem',
                    u'ditt', u'fr\xe5n', u'utan', u'de', u'mot', u'dina', u's\xe5dan', u'du', u'din',
                    u'dig', u'sin', u'vilket', u'denna', u'v\xe5rt', u'mycket', u'upp', u'\xe4n',
                    u'n\xe5got', u'en', u'ej', u'skulle', u'n\xe5gon', u'er', u'v\xe5r', u'sitta',
                    u'bli', u'deras', u'f\xf6r', u'era', u'med', u'd\xe5', u'icke', u'ju', u'mitt',
                    u'men', u'mellan', u'inom', u'sina', u'honom', u'han', u'ett', u'vilken', u'att',
                    u'inte', u'samma', u'vid', u'hennes', u'som', u'sedan', u'blev', u'\xe5t', u'sj\xe4lv',
                    u'ingen', u'vad', u'kunde', u'mina', u'var', u'\xf6ver', u'vilka', u'blivit', u'om',
                    u'hur', u'varit', u'ha', u'h\xe4r', u'ert', u'ut', u'det', u'varje', u'dem', u'den',
                    u'vilkas', u'n\xe4r', u's\xe5', u'vi', u'efter', u'blir', u'av', u'ni', u'min', u'hon',
                    u'eller', u'mig', u'henne', u'till', u'sig', u'p\xe5', u'nu', u'n\xe5gra', u'dessa',
                    u'kan', u'detta', u'v\xe5ra', u'hans', u'dess', u'\xe4r', u'man', u'i', u'varf\xf6r']
        actual = self.stopwordManager.getStopwords()
        self.assertEqual(sorted(expected), sorted(actual))



    def test_filtering_words(self):
        """
        Test how to filter a list of strings using the StopwordManager
        """
        self.stopwordManager = StopwordManager(language="en")
        expected = ["Tree", "Tall"]

        words = ["The", "Tree", "is", "Tall"]
        actual = self.stopwordManager.filterStopWords(words)
        self.assertEqual(expected, actual)

    def test_language_not_available(self):
        """
        Test when a not available language is given in input to the StopwordManager
        """
        language="not_valid_language"
        filename=None
        self.assertRaises(ValueError, StopwordManager, filename, language)

    def helper_readFilename(self, filename=''):
        stopwords = []
        if not filename:
            raise Exception("The file is empty")

        fileToRead = "%s%s" % (self.stopwordsDirectory, filename)

        f = open(fileToRead, 'r')
        lines = f.readlines()
        f.close()

        stopwords = filter(None, map(lambda x: x.split('|')[0].strip().lower().decode('utf-8'), lines))
        return stopwords

if __name__ == '__main__':
    unittest.main()
