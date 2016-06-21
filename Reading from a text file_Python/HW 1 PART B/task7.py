import json

file_open = open('CrimeReport.txt' , 'r').readlines()


for line in file_open:
		
	tweet = json.loads(line)	
	
	print tweet['id']
	

