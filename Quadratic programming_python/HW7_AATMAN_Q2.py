# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 15:08:28 2016

@author: Aatman
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 23:18:49 2016

@author: Aatman
"""

from cvxopt import matrix, solvers, spmatrix
import numpy as np
import matplotlib.pyplot as plt
from math import *


def main():
    global position,position1
    position=3
    
    
    data = [[3,5,1], [5,3,1], [6,6,1], [5,6,-1],[6,5,-1]]
    Q = spmatrix(2.0, range(8), range(8))
    Q[2,2] = 0
    Q[3,3] = 0
    Q[4,4] = 0
    Q[5,5] = 0
    Q[6,6] = 0
    Q[7,7] = 0
   # print Q
    p = matrix([0.0, 0.0, 0.0,1,1,1,1,1], (8,1))
   # print p
    G = []
    h = []
    for items in data:
        row = []
        if items[2] == 1:
            row.extend([-1 * item for item in items[:2]])
            row.append(-1)
            for j in range(0,5):
                row.append(0)
            row[position] = -1
            position+=1
            G.append(row)
            h.append(-1.0)
        else:
            row.extend(items[:2])
            row.append(1)
            for j in range(0,5):
                row.append(0)
            row[position] = -1
            position+=1
            G.append(row)
            h.append(-1.0)
    position1 = 2
    for i in range(0,5):
        row[position1] = -1
        row =[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]        
        position1+=1
        G.append(row) 
        
     
   
    
    G = matrix(G).trans()
    G[4,2]=1
    
   # print G
    h.append(0)
    h.append(0)
    h.append(0)
    h.append(0)
    h.append(0)
    
    h = matrix(h)
  
    #print h
    A = None
    b = None
    sol=solvers.qp(Q, p, G, h)
    w1 = sol['x'][0]
    w2 = sol['x'][1]
    b  = sol['x'][2] 
    print 'Q is\n',Q
    print 'p is\n',p
    print 'G is\n',G
    print 'h is\n',h
    print 'w1= {0}; w2={1}; b={2}'.format(w1, w2, b)
    
    
    

    ### suppose you have obtained sol['x'] from CVXOPT QP minimization

    x = [item[0] for item in data if item[2] == 1]
    y = [item[1] for item in data if item[2] == 1]
    plt.scatter(x, y, s=80, facecolors='none', edgecolors='r')
    x = [item[0] for item in data if item[2] == -1]
    y = [item[1] for item in data if item[2] == -1]
    plt.scatter(x, y, s=80, facecolors='none', edgecolors='b')
    x = [item[0] for item in data]
    y = [item[1] for item in data]
    plt.scatter(x, y, s=40, facecolors='none', edgecolors='k')
    w1 = sol['x'][0]
    w2 = sol['x'][1]
    b = sol['x'][2]

    print 'Answer to question a:'
    print 'w: {0}; b: {1} \n'.format([w1,w2], b)
    print 'Answer to question b:'
    for point in data:
        print '{0}: {1}'.format(point, abs(w1 * point[0] + w2 * point[1] + b)/sqrt(w1 * w1 + w2 * w2))

    print '\nAnswer to question c: '
    print 2/sqrt(w1 * w1 + w2 * w2)

    print '\nAnswer to question d:'
    print 'w.x + b > 0 for positive class'
    print 'w.x + b < 0 for negative class'

    new_points = [[5, 3], [3, 1], [4, 3], [4, 4], [5, 4]]

    print '\nAnswer to question c:'
    for point in new_points:
        if w1 * point[0] + w2 * point[1] + b < 0:
            print '{0}: {1}'.format(point, 'FALSE')
        else:
            print '{0}: {1}'.format(point, 'TRUE')

    x = [min([item[0] for item in data]), max([item[0] for item in data])]

    y = [(w1 * x[i] + b)/(-1 * w2) for i in range(2)]

    plt.plot(x, y, color='red')

    y = [(w1 * x[i] + b - 1)/(-1 * w2) for i in range(2)]

    plt.plot(x, y, color='black')

    y = [(w1 * x[i] + b + 1)/(-1 * w2) for i in range(2)]

    plt.plot(x, y, color='black')

    plt.gca().set_aspect('equal', adjustable='box')

    plt.grid()

    plt.show()


if __name__ == '__main__':
    main()