#This program predicts the outcome of the match. 
# It makes three predictions:
# 1) winner of an outcome 2) Forecasted winner 3) victory margin
#-----------------------------------------------------------------------
import statistics
import csv
import math
import datetime

items1 = [0.0]
items1before = [0.0]
items1after = [0.0]

items2 = [0.0]
items2before = [0.0]
items2after = [0.0]

count1 = 0
count2 = 0

format = '%Y-%m-%d %H:%M:%S'
matchTime1 = '1900-05-01 19:50:00' 
matchTime = datetime.datetime.strptime(matchTime1,format)

inpTweets1 = csv.reader(open('D:\\Test\\matches\\round5\\ResultcarltonMetaData.csv',"rU"), dialect='excel-tab')
inpTweets2 = csv.reader(open('D:\\Test\\matches\\round5\\ResultcollingwoodMetaData.csv',"rU"), dialect='excel-tab')

for row in inpTweets1:
	timestamp = row[2]
	time = datetime.datetime.strptime(timestamp,format)
	neutral1 = row[3]
	positive1 = row[4]
	negative1 = row[5]
	ratioNP1 = row[7]
	floatratio1 = float(ratioNP1)
	count1 += 1
	
	#skiping the first 40 entries in graph(to remove unstable part)
	if (count1 > 40):
		if (time < matchTime):
			items1before.append(floatratio1)
		else:
			items1after.append(floatratio1)
		items1.append(floatratio1)
		
neuCount1 = float(neutral1)
posCount1 = float(positive1)
negCount1 = float(negative1)
totaltweet1 = negCount1 + posCount1 + neuCount1

i1 = statistics.median(items1)
i1before = statistics.median(items1before)
i1after = statistics.median(items1after)

j1 = statistics.mode(items1)
j1before = statistics.mode(items1before)
j1after = statistics.mode(items1after)

k1 = statistics.mean(items1)
k1before = statistics.mean(items1before)
k1after = statistics.mean(items1after)

print"TeamA Stats"
print"median:", i1
print"mode:", j1
print"mean:", k1
print"Final:", floatratio1

for row1 in inpTweets2:
	neutral2 = row1[3]
	positive2 = row1[4]
	negative2 = row1[5]
	ratioNP2 = row1[7]
	floatratio2 = float(ratioNP2)
	count2 += 1
	
#skiping the first 40 entries in graph(to remove unstable part)	
	if (count2 > 40):
		if (time < matchTime):
			items2before.append(floatratio1)
		else:
			items2after.append(floatratio1)
		items2.append(floatratio2)

neuCount2 = float(neutral2)
posCount2 = float(positive2)
negCount2 = float(negative2)
totaltweet2 = negCount2 + posCount2 + neuCount2

i2 = statistics.median(items2)
i2before = statistics.median(items2before)
i2after = statistics.median(items2after)

j2 = statistics.mode(items2)
j2before = statistics.mode(items2before)
j2after = statistics.mode(items2after)

k2 = statistics.mean(items2)
k2before = statistics.mean(items2before)
k2after = statistics.mean(items2after)

print"TeamB Stats"
print"median:", i2
print"mode:", j2
print"mean:", k2
print"Final:", floatratio2

# This function calculated the typicality score
def typicalityCoefficient(x):
	coEff = math.log(x,2)
	if (coEff < 0):
		coEff = coEff*(-1)
	return coEff

# this calculates the ratio of number of tweets for each team
def typicalityCheck(x,y):
	p = 0.0
	p = x/y
	return p
	
# the difference between two numbers
def resultantDifference(x,y):
	num1 = x
	num2 = y
	if (num1 > num2):
		dif = num1 - num2 
	elif (num2>num1):
		dif = num2 - num1
	return dif
	
typRatio = typicalityCheck(totaltweet1,totaltweet2)
if (typRatio != 1):
	typCoEff = typicalityCoefficient(typRatio)
else:
	typCoEff = 1
	wti1 = i1*typCoEff
	wtk1 = k1*typCoEff
	wtNP1 = floatratio1*typCoEff
	wti2 = i2*typCoEff
	wtk2 = k2*typCoEff
	wtNP2 = floatratio2*typCoEff
	
if ((typCoEff > 0.0) and (typCoEff <= 0.25)):
	wti1 = i1
	wtk1 = k1
	wtNP1 = floatratio1
	wti2 = i2
	wtk2 = k2
	wtNP2 = floatratio2
elif ((typCoEff > 0.25) and (typCoEff <= 0.80)):
	wti1 = i1*typCoEff
	wtk1 = k1*typCoEff
	wtNP1 = floatratio1*typCoEff
	wti2 = i2*typCoEff
	wtk2 = k2*typCoEff
	wtNP2 = floatratio2*typCoEff	
