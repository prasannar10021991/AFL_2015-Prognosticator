#This code is used to generate the keys for searching in the web.
#-----------------------------------------------------------------------
#import regex
import re

def processTweet(tweet):
    '''process the tweets'''
    key = re.search('(?<=#)\w+',tweet)
    if(key == None):
        return key
    else:
        return key.group(0)
#end 

def removeDuplicates(stopWordListFileName):
    '''read the Hashkeylist.txt file and removes duplicate'''
    hashkeys = []
    fkeylist = open('D:\Test\hashkeylist.txt', 'r')
    line = fkeylist.readline()
    while line:
        word = line.strip()
        if (word not in hashkeys):
		   stopWords.append(word)
        line = fStopList.readline()
    fStopList.close()
    return hashkeys
#end

fRead = open('D:\Test\hashjunk.txt','r')
fWrite = open('D:\Test\hashkeylist.txt','w')
tweet = fRead.readline()

while tweet:
	hashkeys = []
	hashKey = processTweet(tweet)
	if ((hashKey != None) and (hashKey not in hashkeys)):
	    print >> fWrite,'#%s' %hashKey
	    hashkeys.append(hashKey)
	tweet = fRead.readline()
#end-loop

fRead.close()
fWrite.close()