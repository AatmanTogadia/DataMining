from pattern.en import sentiment
from pattern.en import positive
import json

file_open = open('crime.txt' , 'r').readlines()

for line in file_open:
		
	tweet = json.loads(line)	
	
	t = tweet['text']
	s = sentiment(t)
	
	
	#print s[0]	
	
	if positive(t,0.1) == True:
		open('positive-sentiment-tweets.txt','a').write(json.dumps(tweet)+"\n")
	else:
		open('nagative-sentiment-tweets.txt','a').write(json.dumps(tweet)+"\n")
	
	