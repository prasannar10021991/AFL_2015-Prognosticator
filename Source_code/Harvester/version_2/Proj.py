from TwitterSearch import *
import couchdb
import json
import time
from pyexpat import features

     
    
try:
    featurelist = ["afl","afl2015","afl15","australian football league","australianfootballleague","collingwoodvsstkilda","magpiessuck","saintssuck","magpiesvssaints","piesvssaints","MCG","Collingwood Football Club","collingwoodfc","stkildafc","collingwoodfootballclub","The Magpies","themagpies","the pies","thepies","St Kilda Football Club","stkildafootballclub","The Saints","thesaints","gocollingwood","gomagpies","gopies","magpiesftw","piesftw","gpsaints","saintsftw","stkildaftw","Nick Riewoldt","Jesse White","Dane Swan","Scott Pendlebury","Shane Savage","Steele Sidebottom","Jack Steven","piesrule","magpiesrule","saintsrule"]
    features = []
    #must = ["carlton football club","theblues","richmond football club","thetigers","carlton","richmond","gocarlton","gorichmond","thebluesftw","thetigersftw","carltonftw","richmondftw"]
    couch = couchdb.Server()
    couch = couchdb.Server('http://127.0.0.1:5984/')
    db = couch['twittersearch']
    
    def combos(S,n):
        if (n <= 0): return
        for s in S:
            if len(s) <= n: yield s
            yield "#"+s
            
    for x in combos(featurelist,100): 
        features.append(x)   
    
    
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.set_keywords(features) # let's define all words we would like to have a look for
    tso.set_language('en') # we want to see German tweets only
    tso.set_include_entities(True) # and don't give us all those entity information
    # it's about time to create a TwitterSearch object with our secret tokens
    ts = TwitterSearch(
        consumer_key = '7Kk3B38wZNGVKVbOKCLXs2u8J',
        consumer_secret = 'gLPsOF1UnZ9tsYoR7Zpmn05WPFIn6FKydvyfnrpdPqI7BKKZyJ',
        access_token = '129674370-Z6Fhod4lrbpy3d8qGOSWhQT4jlcBCqD41UTrTmrN',
        access_token_secret = '1BdAJuffVxhS93yFup8oq9zc9umxSt2Ii4NAYxsk0WB4p'
    )
    #params = urllib3.urlencode(dict(q='obama', rpp=10, geocode='37.781157,-122.398720,1mi'))
    #u = urllib.urlopen('http://search.twitter.com/search.json?' + params)
    #j = json.load(u)
    #pprint.pprint(j)
    # this is where the fun actually starts :)
    for tweet in ts.search_tweets_iterable(tso):
        try:
            
            tweet_data = json.loads(tweet)
            text = tweet_data['text']
            #text = tweet.encode('ascii', 'ignore').decode('ascii')
            screen_name = tweet_data['user']['screen_name']
            date = tweet_data['created_at']
            tweet_id = tweet_data['id']
            user_id = tweet_data['user']['id']
            geo = tweet_data['geo']
            coordinates = tweet_data['coordinates']
            user_location = tweet_data['user']['location']
            place_tweet = tweet_data['place']
            user_description = tweet_data['user']['description']
            location_data = str(geo)+","+str(coordinates)+","+str(place_tweet)
                    
            doc = {"tweet_id":tweet_id,"user_id":user_id,"screen_name":screen_name,"date":date,"tweet_text":tweet,"geo":geo,"coordinates":coordinates,"user_location":user_location,"user_description":user_description}
            db.save(doc)
                    
            tweetData = open('AFLtweetsDBSearchResults.csv','a')
            tweet_details = str(tweet_id)+"::"+"@"+screen_name+"::"+date+":::"+tweet
            print tweet_details
            tweetData.write(tweet_details)
            tweetData.write('\n')
            tweetData.close()
                
                                        
            
                    
            
        
        except BaseException, e :
            print 'failed onData,',str(e)
            time.sleep(2)
                


    

except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)
    



           

            
