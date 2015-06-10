#this program implements NLTK's Naive Bayes Classifier. 
# this code is used from web source : http://ravikiranj.net/posts/

import csv
import re
import nltk

def processTweet(tweet):
    '''process the tweets'''

    #Convert to lower case
    tweet = tweet.lower()
    #Convert www.* or https?://* to URL
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','URL',tweet)
    #Convert @username to AT_USER
    #tweet = re.sub('@[^\s]+','AT_USER',tweet)
    #Remove additional white spaces
    tweet = re.sub('[\s]+', ' ', tweet)
    #Replace #word with word
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    #trim
    tweet = tweet.strip('\'"')
    return tweet
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

#start getfeatureVector
def getFeatureVector(tweet, stopWords):
	featureVector = []
	alligator = 0
	effect = 0
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

#start replaceTwoOrMore
def replaceTwoOrMore(s):
    #look for 2 or more repetitions of character and replace with the character itself
    pattern = re.compile(r"(.)\1{1,}", re.DOTALL)
    return pattern.sub(r"\1\1", s)
#end

#start extract_features
def extract_features(tweet):
    tweet_words = set(tweet)
    features = {}
    for word in featureList:
        features['contains(%s)' % word] = (word in tweet_words)
    return features
#end

inpTweets = csv.reader(open('D:\\Test\\1801.csv',"rU"), dialect='excel-tab') #delimiter =',', quotechar = '|')
inpTweets1 = csv.reader(open('D:\\Test\\matches\\round6\\melbvssydneyTweets.csv',"rU"), dialect='excel-tab') #delimiter =',', quotechar = '|')
outTweet = csv.writer(open('D:\\Test\\matches\\round6\\ResultmelbvssydneyTweets.csv',"wb"), dialect='excel-tab', quotechar="",quoting = csv.QUOTE_NONE)

try:
	ffv = open('D:\Test\FeatureVector3.txt', 'w')
except IOError, message:  # file open failed
	print "File could not be opened:", message
	sys.exit(1)


stopWords = []	
st = open('D:\\Test\\StopWords.txt', 'r')
stopWords = getStopWordList('D:\\Test\\StopWords.txt')

featureList = []
tweets = []
for row in inpTweets:
	sentiment = row[0]
	tweet = row[1]
	featureVector = getFeatureVector(tweet, stopWords)
	print >> ffv, featureVector
	featureList.extend(featureVector)
	tweets.append((featureVector, sentiment));
	

 
#try:
#	fts = open('D:\Test\TrainingSet3.txt', 'w')
#except IOError, message:  # file open failed
#	print "File could not be opened:", message
#	sys.exit(1)
	
# Remove featureList duplicates
featureList = list(set(featureList))

# Generate the training set
training_set = nltk.classify.util.apply_features(extract_features, tweets)
#print >> fts, training_set

#fts.close()

# Train the Naive Bayes classifier
NBClassifier = nltk.NaiveBayesClassifier.train(training_set)

# Test the classifier

for row in inpTweets1:
	try:
		name = row[0]
	except IndexError, message:
		print" row:", message
		continue
	stweet = name.split(":::")
	try:
		tweet1 = processTweet(stweet[2])
		time = stweet[1]
		time_part = time.split()
	except IndexError, message:
		print "index out of range:",message
		continue
	testTweet = tweet1
	month = time_part[1]
	date = time_part[2]
	time = time_part[3]
	sentiment = NBClassifier.classify(extract_features(getFeatureVector(testTweet, stopWords)))
	outTweet.writerow((sentiment,testTweet,month,date,time))

