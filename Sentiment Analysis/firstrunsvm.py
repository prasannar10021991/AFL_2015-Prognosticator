#This is the SVM implementation of NLTK. 
# this code is used from web source : 
# http://ravikiranj.net/posts/

import sys
import csv
import re
import svmutil
import nltk
from svmutil import *

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



def getSVMFeatureVectorAndLabels(tweets, featureList):
    sortedFeatures = sorted(featureList)
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
        elif(tweet_opinion == 'neutral'):
            label = 2
        labels.append(label)
    #return the list of feature_vector and labels
    return {'feature_vector' : feature_vector, 'labels': labels}
#end


def getSVMFeatureVector(test_tweets, featureList):
    sortedFeatures = sorted(featureList)
    map = {}
    feature_vector = []
    for t in tweets:
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
        
    #return the list of feature_vector and labels
    return feature_vector
#end

inpTweets = csv.reader(open('C:\\Users\\kaushik\\Desktop\\New folder\\TrainingSet1.csv',"rU"), dialect='excel-tab') #delimiter =',', quotechar = '|')
inpTweets1 = csv.reader(open('C:\Users\kaushik\Desktop\New folder\\TrainingSet2.csv',"rU"), dialect='excel-tab') #delimiter =',', quotechar = '|')
outTweet = csv.writer(open('C:\Users\kaushik\Desktop\New folder\\TestResultSVM.csv',"wb"), dialect='excel-tab')

try:
	ffv = open('C:\Users\kaushik\Desktop\New folder\\FeatureVectorSVM.txt', 'w')
except IOError, message:  # file open failed
	print "File could not be opened:", message
	sys.exit(1)
	
 
try:
	fts = open('C:\Users\kaushik\Desktop\New folder\\TrainingSetSVM.txt', 'w')
except IOError, message:  # file open failed
	print "File could not be opened:", message
	sys.exit(1)


stopWords = []	
st = open('C:\Users\kaushik\Desktop\New folder\\StopWords.txt', 'r')
stopWords = getStopWordList('C:\Users\kaushik\Desktop\New folder\\StopWords.txt')

featureList = []
tweets = []
for row in inpTweets:
	sentiment = row[0]
	tweet = row[1]
	featureVector = getFeatureVector(tweet, stopWords)
	print >> ffv, featureVector
	featureList.extend(featureVector)
	tweets.append((featureVector, sentiment));
	
#Train the classifier
result = getSVMFeatureVectorAndLabels(tweets, featureList)
problem = svm_problem(result['labels'], result['feature_vector'])
#'-q' option suppress console output
param = svm_parameter('-q')
param.kernel_type = LINEAR
classifier = svm_train(problem, param)
#svm_save_model(classifierDumpFile, classifier)

print >> fts, result	

# Remove featureList duplicates
featureList = list(set(featureList))

fts.close()

# Test the classifier
test_tweets =[]
for row in inpTweets1:
	manualSentiment = row[0]
	testTweet = row[1]
	featureVector = getFeatureVector(testTweet, stopWords)
	test_tweets.append((featureVector,manualSentiment));
	
test_feature_vector = getSVMFeatureVector(test_tweets, featureList)

#p_labels contains the final labeling result
p_labels, p_accs, p_vals = svm_predict([0] * len(test_feature_vector),test_feature_vector, classifier)
outTweet.writerow((p_labels))