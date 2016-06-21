#!/usr/bin/python

#
# Example boxplot code
#

from pylab import *
import csv
# fake up some data

spread= rand(50) * 100
center = ones(25) * 50
flier_high = rand(10) * 100 + 100
flier_low = rand(10) * -100

data =concatenate((spread, center, flier_high, flier_low), 0)

reader = csv.reader(open('new book.csv'), delimiter=",")
data=[]
for row in reader:
     #print row[0].replace(",","")
     print row[0]
     data.append(row[0])
     '''if(row[0].replace(",","").isdigit()):
          data.append(float(row[0].replace(",",""))/100-100)'''

data.sort()

data = map(float, data)
print data
# change whisker length
figure()
boxplot(data,0,'rs',0,0.75)
#boxplot(data,1,'rs',0,0.00009)

show()
