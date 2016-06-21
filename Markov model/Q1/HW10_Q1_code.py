# -*- coding: utf-8 -*-
"""
Created on Sun May 01 15:31:02 2016

@author: Aatman
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 22:54:26 2016

@author: Aatman
"""


__author__ = 'Aatman'

from sklearn.linear_model import LogisticRegression
from sklearn import svm
import pylab as pl
import numpy as np
from sklearn import cross_validation
from sklearn.grid_search import GridSearchCV
import json

tweets = []
for line in open('HW10_Q1_training.txt').readlines():
    tweets.append(json.loads(line))

global a
a = 0

# Generate X and y

#Generating X by using freq. of Cities. If all 3 cities occur together and thier total freq. is more than 3 then I have given a label 1 or else 0.
X = []
y = []
for class_label, text in tweets:
    x=[]
    frequency = 0
    
    
    
    for i in text:
        if(i == "Seattle" or i == "Philapedia" or i=="Boston"):
            frequency+=1
            
        if (frequency>3):
            a+=1
            x.append(1)
        else:
            x.append(0)
		         
            
        
            
            
    y.append(class_label)
    X.append(x)


# 10 folder cross validation 
svc = svm.SVC(kernel='linear')
Cs = range(1,5)
clf = GridSearchCV(estimator=svc, param_grid=dict(C=Cs), cv = 10)
clf.fit(X, y)


tweets = []
for line in open('HW10_Q1_testing.txt').readlines():
    tweets.append(json.loads(line))


X = []
for text in tweets:
	x=[]
	frequency = 0
	
	for i in text:
		
		if(i == "Seattle" or i == "Philapedia" or i=="Boston"):
			frequency+=1
			
			
		if (frequency>3):
			a+=1
			
			x.append(1)
			
			
		else:
			x.append(0)
			
			
	X.append(x)
y = clf.predict(X)

f = open('HW10_Q1_predictions.txt', 'w')
for  idx,text in enumerate(tweets):
    f.write(json.dumps(y[idx]) + '\r\n')
f.close()