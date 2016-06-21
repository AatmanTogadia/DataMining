# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 23:18:22 2016

@author: Aatman
"""

import json
import Orange
stopwords = ["a","citrus","pip","ready","care","frozen","other","whole","bottled","tropical","specialty ","processed","salty","canned","artif.","shopping","domestic","brown","pickled","condensed","root","white","chewing","sparkling","(appetizer)","misc.","baking","frankfurter", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along", "already", "also","although","always","am","among", "amongst", "amoungst", "amount",  "an", "and", "another", "any","anyhow","anyone","anything","anyway", "anywhere", "are", "around", "as",  "at", "back","be","became", "because","become","becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides", "between", "beyond", "bill", "both", "bottom","but", "by", "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven","else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own","part", "per", "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thickv", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the"]


#dataset of a grocery store where each line is of a single user describing what items he/she purchased on a single transaction.
#I had to insert few stopwords like : ready,frozen,bottled,tropical etc ,because some items were inputed as "ready meal","tropical fruits" etc.


tweets = []
for line in open('user_items_id.txt').readlines():
    tweets.append(json.loads(line))

# creating vocabulary of frequent items
freq_items = dict()
for user_id, user_id2, text in tweets:
    for term in text.split():
        term = term.lower()
        if len(term) > 2 and term not in stopwords:
            if freq_items.has_key(term):
                freq_items[term] = freq_items[term] + 1
            else:
                freq_items[term] = 1

# Remove terms whose frequencies are less than a threshold (e.g., 5)
freq_items = {term: freq for term, freq in freq_items.items() if freq > 5}
# Generate an id (starting from 0) for each term in vocab
freq_items = {term: idx for idx, (term, freq) in enumerate(freq_items.items())}



print freq_items


# creating raw data using vocab of most frequent items.

#for the raw data, we will only consider a user's items which is in the most frequent dictionary.

my_data = []


for line in open('user_trans.txt').readlines():
    user_item = ""
    for word in line.split():
        if word in freq_items:
            if user_item == "":
                user_item += word
            else:
                user_item += ", "
                user_item += word
    my_data.append(user_item)    
    
    
    
    
#print raw_data    

f = open('data.basket', 'w')
for item in my_data:
    f.write(item + '\n')
f.close()

# Load data from the text file: data.basket
data = Orange.data.Table("data.basket")


# Identify association rules with supports at least 0.02
rules = Orange.associate.AssociationRulesSparseInducer(data, support = 0.06)


# print out rules
print "%4s %4s  %s" % ("Supp", "Conf", "Rule")
for r in rules[:]:
    print "%4.1f %4.1f  %s" % (r.support, r.confidence, r)


rule = rules[0]


            
for idx, d in enumerate(data):
    print '\nUser {0}: {1}'.format(idx, my_data[idx])
    for r in rules:
        if r.applies_left(d) and not r.applies_right(d):
            print "%4.1f %4.1f  %s" % (r.support, r.confidence, r)







