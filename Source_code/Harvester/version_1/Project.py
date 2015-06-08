from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import tweepy
import time
import json
import couchdb


ckey = '7Kk3B38wZNGVKVbOKCLXs2u8J'
csecret = 'gLPsOF1UnZ9tsYoR7Zpmn05WPFIn6FKydvyfnrpdPqI7BKKZyJ'
atoken = '129674370-Z6Fhod4lrbpy3d8qGOSWhQT4jlcBCqD41UTrTmrN'
asecret = '1BdAJuffVxhS93yFup8oq9zc9umxSt2Ii4NAYxsk0WB4p'
featurelist = ["afl","afl2015","afl15","australian football league","australianfootballleague","MCG","Collingwood Football","collingwoodfc","collingwood_fc","stkildafc","stkilda_fc","collingwoodfootballclub","carlton blues","carltonfc","carlton_fc","hawthorn hawks","hawthornfc","hawthorn_fc","Adelaide Crows","adelaidefc","adelaide_fc","crows","Magpies","themagpies","pies","thepies","Kilda Football","stkildafootballclub","Saints","thesaints","gocollingwood","gomagpies","gopies","magpiesftw","piesftw","gpsaints","saintsftw","stkildaftw","footyseason","aflmelbourne","afl360","thetigers","thedemons","sydneyswans","sydneyfc","thesuns","thebombers","thedons","essendonfootballclub","essendonfc","essendon_fc","brisbanelions","brisbanefc","brisbane_fc","Nick Riewoldt","Jesse White","westernbulldogs","westcoasteagles","Dane Swan","Scott Pendlebury","Shane Savage","Steele Sidebottom","Jack Steven","piesrule","magpiesrule","saintsrule","greaterwesternsydneygiants","greaterwesternsydneyfc","greaterwesternsydney_fc","gwsgiants","adelaidefootballclub","northmelbournefootballclub","northmelbournefc","northmelbourne_fc","thekangaroos","fremantlefootballclub","fremantlefc","fremantle_fc","thedockers","portadelaidefootballclub","portadelaidefc","portadelaide_fc","aflpower","hawthornfootballclub","geelongfootballclub","geelongfc","geelong_fc","thecats"]
other = ["#aflbluestigers","#afldeessuns","#aflswansdons","#afllionspies","#afldogseagles","#aflsaintsgiants","#aflcrowsnorth","#aflfreopower","#aflhawkscats","#afleaglesblues","#afltigersdogs","#aflgiantsdees","#aflpiescrows","#aflpowerswans","#aflsunssaints","#aflcatsfreo","#aflbombershawks","#aflnorthlions","#aflpiessaints","#aflbluesdons","#aflcrowsdees","#aflswansgiants","#aflnorthpower","#afllionstigers","#aflhawksdogs","#aflcatssuns","#afleaglesfreo","#afltigersdees","#aflsaintsblues","#afldonspies","#aflgiantssuns","#aflpowerhawks","#aflfreoswans","#afllionseagles","#aflcatsnorth","#afldogscrows","#aflbluespies","#afltigerscats","#aflswansdogs","#aflsunslions","#aflnorthhawks","#afleaglesgiants","#afldeesfreo","#aflsaintsdons","#aflcrowspower","#aflpiescats","#aflnorthtigers","#afldogssaints","#aflgiantshawks","#aflsunscrows","#afldeesswans","#aflfreodons","#aflblueslions","#aflpowereagles","#afldonsnorth","#aflcrowssaints","#aflhawksdees","#aflbluesgiants","#aflswanscats","#afleaglessuns","#afldogsfreo","#afltigerspies","#afllionspower","#aflcatsblues","#aflsaintseagles","#aflgiantscrows","#aflsunspies","#aflhawksswans","#aflfreonorth","#afldonslions","#afldeesdogs","#aflpowertigers","#aflswansblues","#aflhawkssuns","#afldeespower","#afldogsgiants","#afltigersdons","#aflcrowsfreo","#afllionssaints","#aflpiesnorth","#afleaglescats","#aflfreotigers","#aflbluescrows","#aflsunsswans","#afldonscats","#aflpowerdogs","#aflgiantslions","#aflnortheagles","#aflsaintshawks","#afldeespies","#aflpowercats","#aflsunsfreo","#afleaglesdons","#aflnorthswans","#aflpiesgiants","#aflsaintsdees","#aflcrowshawks","#afltigerseagles","#aflbluespower","#aflgiantsnorth","#afldogslions","#aflcatsdees","#aflfreopies","#aflswanstigers","#aflhawksdons","#afllionscrows","#aflsaintsdogs","#aflbluessuns","#aflswanspower","#aflpieshawks","#afltigersgiants","#aflsunsnorth""#afldogsblues","#afldeeseagles","#afldonssaints","#aflcrowscats","#aflfreolions","#aflpowerpies","#afltigersblues","#afldonsdees","#afldogssuns","#aflnorthcats","#afleaglescrows","#aflgiantssaints","#aflhawksfreo","#afllionsswans","#aflnorthdons","#aflcatsdogs","#aflsunsgiants","#aflpieseagles","#aflswanshawks","#aflfreoblues","#afldeeslions","#aflpowercrows","#aflsaintstigers","#aflblueshawks","#aflgiantscats","#aflcrowssuns","#afltigersfreo","#afldonspower","#afllionsnorth","#afldogspies","#afldeessaints","#afleaglesswans","#aflhawkstigers","#aflcatslions","#aflpiesdees","#aflswanscrows","#aflbluesnorth","#aflsunseagles","#aflpowersaints","#afldonsdogs","#aflfreogiants","#aflcrowstigers","#aflpiesblues","#afldogspower","#afllionssuns","#afleagleshawks","#aflcatsswans","#afldeesnorth","#aflgiantsdons","#aflsaintsfreo","#aflswanspies","#afldonscrows","#aflnorthsaints","#aflpowergiants","#aflcatshawks","#afllionsblues","#afltigerssuns","#afldogsdees","#aflfreoeagles","#aflhawkspower","#aflpiestigers","#aflgiantsswans","#aflsunsdons","#aflsaintscats","#aflcrowslions","#aflnorthfreo","#aflbluesdees","#afleaglesdogs","#aflcatspies","#aflgiantsblues","#aflhawkslions","#aflnorthdogs","#afldonstigers","#aflsunspower","#aflcrowseagles","#aflsaintsswans","#aflfreodees","#aflhawksblues","#aflcatscrows","#afltigersnorth","#aflpowerfreo","#aflpiesdons","#aflswanssuns","#afldeesgiants","#afleaglessaints","#afllionsdogs"]
couch = couchdb.Server()
couch = couchdb.Server('http://127.0.0.1:5984/')
db = couch['twitterstream']

