# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 21:53:56 2016

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
import nltk
from nltk.corpus import stopwords
import pickle



english_stopwords = ["a", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along", "already", "also","although","always","am","among", "amongst", "amoungst", "amount",  "an", "and", "another", "any","anyhow","anyone","anything","anyway", "anywhere", "are", "around", "as",  "at", "back","be","became", "because","become","becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides", "between", "beyond", "bill", "both", "bottom","but", "by", "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven","else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own","part", "per", "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thickv", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the"]

spanish_stopwords = set(stopwords.words("spanish")) #creating a list of spanish stop-words

all_stopwords=[]
all_stopwords.append(english_stopwords)
all_stopwords.append(spanish_stopwords) #both spanish and eglish stop-words combined.



tweets_nega = []
for line in open('train_nega_tweets.txt').readlines():
    
    tweet=json.loads(line)
    
    temp=tweet['text']
    
    items=[0,temp]
    tweets_nega.append(items)
  

  
# Extract the vocabulary of keywords
vocab = dict()
for label,text in tweets_nega:
    for term in text.split():
        term = term.lower()
        if len(term) > 2 and term not in all_stopwords:
            if vocab.has_key(term):
                vocab[term] = vocab[term] + 1
            else:
                vocab[term] = 1



# Remove terms whose frequencies are less than a threshold (e.g., 20)
vocab = {term: freq for term, freq in vocab.items() if freq > 20}
# Generate an id (starting from 0) for each term in vocab
vocab = {term: idx for idx, (term, freq) in enumerate(vocab.items())}

# Generate X and y
print vocab
X = []
y = []
for class_label, tweet_text in tweets_nega:
    x = [0] * len(vocab)
    terms = [term1 for term1 in tweet_text.split() if len(term1) > 2]
    for term in terms:
        if vocab.has_key(term):
            x[vocab[term]] += 1
    y.append(class_label)
    X.append(x)



tweets_posi = []
for line in open('train_posi_tweets.txt').readlines():
    tweet=json.loads(line)
    
    lala=tweet['text']
    items=[1,lala]
    tweets_posi.append(items)




  
for class_label, tweet_text in tweets_posi:
    x = [0] * len(vocab)
    terms = [term2 for term2 in tweet_text.split() if len(term2) > 2]
    for term in terms:
        if vocab.has_key(term):
            x[vocab[term]] += 1
    y.append(class_label)
    X.append(x)
    

# 10 folder cross validation to estimate the best w and b
svc = svm.SVC(kernel='linear')
Cs = range(1,5)
clf = GridSearchCV(estimator=svc, param_grid=dict(C=Cs), cv = 10)



clf = LogisticRegression()
clf.fit(X, y)


print clf.predict(X)



# predict the class labels of new tweets
#print clf.predict(X)
tweets_test = []
for line in open('test_tweets.txt').readlines():
    tweet=json.loads(line)
    
    lala=tweet['text']
    #items=[lala]
    tweets_test.append(lala)
    
#print tweets
    
# Generate X for testing tweets
X=[]
for tweet_text in tweets_test:
    x = [0] * len(vocab)
    terms = [term3 for term3 in tweet_text.split() if len(term3) > 2]
    for term in terms:
        if vocab.has_key(term):
            x[vocab[term]] += 1
    X.append(x)
    
    
#print X    
    

   
y = clf.predict(X)


tweets1=[]
for line in open('test_tweets.txt').readlines():
    tweet=json.loads(line)
    
    e_id=tweet['embersId']
    text=tweet['text']
    items=[e_id,text]
    tweets1.append(items)
   

f1 = open('trained_LR_classifier.pkl', 'w')

f1.write(pickle.dumps(clf))

f1.close()

pred=dict()
t='true'
f='false'

f2=open('predictions.txt','w')


for idx, [tweet_id, tweet_text] in enumerate(tweets1):
    if y[idx]==1:
        pred.update({tweet_id:t})
    else:
        pred.update({tweet_id:f})
        
        

f2.write(json.dumps(pred))

f2.close()
 


print '\r\nAmong the total {1} tweets, {0} tweets are predicted as positive.'.format(sum(y), len(y))