import re
import csv

#start process_tweet
def processTweet(tweet):
    '''process the tweets'''

    #Convert to lower case
    tweet = tweet.lower()
    #Convert www.* or https?://* to URL
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','URL',tweet)
    #Convert @username to AT_USER
    tweet = re.sub('@[^\s]+','AT_USER',tweet)
    #Remove additional white spaces
    tweet = re.sub('[\s]+', ' ', tweet)
    #Replace #word with word
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    #trim
    tweet = tweet.strip('\'"')
    return tweet
#end

#start replaceTwoOrMore
def replaceTwoOrMore(s):
    #look for 2 or more repetitions of character and replace with the character itself
    pattern = re.compile(r"(.)\1{1,}", re.DOTALL)
    return pattern.sub(r"\1\1", s)
#end

#start getStopWordList
def getStopWordList(stopWordListFileName):
    #read the stopwords file and build a list
    stopWords = []
    stopWords.append('AT_USER')
    stopWords.append('URL')

    fStopList = open(stopWordListFileName, 'r')
    line = fStopList.readline()
    while line:
        word = line.strip()
        stopWords.append(word)
        line = fStopList.readline()
    fStopList.close()
    return stopWords
#end

def writeHeader(sortedFeatures1):
	outArff = open('D:\\Test\\arffTrainingSet2-1.csv',"w") #, dialect = 'excel', delimiter =' ', quotechar = '|', quoting = csv.QUOTE_NONE)
	s = '@relation trainingSet'
	print>>outArff,s
	print>>outArff, ' '
	for y in sortedFeatures1:
		print>>outArff,'@attribute %s numeric'%y
	print>>outArff,'@attribute sentiment {0,1,2}'
	print>>outArff, ' '
	print>>outArff, '@data'
	outArff.close()

def getSVMFeatureMapAndLabels(tweets, featureList1):
	outArff1 = csv.writer(open('D:\\Test\\arffTrainingSet2-1.csv',"ab"), dialect = 'excel', delimiter =',', quotechar = '', quoting = csv.QUOTE_NONE)
	sortedFeatures = sorted(featureList1)
	#sortedFeatures = list(set(sortedFeatures))
	sortedFeatures1 = sortedFeatures
	#sortedFeatures1.append('sentiment')
	writeHeader(sortedFeatures1)
	#outArff.writerow(sortedFeatures1)
	map = {}
	feature_vector = []
	labels = []
	for t in tweets:
		label = 0
		map = {}
		#Initialize empty map
		for w in sortedFeatures:
			map[w] = 0
			tweet_words = t[0]
			tweet_opinion = t[1]
			#Fill the map
			for word in tweet_words:
				#process the word (remove repetitions and punctuations)
				word = replaceTwoOrMore(word)
				word = word.strip('\'"?,.')
				#set map[word] to 1 if word exists
				if word in map:
					map[word] = 1
				#end for loop
		values = map.values()
		feature_vector.append(values)
		if(tweet_opinion == 'positive'):
			label = 0
		elif(tweet_opinion == 'negative'):
			label = 1
		elif(tweet_opinion == 'neutrino'):
			label = 2
		values.append(label)
		outArff1.writerow((values))	
	 
    #return the list of feature_vector and labels
    #return {'feature_vector' : feature_vector, 'labels': labels}
#end

#start getfeatureVector
def getFeatureVector(tweet, stopWords):
	featureVector = []
	#split tweet into words
	words = tweet.split()
	for w in words:
		#replace two or more with two occurrences
		w = replaceTwoOrMore(w)
		#strip punctuation
		w = w.strip('\'"?,.')
		#check if the word stats with an alphabet
		val = re.search(r"^[a-zA-Z][a-zA-Z0-9]*$", w)
		#ignore if it is a stop word
		if(w in stopWords or val is None):
			continue
		else:
			featureVector.append(w.lower())
	return featureVector
#end

inpTweets = csv.reader(open('D:\\Test\\TrainingSet2-1.csv',"rU"), dialect='excel-tab') #delimiter =',', quotechar = '|')
#outArff = csv.writer(open('D:\\Test\\arffTraining2.csv',"wb"), delimiter =';', quotechar = '', quoting = csv.QUOTE_NONE)

stopWords = []	
st = open('D:\Test\StopWords.txt', 'r')
stopWords = getStopWordList('D:\Test\StopWords.txt')


try:
	ffv = open('D:\Test\FeatureList.txt', 'r')
except IOError, message:  # file open failed
	print "File could not be opened:", message
	sys.exit(1)

featureList = []
tweets = []
for row in inpTweets:
	sentiment = row[0]
	tweet = processTweet(row[1])
	featureVector = getFeatureVector(tweet, stopWords)
	featureList.extend(featureVector)
	#outfeature.writerow((featureVector))
	tweets.append((featureVector, sentiment));

	# Remove featureList duplicates

lineA = ffv.readline()
featureList1 =[]
while lineA:
	lineA = lineA.strip()
	word = lineA.split(",")
	featureList1.extend(word)
	lineA = ffv.readline()
ffv.close()

featureList1 = list(set(featureList1))

getSVMFeatureMapAndLabels(tweets, featureList1)