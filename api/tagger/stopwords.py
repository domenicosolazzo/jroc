def readStopWordsFile(file):
    f = open(file, 'r')
    lines = f.readlines()
    f.close()
    return lines

# Reads the file and puts the stop words into a list.
def getStopWords(file_name):
	return filter(None, map(lambda x: x.split('|')[0].strip().lower(), readStopWordsFile(file_name)))

# Remove stop words from a list.
def filterStopWords(stopwords, to_filter):
	return filter(lambda x: not x.lower() in stopwords, to_filter)
