import numpy as np
import numpy.random
import matplotlib.pyplot as plt
import  seaborn as sns
import pandas 



import csv

data = pandas.read_csv('servo.data', sep=',', header=None)
sns.heatmap(data.corr(),square= True)
plt.show()

#servo.data has 3 attrbutes with numerical values; pgain,vgain and class.