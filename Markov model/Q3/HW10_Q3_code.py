
import json

import numpy as np
import types


# In[23]:

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
        self.transmat = self.transmat *                         np.transpose(np.outer(np.ones([ns,1]), 1./d))

    def predict(self, obs, steps):
        pred = []
        n = len(obs)
        if len(obs) > 0:
            s = obs[-1]
        else:
            s = np.argmax(np.random.multinomial(1, 
                            self.startprob.tolist(), size = 1))
        for i in range(steps):
            s1 = np.random.multinomial(1, self.transmat[s,:].tolist(), 
                                       size = 1)
            pred.append(np.argmax(s1))
            s = np.argmax(s1)
        return pred




label = {0: "New York City", 1: "Boston", 2: "Washington D.C.",3:"Seattle",4:"Philapedia"}

tweets=[]
y=[]
final_y = []
for line in open('HW10_Q3_training.txt').readlines():
    tweets.append(json.loads(line))
    #
    #print line
for items in tweets:
    #print items
    y = []
    for i in items:
        if i=="New York City":
            y.append(0)
        elif i=="Boston":
            y.append(1)
        elif i=="Washington D.C.":
            y.append(2)
        elif i=="Seattle":
            y.append(3)
        elif i=="Philapedia":
            y.append(4)
    #print y
    final_y.append(y)
                    
#print len(final_y)                    
tweets1=[]
y1=[]
final_y1 = []


count=0
for line in open('HW10_Q3_testing.txt').readlines():
    tweets1.append(json.loads(line))
    #
    #print line
for items in tweets1:
    
         
    #print items
    y1 = []
    for i in items:
        
        if i=="New York City":
            y1.append(0)
        elif i=="Boston":
            y1.append(1)
        elif i=="Washington D.C.":
            y1.append(2)
        elif i=="Seattle":
            y1.append(3)
        elif i=="Philapedia":
            y1.append(4)
    #print y
       
    final_y1.append(y1)
    
    
                  
mm = markovmodel()
mm.fit(final_y)


f=open("HW10_Q3_predictions.txt",'w')


final=[]
for i in final_y1:
    pred = mm.predict(i, 5)
    #final=[label[s] for s in pred]
    
    f.write(json.dumps([label[s] for s in pred])+'\n')
    
f.close() 
    #print [label[s] for s in pred]
     
 

                    
                    
                    
                    
             
            
            
        
    
