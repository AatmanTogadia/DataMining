import twitter, sys, json
#from pattern.en import positive
reload(sys)
sys.setdefaultencoding("utf-8")

myApi=twitter.Api(consumer_key='9DAqF8iHJbOr0d0ouPnBzTlFi', \
                  consumer_secret='DcwdIbZ6VinH3fJiT8IaCFM7jxWU8dCsDiBaNxU46dXI9boc25', \
                  access_token_key='697830429748023296-VXBfZL5P4iNJGu6RaEtiT9SnjHkKebn', \
                  access_token_secret='suLwIIjJheal1RmDDJRhOZkOuXu7rdMMDYkChzYN10pgq')

def print_info(tweet):
    print '***************************'
    print 'Tweet ID: ', tweet['id']
    print 'Post Time: ', tweet['created_at']
    print 'User Name: ', tweet['user']['screen_name']
    try:
	    print 'Tweet Text: ', tweet['text']
    except:
		pass

def rest_query_ex1():
    geo = ('42.6525', '-73.7572', '90mi')
    raw_tweets = myApi.GetSearch(None, geo, count = 100)
    
    for raw_tweet in raw_tweets:
        tweet = json.loads(str(raw_tweet))
#        print_info(tweet)
    print len(raw_tweets)

def rest_query_ex2():
    query = 'VIOLENCE OR CRIME'
    geo = ('40.7305991', '-73.9865811', '450mi') # City of New York
    f = open('Random-OTHER-100-tweets.txt','w')    
    MAX_ID = None
    print 'aa'
    
    for it in range(1):
        raw_tweets = myApi.GetSearch(query, geo, count=200, max_id = MAX_ID)
        tweets = [json.loads(str(raw_tweet)) for raw_tweet \
                  in raw_tweets]
        MAX_ID = tweets[-1]['id']
        
        for raw_tweet in raw_tweets:
            tweet = json.loads(str(raw_tweet))
            f.write(tweet['text']+'\n')
            
       

def rest_query_ex3(): 
    query = 'VIOLENCE OR CRIME'
    #f = open('output.txt','w')
    geo = ('40.7305991', '-73.9865811', '450mi') # City of New York
    MAX_ID = None 
    for it in range(1): # Retrieve up to 200 tweets
        tweets = [json.loads(str(raw_tweet)) for raw_tweet \
                  in myApi.GetSearch(query, geo, count = 100, max_id = MAX_ID, result_type='recent')]
        #f.write(str(tweets)+'\n')
        if tweets:
            MAX_ID = tweets[-1]['id']
            print MAX_ID, len(tweets)

def main():
    #for i in range(10):
    #rest_query_ex1()
    rest_query_ex2()
    rest_query_ex3()
    
    pass

if __name__ == '__main__':
    main()
    

                                     


