import json,datetime,os
#os.mkdir('output-folder')
#MON-DAY-YEAR-HOUR
file_open = open('CrimeReport.txt' , 'r').readlines()

if not os.path.exists('output-folder'):
    os.makedirs('output-folder')

for line in file_open:
	
	tweet = json.loads(line)	

	created_tweet = datetime.datetime.strptime(tweet['created_at'],'%a %b %d %H:%M:%S +0000 %Y')
	
	m = created_tweet.month
	d = created_tweet.day
	y = created_tweet.year
	h = created_tweet.hour
	
	format = "%d-%d-%d-%d.txt"%(m,d,y,h)
	
	convert_string = str(format)
	
	path = 'output-folder/'
	join_file = os.path.join(path, convert_string)
	open(join_file,'a').write(json.dumps(tweet)+"\n")
	
	
	
	
	
	
	
	
	
	
	
	