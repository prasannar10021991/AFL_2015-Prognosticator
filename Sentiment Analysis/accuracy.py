import csv

inpTweets = csv.reader(open('D:\\Test\\TestResult3.csv',"rU"), dialect='excel-tab') # delimiter =',', quotechar = '|')
outTweet = csv.writer(open('D:\\Test\\TestResultAccuracy3.csv',"wb"), dialect='excel-tab')

tweets = []
totalTruePos = 0.0
totalFalsePos = 0.0
totalTrueNeg = 0.0
totalFalseNeg = 0.0 
totalTrueNut = 0.0
totalFalseNut = 0.0
totalTrue = 0.0

for row in inpTweets:
	predictedSentiment = row[0]
	realSentiment = row[1]
	tweet = row[2]
	outcome=""
	if (predictedSentiment == 'positive') and (predictedSentiment == realSentiment):
		outcome = "TruePpositive"
		totalTruePos += 1
		totalTrue += 1
	elif (predictedSentiment == 'positive') and (predictedSentiment != realSentiment):
		outcome = "FalsePositive"
		totalFalsePos += 1
	elif (predictedSentiment == 'negative') and (predictedSentiment == realSentiment):
		outcome = "TrueNegative"
		totalTrueNeg += 1
		totalTrue += 1
	elif (predictedSentiment == 'negative') and (predictedSentiment != realSentiment):
		outcome = "FalseNegative"
		totalFalseNeg += 1
	elif (predictedSentiment == 'neutrino') and (predictedSentiment == realSentiment):
		outcome = "TrueNeutrino"
		totalTrueNut += 1
		totalTrue += 1
	elif (predictedSentiment == 'neutrino') and (predictedSentiment != realSentiment):
		outcome = "FalseNeutrino"
		totalFalseNut += 1
	else:
		outcome = "None"
	outTweet.writerow((outcome,predictedSentiment,realSentiment,tweet))
	
Accuracy = totalTrue/(totalTruePos+totalFalsePos+totalTrueNeg+totalFalseNeg+totalTrueNut+totalFalseNut)
P_Precision = totalTruePos/(totalTruePos+totalFalsePos)
N_Precision = totalTrueNeg/(totalTrueNeg+totalFalseNeg)
U_Precision = totalTrueNut/(totalTrueNut+totalFalseNut)
#outTweet.writerow()
outTweet.writerow((Accuracy,P_Precision,N_Precision,U_Precision))
