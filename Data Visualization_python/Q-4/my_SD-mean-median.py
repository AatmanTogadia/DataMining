from pattern.en import sentiment

import math
def mean_median():
    file_open = open('500-tweets.txt' , 'r').readlines()
    s2=[]
    for line in file_open:
    
        s = sentiment(line)	
        s1 = s[0]
        s2.append(s1)
   
    a = sum(s2)

    s2.sort()
    




    print 'Median =',s2[250] # There are 501 values in this list, there for the median will be 250th element.
    print 'Mean = ',a/501
    print 'MIN =',min(s2)

def SD():
    file_open = open('500-tweets.txt' , 'r').readlines()
    s2=[]
    for line in file_open:
    
        s = sentiment(line)	
        s1 = s[0]
        s2.append((s1-0.046)*(s1-0.046))
    b = sum(s2) 
    print 'Standard Deviation  = ',math.sqrt(b/500)
   
    
 
 
def MAD():
    file_open = open('500-tweets.txt' , 'r').readlines()
    s2=[]
    for line in file_open:
    
        s = sentiment(line)	
        s1 = s[0]
        s2.append(abs((s1-0.046)))

    
    print 'MAD =',sum(s2)/501
    print 'MAX = ',max(s2)
    


def main():
    
    MAD()
    mean_median()
    SD()
    pass

if __name__ == '__main__':
    main()
    



