from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import tweepy
import time
import json
import couchdb
from pyexpat import features


ckey = '7Kk3B38wZNGVKVbOKCLXs2u8J'
csecret = 'gLPsOF1UnZ9tsYoR7Zpmn05WPFIn6FKydvyfnrpdPqI7BKKZyJ'
atoken = '129674370-Z6Fhod4lrbpy3d8qGOSWhQT4jlcBCqD41UTrTmrN'
asecret = '1BdAJuffVxhS93yFup8oq9zc9umxSt2Ii4NAYxsk0WB4p'
#query = ["afl","afl challenge","australian football league","kangas","carlscum","carltank","blue baggers","mayblooms","hula hoops","carlton blues","hawthorn hawks","Adelaide Crows","The crows","Tex Walker","Eddie betts","podsiadly","josh jenkins", "van berlo", "Patrick Dangerfield", "Rory Sloane", "tom lynch", "kerridge",  "David Mackay", "Mackay","Brodie martin","elis yolmen","Thommo","Taylor walker","afl2015","victoriabitter","afl aussie","afl vic","footyseason","aflmelbourne","afl360","thetigers","thedemons","sydneyswans","thesuns","thebombers","thedons","essendonfootballclub","brisbanelions","collingwoodfootballclub","magpies","westernbulldogs","westcoasteagles","stkildafootballclub","thesaints","greaterwesternsydneygiants","gwsgiants","adelaidefootballclub","northmelbournefootballclub","thekangaroos","fremantlefootballclub","thedockers","portadelaidefootballclub","aflpower","hawthornfootballclub","geelongfootballclub","thecats"] 
featurelist = ["afl","afl2015","afl15","australian football league","australianfootballleague","MCG","Collingwood Football Club","collingwoodfc","collingwood_fc","stkildafc","stkilda_fc","collingwoodfootballclub","carlton blues","carltonfc","carlton_fc","hawthorn hawks","hawthornfc","hawthorn_fc","Adelaide Crows","adelaidefc","adelaide_fc","The crows","The Magpies","themagpies","the pies","thepies","St Kilda Football Club","stkildafootballclub","The Saints","thesaints","gocollingwood","gomagpies","gopies","magpiesftw","piesftw","gpsaints","saintsftw","stkildaftw","footyseason","aflmelbourne","afl360","thetigers","thedemons","sydneyswans","sydneyfc","thesuns","thebombers","thedons","essendonfootballclub","essendonfc","essendon_fc","brisbanelions","brisbanefc","brisbane_fc","Nick Riewoldt","Jesse White","westernbulldogs","westcoasteagles","Dane Swan","Scott Pendlebury","Shane Savage","Steele Sidebottom","Jack Steven","piesrule","magpiesrule","saintsrule","greaterwesternsydneygiants","greaterwesternsydneyfc","greaterwesternsydney_fc","gwsgiants","adelaidefootballclub","northmelbournefootballclub","northmelbournefc","northmelbourne_fc","thekangaroos","fremantlefootballclub","fremantlefc","fremantle_fc","thedockers","portadelaidefootballclub","portadelaidefc","portadelaide_fc","aflpower","hawthornfootballclub","geelongfootballclub","geelongfc","geelong_fc","thecats"]

couch = couchdb.Server()
couch = couchdb.Server('http://127.0.0.1:5984/')
db = couch['twittersearch']

auth = OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)
api = tweepy.API(auth,wait_on_rate_limit=True)
features = []
#must = ["afl","afl2015","North Melbourne Football Club","The Kangaroos","thekangaroos","Brisbane Lions","the lions","thelions","gobrisbane","gokangaroos","kangaroosftw","lionsftw","brisbaneftw","northmelbourneftw"]
sinceid = 0
def combos(S,n):
    if (n <= 0): return
    for s in S:
        if len(s) <= n: yield s
        yield "#"+s

def set_default(obj):
    if isinstance(obj, set):
        return list(obj)
    raise TypeError
            
for x in combos(featurelist,1000000): 
    features.append(x)
print features
    
for i in range(0,100):
    print ("ROUND"+str(i))
    for word in features:
        results =  tweepy.Cursor(api.search,q=word,rpp=100,result_type="mixed",since_id=sinceid,include_entities=True,lang="en",geocode = "-37.814251,144.963165,30000mi").items()
        while True:
            try:
                tweet = results.next()
                for tweets in results:
                    try:
                        json_tweet = json.dumps(tweets._json)
                        json_val = json.loads(json_tweet)
                        text = json_val["text"]
                        #print type(json_val)
                        screen_name = (json_val["user"]["screen_name"]).encode('utf-8').strip()
                        #print screen_name
                        date = str(json_val["created_at"])
                        _id = str(json_val["id"]).encode('utf-8').strip()
                        tweetid = json_val["id"]
                        #print(type(tweetid))
                        #if (tweetid > sinceid):
                        #   print type(tweetid)
                        #  print ("NEW SINCE ID:"+ str(tweetid))
                        #sinceid = json_val["id"]
                        user_id = str(json_val["user"]["id"]).encode('utf-8').strip()
                        geo = str(json_val["geo"]).encode('utf-8').strip()
                        coordinates = str(json_val["coordinates"]).encode('utf-8').strip()
                        user_location = (json_val["user"]["location"]).encode('utf-8').strip()
                        place_tweet = str(json_val["place"]).encode('utf-8').strip()
                        user_description = (json_val["user"]["description"]).encode('utf-8').strip()
                        
                        #location_data = str(geo)+","+str(coordinates)+","+str(place_tweet)
                        doc = {"_id":_id,"date":date,"user_id":user_id,"screen_name":screen_name,"tweet_text":text,"geo":geo,"coordinates":coordinates,"tweet_location":place_tweet,"user_location":user_location,"user_description":user_description}
                        #print doc
                        db.save(doc)
                        tweetData = open('AFLtweetsDBSearchResults.csv','a')
                        #tweet_details = tweet_id+"::"+"@"+screen_name+"::"+((date).encode('utf-8').strip())+":::"+str(text)
                        tweet_details = str(_id)+":::"+((text).encode('utf-8').strip())
                        print tweet_details
                        tweetData.write(tweet_details)
                        tweetData.write('\n')
                        tweetData.close()
                        
                    except tweepy.TweepError:
                        time.sleep(60*15)
                    except couchdb.http.ResourceConflict:
                        print"SKIPPING DUPLICATE"    
                continue
            except StopIteration:
                break   
        
