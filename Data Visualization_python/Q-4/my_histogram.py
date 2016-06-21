# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 15:05:33 2016

@author: Aatman
"""
# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pylab as plt
import csv

vgain = []
reader = csv.reader(open('servo.csv'))
for row in reader:
    
    vgain.append(row[3])
       

    
#print vgain.sort()

vgain.sort()
vgain = map(int, vgain)
print vgain
bins = [0,1,2,3,4,5,6]
plt.hist(vgain, bins)
plt.title("vgain value count")
plt.ylabel("Count")
plt.xlabel("vgain") 
plt.show()
#Histogram shows number of counts of a 'vgain' value.



                  