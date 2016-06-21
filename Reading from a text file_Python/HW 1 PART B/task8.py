import json,datetime

file_open = open('CrimeReport.txt' , 'r').readlines()

tweets=[]

for line in file_open:
		
	tweet = json.loads(line)	
	tweets.append(tweet)
	
#created_tweet = datetime.datetime.strptime(tweet['created_at'],'%a %b %d %H:%M:%S +0000 %Y')

sorted_tweet = sorted(tweets,key= lambda item: datetime.datetime.strptime(item['created_at'],'%a %b %d %H:%M:%S +0000 %Y'))

#sorted_tweet = sorted(tweets,key= lambda item: created_tweet)


f = open('output.txt','w')

for tweet in sorted_tweet[-10:]:
	f.write(json.dumps(tweet) + '\n')
	#print tweet['created_at']
f.close()


print sorted_tweet[-10:]




















