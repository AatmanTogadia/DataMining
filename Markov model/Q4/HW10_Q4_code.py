# -*- coding: utf-8 -*-
"""
Created on Sun May 01 21:32:44 2016

@author: Aatman
"""
import json
import numpy as np
from hmmlearn import hmm
import types

label = {0: "New York City", 1: "Boston", 2: "Washington D.C.",3:"Seattle",4:"Philapedia"}

tweets=[]
yy=[]
y = []
X = []
for line in open('HW10_Q4_training.txt').readlines():
    #print line
    tweets.append(json.loads(line))
    #tweets.pop(0)
    x = tweets[1:]
    #print  tweets
    #
    #print line
for items in tweets:
    yy = []
    x=[]
    #items.pop(0)
    for item in items[1]:
        #print item[1]
        
        if item[0]=="New York City":
            x.append([item[1]])
            yy.append(0)
        elif item[0]=="Boston":
            x.append([item[1]])
            yy.append(1)
        elif item[0]=="Washington D.C.":
            x.append([item[1]])
            yy.append(2)
        elif item[0]=="Seattle":
            x.append([item[1]])
            yy.append(3)
        elif item[0]=="Philapedia":
            x.append([item[1]])
            yy.append(4)
        #for i in items[0]:
            #print i
    
    
    #print y
    y.append(yy)
    X.append(x)
    

        
    

#print final_x   
#print final_y

tweets1=[]
#y1=[]
final_y1 = []
final_x1 = []
for line in open('HW10_Q4_testing.txt').readlines():
    #print line
    tweets1.append(json.loads(line))
    #print tweets1
    
    
    
for tt in tweets1:
    y1=[]
    
    
    for i in tt:
        y1.append([i])
    
    final_x1.append(y1)
    
#print final_x1[999]


class markovmodel:
    #transmat: None
    def __init__(self, transmat = None, startprob = None):
        self.transmat = transmat
        self.startprob = startprob
    # It assumes the state number starts from 0
    def fit(self, X):
        ns = max([max(items) for items in X]) + 1
        self.transmat  = np.zeros([ns, ns])
        self.startprob = np.zeros([ns])
        for items in X:
            n = len(items)
            self.startprob[items[0]] += 1
            for i in range(n-1):
                self.transmat[items[i], items[i+1]] += 1
        self.startprob = self.startprob / sum(self.startprob)
        n = self.transmat.shape[0]
        d = np.sum(self.transmat, axis=1)
        for i in range(n):
            if d[i] == 0:
                self.transmat[i,:] = 1.0 / n
        d[d == 0] = 1
        self.transmat = self.transmat * np.transpose(np.outer(np.ones([ns,1]), 1./d))

    def predict(self, obs, steps):
        pred = []
        n = len(obs)
        if len(obs) > 0:
            s = obs[-1]
        else:
            s = np.argmax(np.random.multinomial(1, self.startprob.tolist(), size = 1))
        for i in range(steps):
            s1 = np.random.multinomial(1, self.transmat[s,:].tolist(), size = 1)
            pred.append(np.argmax(s1))
            s = np.argmax(s1)
        return pred


# In[28]:

def hmm_predict_states(ghmm, obs, steps):
    y = ghmm.predict(obs)
    mm = markovmodel(ghmm.transmat_, ghmm.startprob_)
    return mm.predict([y[-1]], steps)

def hmm_predict_features(ghmm, obs, steps):
    y = ghmm.predict(obs)
    pred = []
    mm = markovmodel(ghmm.transmat_, ghmm.startprob_)
    sts = mm.predict([], steps)
    for s in sts:
        mean = ghmm.means_[y[-1]]
        cov = ghmm.covars_[y[-1],:]
        x = np.random.multivariate_normal(mean,cov,1)
        pred.append(x[0].tolist())
    return pred

# X: sequence of observations
# y: sequence of latent states
def estimate_parameters(X, y):
    mm = markovmodel()
    mm.fit(y)
    data = dict()
    for i in range(len(y)):
        for s, x in zip(y[i], X[i]):
            if data.has_key(s):
                data[s].append(x)
            else:
                data[s] = [x]
    ns = len(data.keys())
    means = np.array([[np.mean(data[s])] for s in range(ns)])
    covars = np.tile(np.identity(1), (ns, 1, 1))
    for s in range(ns):
        covars[s, 0] = np.std(data[s])
    return mm.startprob, mm.transmat, means, covars


# In[32]:


# Task 1: Predict the latent cities of training sequences

# In[33]:

f=open("HW10_Q4_prediction.txt",'w')
startprob, transmat, means, covars = estimate_parameters(X, y)#train
model = hmm.GaussianHMM(5, "full", startprob, transmat) # change 3 to 5
model.means_  = means
model.covars_ = covars
for x in final_x1: #testing
    y = model.predict(x)
    #print [label[s] for s in y]
    j=[label[s] for s in y]
    f.write(json.dumps(j)+'\n')
    
f.close()




   
   
   
   
   
   
   
   
   