elif((typCoEff > 0.80) and (typCoEff < 1.0)):
	weight = 0.80
	wti1 = i1*weight
	wtk1 = k1*weight
	wtNP1 = floatratio1*weight
	wti2 = i2*weight
	wtk2 = k2*weight
	wtNP2 = floatratio2*weight
elif((typCoEff > 1.0) and (typCoEff < 1.20)):
	weight = 0.80
	wti1 = i1*weight
	wtk1 = k1*weight
	wtNP1 = floatratio1*weight
	wti2 = i2*weight
	wtk2 = k2*weight
	wtNP2 = floatratio2*weight
elif ((typCoEff >= 1.20)):
	wti1 = i1/typCoEff
	wtk1 = k1/typCoEff
	wtNP1 = floatratio1/typCoEff
	wti2 = i2/typCoEff
	wtk2 = k2/typCoEff
	wtNP2 = floatratio2/typCoEff	
	
print "Typ Coeff:",typCoEff
print"Weighted values of team1"
print wti1
print wtk1
print wtNP1
print"Weighted values of team2"
print wti2
print wtk2
print wtNP2	

#the following is executed under minute difference in the typicality coefficient score
if (resultantDifference(wtNP1,wtNP2) < 0.10):
	if ((i1 <= k1) and (i2 <= k2)):
		if ((i1after<i1before) and (i2after<i2before) and (ratioNP1<ratioNP2)):
			print "Team A won the match"
		elif ((i1after<i1before) and (i2after<i2before) and (i1after<i2after)):
			print "Team A won the match"
		elif ((i1after<i1before) and (i2after<i2before)):
			print "TeamB won the match"
		elif ((i1after<i1before) and (i2after>i2before) and (ratioNP1<ratioNP2)):
			print"Team A won the match"
		elif ((i1after<i1before) and (i2after>i2before) and (i1after<i2after)):
			print "TeamA won the match"
		elif ((i1after<i1before) and (i2after>i2before)):
			print "TeamB won the match"
		elif ((i1after>i1before) and (i2after>i2before)and (ratioNP1<ratioNP2)):
			print "TeamA won the match"
		elif ((i1after>i1before) and (i2after>i2before)and (i1after<i2after)):
			print "Team A won the match"
		elif ((i1after>i1before) and (i2after>i2before)):
			print "Team B won the match"
		elif ((i1after>i1before) and (i2after<i2before) and (ratioNP2<ratioNP1)):
			print "TeamB won the match"
		elif ((i1after>i1before) and (i2after<i2before) and (i2after<i1after)):
			print "TeamB won the match"
		elif ((i1after>i1before) and (i2after<i2before)):
			print "Team A won the match"
		elif ((i1after == i1before) and (i2after < i2before)):
			print "Team B won"
		elif ((i1after == i1before) and (i2after > i2before)):
			print "Team A won"
		elif ((i1after < i1before) and (i2after == i2before)):
			print "Team A won"
		elif ((i1after > i1before) and (i2after == i2before)):
			print "Team B won"
	# the follwing elifs consider the cases where median becomes greater than mean
	elif ((i1 <= k1) and (i2 > k2)):
		if (ratioNP1 < ratioNP2):
			if (resultantDifference(i2,k2) >0.10):
				print "Team B won the match"
				print "hit2"
			else: 
				print"Team A won the match"
		else:
			print"Team B won the match"
	elif ((i1 > k1) and (i2 <= k2)):
		if (ratioNP2 < ratioNP1):
			if (resultantDifference(i1,k1) > 0.10):
				print "Team A won the match"
				print "hit3"
			else:
				print "Team B won the match"
		else:
			print"Team A won the match"
	elif ((i1 > k1) and (i2 > k2)):
		if (ratioNP1 < ratioNP2):
			print "Team A won the match"
		else:
			print"Team B won the match"
#the following is executed usually 
else:
	if (ratioNP1 < ratioNP2):
		print "Team A won the match"
	else:
		print"Team B won the match"

#the following is executed to predict who do people think would win the contest
if (k1before<k2before):
	print "TEAM A IS THE CHOICE"
else:
	print "TEAM B IS THE CHOICE"

#the following predicts the victory margin of the contest
if (resultantDifference(wtNP1,wtNP2) <= 0.10):
	print "Low Final Score Margin"
elif (resultantDifference(wtNP1,wtNP2) <= 0.20):
	print"Medium Final Score Margin"
elif (resultantDifference(wtNP1,wtNP2) <= 0.30):
	print"High Final Score Margin"
else:
	print"Very High Final Score Margin"

