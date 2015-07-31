def readStopWordsFile(file):
    f = open(file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def filterStopWords(line):
    return line.split('|')[0].strip()

def getStopWords(file_name):
	return filter(None, map(filterStopWords, readStopWordsFile(file_name)))
