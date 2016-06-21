# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 21:05:50 2016

@author: Aatman
"""

import pandas
import matplotlib.pyplot as plt
from pandas.tools.plotting import parallel_coordinates


data = pandas.read_csv('servo.data', sep=',', header=None, names=['A', 'B', 'C', 'D', 'E'])

#print data
data = data.drop('A', 1)
data = data.drop('B',1)

print data

parallel_coordinates(data, 'E')
plt.show()
