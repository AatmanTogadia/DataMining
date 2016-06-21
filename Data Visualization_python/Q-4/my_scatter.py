# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 14:51:47 2016

@author: Aatman
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 14:36:27 2016

@author: Aatman
"""

import numpy as np
import matplotlib.pyplot as plt
import csv
vgain=[]
servo_class=[]

area=[]
colors=[]
'''1. motor: A,B,C,D,E
   2. screw: A,B,C,D,E
   3. pgain: 3,4,5,6
   4. vgain: 1,2,3,4,5
   5. class: 0.13 to 7.10'''
reader = csv.reader(open('servo.csv'), delimiter=",")
for row in reader:
    
   
    vgain.append(row[3])
    servo_class.append(row[4])
    area.append(int(row[2])*50+50)
    if row[3]=="1":
          colors.append(1)
    elif row[3]=="2":
          colors.append(2)
    elif row[3]=="3":
           colors.append(3)
    elif  row[3]=="4":
          colors.append(4)
    elif  row[3]=="5":
          colors.append(5)
    
          #colors.append(12)
   
#scatter plot of class and pgain          
         
vgain.sort()
vgain = map(int, vgain)
print vgain  

print servo_class

plt.scatter(vgain, servo_class, s=area, c=colors, alpha=0.5)
plt.show()