Readme Instructions
-------------------

accuracy.py: This program is used to calculate the accuracy given on a test set by a classfier. The results also provide the details of number of truepositives for every class ( positive, negative and neutral). 

firstrun.py: This program implements Naive Bayes Classifier provided by NLTK. Based on training set feature set is derived and then used to classify the development set. 

firstrunsvm.py: This program implements Support Vector Machine provided by NLTK. Based on training set feature set is derived and then used to classify the development set. 

arffdata.py: This program is used to generate arff format file of a training, test and development set for WEKA. The files created are compatible with WEKA(3.6). 

predictor.py: This prgram calculated the typicality score, mean  and median of negative to postive tweet ratio before and after the match and uses them to predict the outcome of a given match. It predicts the winner, final score margin and people's predicted choice for a match. 

hashkey.py: This program is used to generate keys, to be used for harvesting. 

keygenerator.py: This program is used to create keys based on token permutation and combination, to be used for harvesting.  