features = []
#must = ["afl","afl2015","North Melbourne Football Club","The Kangaroos","thekangaroos","Brisbane Lions","the lions","thelions","gobrisbane","gokangaroos","kangaroosftw","lionsftw","brisbaneftw","northmelbourneftw"]

def combos(S,n):
    if (n <= 0): return
    for s in S:
        if len(s) <= n: yield s
        yield "#"+s

            
           

            
class Customlistener(tweepy.StreamListener):

    def on_data(self,data):
        try:
            
            json_val = json.loads(data)
            text = json_val["text"]
            #print type(json_val)
            geo = str(json_val["geo"])
            if(geo=="None"):
                screen_name = (json_val["user"]["screen_name"]).encode('utf-8').strip()
                #print screen_name
                date = str(json_val["created_at"])
                _id = str(json_val["id"]).encode('utf-8').strip()
                #tweetid = json_val["id"]
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
                tweetData = open('AFLtweetsDBStreamResults.csv','a')
                #tweet_details = tweet_id+"::"+"@"+screen_name+"::"+((date).encode('utf-8').strip())+":::"+str(text)
                tweet_details = str(_id)+":::"+((text).encode('utf-8').strip())
                print tweet_details
                tweetData.write(tweet_details)
                tweetData.write('\n')
                tweetData.close()
                
            else:
                print geo
                for word in features:
                    if word in ((text).lower()):
                        print word
                        screen_name = (json_val["user"]["screen_name"]).encode('utf-8').strip()
                        #print screen_name
                        date = str(json_val["created_at"])
                        _id = str(json_val["id"]).encode('utf-8').strip()
                        #tweetid = json_val["id"]
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
                        tweetData = open('AFLtweetsDBStreamResults.csv','a')
                        #tweet_details = tweet_id+"::"+"@"+screen_name+"::"+((date).encode('utf-8').strip())+":::"+str(text)
                        tweet_details = str(_id)+":::"+((text).encode('utf-8').strip())
                        print tweet_details
                        tweetData.write(tweet_details)
                        tweetData.write('\n')
                        tweetData.close()    
                                        
            return True
                    
            
                    
            
        
        except BaseException, e :
            print 'failed onData,',str(e)
            time.sleep(2)
                


    def on_error(self,status):
        print status




for x in combos(featurelist,1000000): 
    features.append(x)

for y in other:
    features.append(y)
    
auth = OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)
api = tweepy.API(auth)

twitterStream = Stream(auth,Customlistener())
twitterStream.filter(languages=["en"],track = features,locations=[112.8,-44.1,154.6,-9.5])
