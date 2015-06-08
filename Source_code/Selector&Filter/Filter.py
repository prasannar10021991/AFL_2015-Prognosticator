#import regex
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
    #tweet = re.sub('@[^\s]+','AT_USER',tweet)
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

try:
    fRead = csv.reader(open('I:\\RP\\New folder (2)\\collingwoodvsessendonrd4.csv',"rU"),dialect='excel-tab') # delimiter = '',quotechar = ':',doublequote=True) #
    fWrite = open('I:\\RP\\New folder (2)\\firsttweets2.txt',"w")
except IOError, message: 
    print "File could not be opened:",message



for row in fRead:
    try:
        name = row[0]
    except IndexError, message:
        print" row:", message
        continue
    stweet = name.split(":::")
    try:
        tweet = processTweet(stweet[2])
    except IndexError, message:
        print "index out of range:",message
        continue
    sentiment = ""
    if(tweet.find("rt @")==-1):
        print >> fWrite,'|%s|,|%s|' %(sentiment,tweet)
 
    
fWrite.close()
#end loop

#
