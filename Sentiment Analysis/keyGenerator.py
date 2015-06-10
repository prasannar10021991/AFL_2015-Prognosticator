#One of the programs used to generate keywords for search in harvesting
#------------------------------------------------------------------------

#import regex
import re
import itertools
import csv

fRead = csv.reader(open('D:\\Test\\tigers.csv',"rb"),dialect='excel-tab')
fWrite = open('D:\\Test\\tigerskeylist.txt',"w")

key = []
for row in fRead:
	name = row[1]
	rawKey = name.split()
	keyLength = len(rawKey)
	for i in range(1,keyLength+1):
		keyPermutation = list(itertools.permutations(rawKey, i))
		str = ""
		keyCombined = []
		for w in keyPermutation:
			keyCombined = str.join(w)
			if (w not in key):
				print >> fWrite,keyCombined
				key.append(keyCombined)
	
fWrite.close()