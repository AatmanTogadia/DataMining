# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 18:37:23 2016

@author: Aatman
"""

import numpy as np
import numpy.random
import matplotlib.pyplot as plt

import csv

pgain = []
vgain = []
reader = csv.reader(open('servo.csv'))
for row in reader:
    
    pgain.append(row[2])
    vgain.append(row[3])
       

    
#print vgain.sort()


vgain.sort()
vgain = map(int, vgain)

pgain.sort()
pgain = map(int , pgain)

heatmap, xedges, yedges = np.histogram2d(vgain, pgain, bins=5)
extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]

plt.clf()
plt.imshow(heatmap, extent=extent)
plt.show()


#Density map of pgain and vgain values






