from tweepy import OAuthHandler
import tweepy
import time
import json
import couchdb





savert1 = 0
savert2 = 0
savefc1 = 0
savefc2 = 0
savewt1 = 0
savewt2 = 0
saveft = ""
savefl = ""
savemr1 = 0
savemr2 = 0
savefp = ""

ckey = '7Kk3B38wZNGVKVbOKCLXs2u8J'
csecret = 'gLPsOF1UnZ9tsYoR7Zpmn05WPFIn6FKydvyfnrpdPqI7BKKZyJ'
atoken = '129674370-Z6Fhod4lrbpy3d8qGOSWhQT4jlcBCqD41UTrTmrN'
asecret = '1BdAJuffVxhS93yFup8oq9zc9umxSt2Ii4NAYxsk0WB4p'
#query = ["afl","afl challenge","australian football league","kangas","carlscum","carltank","blue baggers","mayblooms","hula hoops","carlton blues","hawthorn hawks","Adelaide Crows","The crows","Tex Walker","Eddie betts","podsiadly","josh jenkins", "van berlo", "Patrick Dangerfield", "Rory Sloane", "tom lynch", "kerridge",  "David Mackay", "Mackay","Brodie martin","elis yolmen","Thommo","Taylor walker","afl2015","victoriabitter","afl aussie","afl vic","footyseason","aflmelbourne","afl360","thetigers","thedemons","sydneyswans","thesuns","thebombers","thedons","essendonfootballclub","brisbanelions","collingwoodfootballclub","magpies","westernbulldogs","westcoasteagles","stkildafootballclub","thesaints","greaterwesternsydneygiants","gwsgiants","adelaidefootballclub","northmelbournefootballclub","thekangaroos","fremantlefootballclub","thedockers","portadelaidefootballclub","aflpower","hawthornfootballclub","geelongfootballclub","thecats"] 
featurelist = ["afl","afl2015","afl15","australian football league","australianfootballleague","MCG","Collingwood Football Club","collingwoodfc","collingwood_fc","stkildafc","stkilda_fc","collingwoodfootballclub","carlton blues","carltonfc","carlton_fc","hawthorn hawks","hawthornfc","hawthorn_fc","Adelaide Crows","adelaidefc","adelaide_fc","The crows","The Magpies","themagpies","the pies","thepies","St Kilda Football Club","stkildafootballclub","The Saints","thesaints","gocollingwood","gomagpies","gopies","magpiesftw","piesftw","gosaints","saintsftw","stkildaftw","footyseason","aflmelbourne","afl360","thetigers","thedemons","sydneyswans","sydneyfc","thesuns","thebombers","thedons","essendonfootballclub","essendonfc","essendon_fc","brisbanelions","brisbanefc","brisbane_fc","Nick Riewoldt","Jesse White","westernbulldogs","westcoasteagles","Dane Swan","Scott Pendlebury","Shane Savage","Steele Sidebottom","Jack Steven","piesrule","magpiesrule","saintsrule","greaterwesternsydneygiants","greaterwesternsydneyfc","greaterwesternsydney_fc","gwsgiants","adelaidefootballclub","northmelbournefootballclub","northmelbournefc","northmelbourne_fc","thekangaroos","fremantlefootballclub","fremantlefc","fremantle_fc","thedockers","portadelaidefootballclub","portadelaidefc","portadelaide_fc","aflpower","hawthornfootballclub","geelongfootballclub","geelongfc","geelong_fc","thecats"]
other = ["#aflbluestigers","#afldeessuns","#aflswansdons","#afllionspies","#afldogseagles","#aflsaintsgiants","#aflcrowsnorth","#aflfreopower","#aflhawkscats","#afleaglesblues","#afltigersdogs","#aflgiantsdees","#aflpiescrows","#aflpowerswans","#aflsunssaints","#aflcatsfreo","#aflbombershawks","#aflnorthlions","#aflpiessaints","#aflbluesdons","#aflcrowsdees","#aflswansgiants","#aflnorthpower","#afllionstigers","#aflhawksdogs","#aflcatssuns","#afleaglesfreo","#afltigersdees","#aflsaintsblues","#afldonspies","#aflgiantssuns","#aflpowerhawks","#aflfreoswans","#afllionseagles","#aflcatsnorth","#afldogscrows","#aflbluespies","#afltigerscats","#aflswansdogs","#aflsunslions","#aflnorthhawks","#afleaglesgiants","#afldeesfreo","#aflsaintsdons","#aflcrowspower","#aflpiescats","#aflnorthtigers","#afldogssaints","#aflgiantshawks","#aflsunscrows","#afldeesswans","#aflfreodons","#aflblueslions","#aflpowereagles","#afldonsnorth","#aflcrowssaints","#aflhawksdees","#aflbluesgiants","#aflswanscats","#afleaglessuns","#afldogsfreo","#afltigerspies","#afllionspower","#aflcatsblues","#aflsaintseagles","#aflgiantscrows","#aflsunspies","#aflhawksswans","#aflfreonorth","#afldonslions","#afldeesdogs","#aflpowertigers","#aflswansblues","#aflhawkssuns","#afldeespower","#afldogsgiants","#afltigersdons","#aflcrowsfreo","#afllionssaints","#aflpiesnorth","#afleaglescats","#aflfreotigers","#aflbluescrows","#aflsunsswans","#afldonscats","#aflpowerdogs","#aflgiantslions","#aflnortheagles","#aflsaintshawks","#afldeespies","#aflpowercats","#aflsunsfreo","#afleaglesdons","#aflnorthswans","#aflpiesgiants","#aflsaintsdees","#aflcrowshawks","#afltigerseagles","#aflbluespower","#aflgiantsnorth","#afldogslions","#aflcatsdees","#aflfreopies","#aflswanstigers","#aflhawksdons","#afllionscrows","#aflsaintsdogs","#aflbluessuns","#aflswanspower","#aflpieshawks","#afltigersgiants","#aflsunsnorth""#afldogsblues","#afldeeseagles","#afldonssaints","#aflcrowscats","#aflfreolions","#aflpowerpies","#afltigersblues","#afldonsdees","#afldogssuns","#aflnorthcats","#afleaglescrows","#aflgiantssaints","#aflhawksfreo","#afllionsswans","#aflnorthdons","#aflcatsdogs","#aflsunsgiants","#aflpieseagles","#aflswanshawks","#aflfreoblues","#afldeeslions","#aflpowercrows","#aflsaintstigers","#aflblueshawks","#aflgiantscats","#aflcrowssuns","#afltigersfreo","#afldonspower","#afllionsnorth","#afldogspies","#afldeessaints","#afleaglesswans","#aflhawkstigers","#aflcatslions","#aflpiesdees","#aflswanscrows","#aflbluesnorth","#aflsunseagles","#aflpowersaints","#afldonsdogs","#aflfreogiants","#aflcrowstigers","#aflpiesblues","#afldogspower","#afllionssuns","#afleagleshawks","#aflcatsswans","#afldeesnorth","#aflgiantsdons","#aflsaintsfreo","#aflswanspies","#afldonscrows","#aflnorthsaints","#aflpowergiants","#aflcatshawks","#afllionsblues","#afltigerssuns","#afldogsdees","#aflfreoeagles","#aflhawkspower","#aflpiestigers","#aflgiantsswans","#aflsunsdons","#aflsaintscats","#aflcrowslions","#aflnorthfreo","#aflbluesdees","#afleaglesdogs","#aflcatspies","#aflgiantsblues","#aflhawkslions","#aflnorthdogs","#afldonstigers","#aflsunspower","#aflcrowseagles","#aflsaintsswans","#aflfreodees","#aflhawksblues","#aflcatscrows","#afltigersnorth","#aflpowerfreo","#aflpiesdons","#aflswanssuns","#afldeesgiants","#afleaglessaints","#afllionsdogs"]



#TeamsPlayers:
carltonpl = ["Marc","Murphy","MarcMurphy","MurphyMarc","Bryce","Gibbs","BryceGibbs","GibbsBryce","Kade","Simpson","KadeSimpson","SimpsonKade","Sam","Docherty","SamDocherty","DochertySam","Andrew","Carrazzo","AndrewCarrazzo","CarrazzoAndrew","Tom","Bell","TomBell","BellTom","Chris","Judd","ChrisJudd","JuddChris","Andrew","Walker","AndrewWalker","WalkerAndrew","Andrejs","Everitt","AndrejsEveritt","EverittAndrejs","Patrick","Cripps","PatrickCripps","CrippsPatrick","Zach","Tuohy","ZachTuohy","TuohyZach","Edward","Curnow","EdwardCurnow","CurnowEdward","Christopher","Yarran","ChristopherYarran","YarranChristopher","Levi","Casboult","LeviCasboult","CasboultLevi","Dennis","Armfield","DennisArmfield","ArmfieldDennis","Troy","Menzel","TroyMenzel","MenzelTroy","Cameron","Wood","CameronWood","WoodCameron","Lachlan","Henderson","LachlanHenderson","HendersonLachlan","David","Ellard","DavidEllard","EllardDavid","Sam","Rowe","SamRowe","RoweSam","Ciaran","Byrne","CiaranByrne","ByrneCiaran","Clem","Smith","ClemSmith","SmithClem","Jason","Tutt","JasonTutt","TuttJason","Michael","Jamison","MichaelJamison","JamisonMichael","Simon","White","SimonWhite","WhiteSimon","Liam","Jones","LiamJones","JonesLiam","Kristian","Jaksch","KristianJaksch","JakschKristian","Dale","Thomas","DaleThomas","ThomasDale"]
geelongpl = ["Joel","Selwood","JoelSelwood","SelwoodJoel","Steven","Motlop","StevenMotlop","MotlopSteven","James","Kelly","JamesKelly","KellyJames","Steve","Johnson","SteveJohnson","JohnsonSteve","Corey","Enright","CoreyEnright","EnrightCorey","Cameron","Guthrie","CameronGuthrie","GuthrieCameron","Jackson","Thurlow","JacksonThurlow","ThurlowJackson","Mark","Blicavs","MarkBlicavs","BlicavsMark","Harry","Taylor","HarryTaylor","TaylorHarry","George","Horlin-Smith","GeorgeHorlin-Smith","Horlin-SmithGeorge","Josh","Caddy","JoshCaddy","CaddyJosh","Mathew","Stokes","MathewStokes","StokesMathew","Mitchell","Duncan","MitchellDuncan","DuncanMitchell","Andrew","Mackie","AndrewMackie","MackieAndrew","Jimmy","Bartel","JimmyBartel","BartelJimmy","Darcy","Lang","DarcyLang","LangDarcy","Billie","Smedts","BillieSmedts","SmedtsBillie","Cory","Gregson","CoryGregson","GregsonCory","Tom","Lonergan","TomLonergan","LonerganTom","Mitchell","Clark","MitchellClark","ClarkMitchell","Rhys","Stanley","RhysStanley","StanleyRhys","Jared","Rivers","JaredRivers","RiversJared","Joshua","Walker","JoshuaWalker","WalkerJoshua","Jed","Bews","JedBews","BewsJed","Tom","Hawkins","TomHawkins","HawkinsTom","Jordan","Murdoch","JordanMurdoch","MurdochJordan","Dawson","Simpson","DawsonSimpson","SimpsonDawson","Nakia","Cockatoo","NakiaCockatoo","CockatooNakia"]
fremantlepl = ["Nathan","Fyfe","NathanFyfe","FyfeNathan","David","Mundy","DavidMundy","MundyDavid","Lachie","Neale","LachieNeale","NealeLachie","Stephen","Hill","StephenHill","HillStephen","Michael","Barlow","MichaelBarlow","BarlowMichael","Danyle","Pearce","DanylePearce","PearceDanyle","Michael","Johnson","MichaelJohnson","JohnsonMichael","Paul","Duffield","PaulDuffield","DuffieldPaul","Thomas","Sheridan","ThomasSheridan","SheridanThomas","Garrick","Ibbotson","GarrickIbbotson","IbbotsonGarrick","Matthew","Pavlich","MatthewPavlich","PavlichMatthew","Clancee","Pearce","ClanceePearce","PearceClancee","Lee","Spurr","LeeSpurr","SpurrLee","Luke","McPharlin","LukeMcPharlin","McPharlinLuke","Nicholas","Suban","NicholasSuban","SubanNicholas","Michael","Walters","MichaelWalters","WaltersMichael","Cameron","Sutcliffe","CameronSutcliffe","SutcliffeCameron","Christopher","Mayne","ChristopherMayne","MayneChristopher","Hayden","Ballantyne","HaydenBallantyne","BallantyneHayden","Aaron","Sandilands","AaronSandilands","SandilandsAaron","Zachary","Clarke","ZacharyClarke","ClarkeZachary","Matthew","Taberner","MatthewTaberner","TabernerMatthew","Matthew","De","Boer","MatthewDe","MatthewBoer","DeMatthew","DeBoer","BoerMatthew","BoerDe","MatthewDeBoer","MatthewBoerDe","DeMatthewBoer","DeBoerMatthew","BoerMatthewDe","BoerDeMatthew","Hayden","Crozier","HaydenCrozier","CrozierHayden"]
hawkspl = ["Jordan","Lewis","JordanLewis","LewisJordan","Luke","Hodge","LukeHodge","HodgeLuke","Grant","Birchall","GrantBirchall","BirchallGrant","Isaac","Smith","IsaacSmith","SmithIsaac","Billy","Hartung","BillyHartung","HartungBilly","Sam","Mitchell","SamMitchell","MitchellSam","Josh","Gibson","JoshGibson","GibsonJosh","Matthew","Suckling","MatthewSuckling","SucklingMatthew","William","Langford","WilliamLangford","LangfordWilliam","Shaun","Burgoyne","ShaunBurgoyne","BurgoyneShaun","Taylor","Duryea","TaylorDuryea","DuryeaTaylor","Jarryd","Roughead","JarrydRoughead","RougheadJarryd","Bradley","Hill","BradleyHill","HillBradley","Cyril","Rioli","CyrilRioli","RioliCyril","Jonathan","O'Rourke","JonathanO'Rourke","O'RourkeJonathan","Jack","Gunston","JackGunston","GunstonJack","Jonathon","Ceglar","JonathonCeglar","CeglarJonathon","Paul","Puopolo","PaulPuopolo","PuopoloPaul","Brian","Lake","BrianLake","LakeBrian","Luke","Breust","LukeBreust","BreustLuke","Benjamin","Stratton","BenjaminStratton","StrattonBenjamin","Brendan","Whitecross","BrendanWhitecross","WhitecrossBrendan","Liam","Shiels","LiamShiels","ShielsLiam","James","Sicily","JamesSicily","SicilyJames","James","Frawley","JamesFrawley","FrawleyJames","Jed","Anderson","JedAnderson","AndersonJed","Ben","McEvoy","BenMcEvoy","McEvoyBen"]
stkildapl = ["David","Armitage","DavidArmitage","ArmitageDavid","Jack","Steven","JackSteven","StevenJack","Adam","Schneider","AdamSchneider","SchneiderAdam","Leigh","Montagna","LeighMontagna","MontagnaLeigh","Shane","Savage","ShaneSavage","SavageShane","Sam","Fisher","SamFisher","FisherSam","Jack","Newnes","JackNewnes","NewnesJack","Luke","Dunstan","LukeDunstan","DunstanLuke","Dylan","Roberton","DylanRoberton","RobertonDylan","Jack","Billings","JackBillings","BillingsJack","Sean","Dempster","SeanDempster","DempsterSean","Jarryn","Geary","JarrynGeary","GearyJarryn","Nick","Riewoldt","NickRiewoldt","RiewoldtNick","Maverick","Weller","MaverickWeller","WellerMaverick","Cameron","Shenton","CameronShenton","ShentonCameron","Thomas","Curren","ThomasCurren","CurrenThomas","Jack","Sinclair","JackSinclair","SinclairJack","Josh","Bruce","JoshBruce","BruceJosh","Tim","Membrey","TimMembrey","MembreyTim","Jack","Loniev","JackLonie","LonieJack","Nathan","Wright","NathanWright","WrightNathan","Patrick","McCartin","PatrickMcCartin","McCartinPatrick","Billy","Longer","BillyLonger","LongerBilly","Luke","Delaney","LukeDelaney","DelaneyLuke","Ahmed","Saad","AhmedSaad","SaadAhmed","Eli","Templeton","EliTempleton","TempletonEli"]
collingwoodpl = ["Dane","Swan","DaneSwan","SwanDane","Scott","Pendlebury","ScottPendlebury","PendleburyScott","Taylor","Adams","TaylorAdams","AdamsTaylor","Tom","Langdon","TomLangdon","LangdonTom","Timothy","Broomhead","TimothyBroomhead","BroomheadTimothy","Adam","Oxley","AdamOxley","OxleyAdam","Jarryd","Blair","JarrydBlair","BlairJarryd","Steele","Sidebottom","SteeleSidebottom","SidebottomSteele","Jack","Crisp","JackCrisp","CrispJack","Jackson","Ramsay","JacksonRamsay","RamsayJackson","Brodie","Grundy","BrodieGrundy","GrundyBrodie","Sam","Dwyer","SamDwyer","DwyerSam","Paul","Seedsman","PaulSeedsman","SeedsmanPaul","Travis","Varcoe","TravisVarcoe","VarcoeTravis","Marley","Williams","MarleyWilliams","WilliamsMarley","Jamie","Elliott","JamieElliott","ElliottJamie","Jesse","White","JesseWhite","WhiteJesse","Travis","Cloke","TravisCloke","ClokeTravis","Alan","Toovey","AlanToovey","TooveyAlan","Alex","Fasolo","AlexFasolo","FasoloAlex","Tyson","Goldsack","TysonGoldsack","GoldsackTyson","Ben","Sinclair","BenSinclair","SinclairBen","Nathan","Brown","NathanBrown","BrownNathan","Patrick","Karnezis","PatrickKarnezis","KarnezisPatrick","Corey","Gault","CoreyGault","GaultCorey","Jack","Frost","JackFrost","FrostJack","Jordan","De","Goey","JordanDe","JordanGoey","DeJordan","DeGoey","GoeyJordan","GoeyDe","JordanDeGoey","JordanGoeyDe","DeJordanGoey","DeGoeyJordan","GoeyJordanDe","GoeyDeJordan"]
essendonpl = ["Jobe","Watson","JobeWatson","WatsonJobe","Dyson","Heppell","DysonHeppell","HeppellDyson","Brendon","Goddard","BrendonGoddard","GoddardBrendon","Michael","Hurley","MichaelHurley","HurleyMichael","Brent","Stanton","BrentStanton","StantonBrent","Cale","Hooker","CaleHooker","HookerCale","Jake","Melksham","JakeMelksham","MelkshamJake","Michael","Hibberd","MichaelHibberd","HibberdMichael","Zachary","Merrett","ZacharyMerrett","MerrettZachary","David","Zaharakis","DavidZaharakis","ZaharakisDavid","Dustin","Fletcher","DustinFletcher","FletcherDustin","Travis","Colyer","TravisColyer","ColyerTravis","Martin","Gleeson","MartinGleeson","GleesonMartin","Mark","Baguley","MarkBaguley","BaguleyMark","Ben","Howlett","BenHowlett","HowlettBen","Adam","Cooney","AdamCooney","CooneyAdam","Patrick","Ambrose","PatrickAmbrose","AmbrosePatrick","Paul","Chapman","PaulChapman","ChapmanPaul","James","Gwilt","JamesGwilt","GwiltJames","Joe","Daniher","JoeDaniher","DaniherJoe","Tom","Bellchambers","TomBellchambers","BellchambersTom","Jake","Carlisle","JakeCarlisle","CarlisleJake","Jason","Ashby","JasonAshby","AshbyJason","David","Myers","DavidMyers","MyersDavid"]
goldcoastpl = ["Dion","Prestia","DionPrestia","PrestiaDion","Michael","Rischitelli","MichaelRischitelli","RischitelliMichael","Harley","Bennell","HarleyBennell","BennellHarley","Gary","Jnr","Ablett","GaryJnr","GaryAblett","JnrGary","JnrAblett","AblettGary","AblettJnr","GaryJnrAblett","GaryAblettJnr","JnrGaryAblett","JnrAblettGary","AblettGaryJnr","AblettJnrGary","David","Swallow","DavidSwallow","SwallowDavid","Jarrod","Harbrow","JarrodHarbrow","HarbrowJarrod","Mitchell","Hallahan","MitchellHallahan","HallahanMitchell","Adam","Saad","AdamSaad","SaadAdam","Jack","Martin","JackMartin","MartinJack","Trent","McKenzie","TrentMcKenzie","McKenzieTrent","Steven","May","StevenMay","MaySteven","Nick","Malceski","NickMalceski","MalceskiNick","Matt","Shaw","MattShaw","ShawMatt","Kade","Kolodjashnij","KadeKolodjashnij","KolodjashnijKade","Thomas","Lynch","ThomasLynch","LynchThomas","Aaron","Hall","AaronHall","HallAaron","Sean","Lemmens","SeanLemmens","LemmensSean","Greg","Broughton","GregBroughton","BroughtonGreg","Touk","Miller","ToukMiller","MillerTouk","Brandon","Matera","BrandonMatera","MateraBrandon","Zac","Smith","ZacSmith","SmithZac","Sebastian","Tape","SebastianTape","TapeSebastian","Jarrod","Garlett","JarrodGarlett","GarlettJarrod","Daniel","Gorringe","DanielGorringe","GorringeDaniel","Alex","Sexton","AlexSexton","SextonAlex","Rory","Thompson","RoryThompson","ThompsonRory","Sam","Day","SamDay","DaySam"]
adelaidepl = ["Scott","Thompson","ScottThompson","ThompsonScott","Rory","Sloane","RorySloane","SloaneRory","Richard","Douglas","RichardDouglas","DouglasRichard","Patrick","Dangerfield","PatrickDangerfield","DangerfieldPatrick","Brodie","Smith","BrodieSmith","SmithBrodie","Matthew","Jaensch","MatthewJaensch","JaenschMatthew","Cameron","Ellis-Yolmen","CameronEllis-Yolmen","Ellis-YolmenCameron","Rory","Laird","RoryLaird","LairdRory","Ricky","Henderson","RickyHenderson","HendersonRicky","Daniel","Talia","DanielTalia","TaliaDaniel","Tom","Lynch","TomLynch","LynchTom","Taylor","Walker","TaylorWalker","WalkerTaylor","Kyle","Hartigan","KyleHartigan","HartiganKyle","Eddie","Betts","EddieBetts","BettsEddie","David","MacKay","DavidMacKay","MacKayDavid","Kyle","Cheney","KyleCheney","CheneyKyle","Sam","Jacobs","SamJacobs","JacobsSam","Nathan","Van","Berlo","NathanVan","NathanBerlo","VanNathan","VanBerlo","BerloNathan","BerloVan","NathanVanBerlo","NathanBerloVan","VanNathanBerlo","VanBerloNathan","BerloNathanVan","BerloVanNathan","Josh","Jenkins","JoshJenkins","JenkinsJosh","Luke","Brown","LukeBrown","BrownLuke","Jarryd","Lyons","JarrydLyons","LyonsJarryd","Mitchell","Grigg","MitchellGrigg","GriggMitchell","Charlie","Cameron","CharlieCameron","CameronCharlie","Matthew","Wright","MatthewWright","WrightMatthew","Jake","Kelly","JakeKelly","KellyJake"]
westcoastpl = ["Matthew","Priddis","MatthewPriddis","PriddisMatthew","Chris","Masten","ChrisMasten","MastenChris","Andrew","Gaff","AndrewGaff","GaffAndrew","Matthew","Rosa","MatthewRosa","RosaMatthew","Luke","Shuey","LukeShuey","ShueyLuke","Dominic","Sheed","DominicSheed","SheedDominic","Scott","Selwood","ScottSelwood","SelwoodScott","Jeremy","McGovern","JeremyMcGovern","McGovernJeremy","Mark","Lecras","MarkLecras","LecrasMark","Bradley","Sheppard","BradleySheppard","SheppardBradley","Sam","Butler","SamButler","ButlerSam","Shannon","Hurn","ShannonHurn","HurnShannon","Will","Schofield","WillSchofield","SchofieldWill","Sharrod","Wellingham","SharrodWellingham","WellinghamSharrod","Elliot","Yeo","ElliotYeo","YeoElliot","Joshua","Kennedy","JoshuaKennedy","KennedyJoshua","Jamie","Cripps","JamieCripps","CrippsJamie","Nicholas","Naitanui","NicholasNaitanui","NaitanuiNicholas","Jackson","Nelson","JacksonNelson","NelsonJackson","Jamie","Bennell","JamieBennell","BennellJamie","Josh","Hill","JoshHill","HillJosh","Tom","Lamb","TomLamb","LambTom","Simon","Tunbridgev","SimonTunbridge","TunbridgeSimon","Scott","Lycett","ScottLycett","LycettScott","Patrick","McGinnity","PatrickMcGinnity","McGinnityPatrick","Liam","Duggan","LiamDuggan","DugganLiam","Mitchell","Brown","MitchellBrown","BrownMitchell"]
northmelbournepl = ["Sam","Gibson","SamGibson","GibsonSam","Andrew","Swallow","AndrewSwallow","SwallowAndrew","Ben","Cunnington","BenCunnington","CunningtonBen","Brent","Harvey","BrentHarvey","HarveyBrent","Robbie","Tarrant","RobbieTarrant","TarrantRobbie","Ben","Jacobs","BenJacobs","JacobsBen","Shaun","Higgins","ShaunHiggins","HigginsShaun","Luke","McDonald","LukeMcDonald","McDonaldLuke","Nick","Dal","Santo","NickDal","NickSanto","DalNick","DalSanto","SantoNick","SantoDal","NickDalSanto","NickSantoDal","DalNickSanto","DalSantoNick","SantoNickDal","SantoDalNick","Robin","Nahas","RobinNahas","NahasRobin","Jamie","MacMillan","JamieMacMillan","MacMillanJamie","Shaun","Atley","ShaunAtley","AtleyShaun","Ryan","Bastinac","RyanBastinac","BastinacRyan","Samuel","Wright","SamuelWright","WrightSamuel","Todd","Goldstein","ToddGoldstein","GoldsteinTodd","Jack","Ziebell","JackZiebell","ZiebellJack","Mason","Wood","MasonWood","WoodMason","Scott","Thompson","ScottThompson","ThompsonScott","Jarrad","Waite","JarradWaite","WaiteJarrad","Lindsay","Thomas","LindsayThomas","ThomasLindsay","Drew","Petrie","DrewPetrie","PetrieDrew","Michael","Firrito","MichaelFirrito","FirritoMichael","Kayne","Turner","KayneTurner","TurnerKayne","Daniel","Wells","DanielWells","WellsDaniel","Ben","Brown","BenBrown","BrownBen","Joel","Tippett","JoelTippett","TippettJoel"]
portadelaidepl = ["Robbie","Gray","RobbieGray","GrayRobbie","Brad","Ebert","BradEbert","EbertBrad","Oliver","Wines","OliverWines","WinesOliver","Jasper","Pittard","JasperPittard","PittardJasper","Travis","Boak","TravisBoak","BoakTravis","Jared","Polec","JaredPolec","PolecJared","Hamish","Hartlett","HamishHartlett","HartlettHamish","Kane","Cornes","KaneCornes","CornesKane","Chad","Wingard","ChadWingard","WingardChad","Thomas","Jonas","ThomasJonas","JonasThomas","Matthew","Broadbent","MatthewBroadbent","BroadbentMatthew","Aaron","Young","AaronYoung","YoungAaron","Jackson","Trengove","JacksonTrengove","TrengoveJackson","Nathan","Krakouer","NathanKrakouer","KrakouerNathan","Justin","Westhoff","JustinWesthoff","WesthoffJustin","Kane","Mitchell","KaneMitchell","MitchellKane","Angus","Monfries","AngusMonfries","MonfriesAngus","Alipate","Carlile","AlipateCarlile","CarlileAlipate","Jay","Schulz","JaySchulz","SchulzJay","Jake","Neade","JakeNeade","NeadeJake","Matthew","White","MatthewWhite","WhiteMatthew","Patrick","Ryder","PatrickRyder","RyderPatrick","Jack","Hombsch","JackHombsch","HombschJack","Jarman","Impey","JarmanImpey","ImpeyJarman","Jarrad","Redden","JarradRedden","ReddenJarrad","John","Butcher","JohnButcher","ButcherJohn","Brendon","Ah","Chee","BrendonAh","BrendonChee","AhBrendon","AhChee","CheeBrendon","CheeAh","BrendonAhChee","BrendonCheeAh","AhBrendonChee","AhCheeBrendon","CheeBrendonAh","CheeAhBrendon"]
sydneyswanspl = ["Josh","Kennedy","JoshP","JoshKennedy","P.Josh","P.Kennedy","KennedyJosh","KennedyP","JoshP.Kennedy","JoshKennedyP.","P.JoshKennedy","P.KennedyJosh","KennedyJosh","KennedyP.Josh","Daniel","Hannebery","DanielHannebery","HanneberyDaniel","Kieren","Jack","KierenJack","JackKieren","Jarrad","McVeigh","JarradMcVeigh","McVeighJarrad","Luke","Parker","LukeParker","ParkerLuke","Craig","Bird","CraigBird","BirdCraig","Nick","Smith","NickSmith","SmithNick","Heath","Grundy","HeathGrundy","GrundyHeath","Harry","Cunningham","HarryCunningham","CunninghamHarry","Jake","Lloyd","JakeLloyd","LloydJake","Rhyce","Shaw","RhyceShaw","ShawRhyce","Dane","Rampe","DaneRampe","RampeDane","Lewis","Jetta","LewisJetta","JettaLewis","Jeremy","Laidler","JeremyLaidler","LaidlerJeremy","Lance","Franklin","LanceFranklin","FranklinLance","Isaac","Heeney","IsaacHeeney","HeeneyIsaac","Ben","McGlynn","BenMcGlynn","McGlynnBen","Gary","Rohan","GaryRohan","RohanGary","Dean","Towers","DeanTowers","TowersDean","Sam","Reid","SamReid","ReidSam","Ted","Richards","TedRichards","RichardsTed","Mike","Pyke","MikePyke","PykeMike","Kurt","Tippett","KurtTippett","TippettKurt","Adam","Goodes","AdamGoodes","GoodesAdam"]
richmondtigerspl = ["Trent","Cotchin","TrentCotchin","CotchinTrent","Anthony","Miles","AnthonyMiles","MilesAnthony","Brandon","Ellis","BrandonEllis","EllisBrandon","Bachar","Houli","BacharHouli","HouliBachar","Dustin","Martin","DustinMartin","MartinDustin","Shane","Edwards","ShaneEdwards","EdwardsShane","Taylor","Hunt","TaylorHunt","HuntTaylor","Shaun","Grigg","ShaunGrigg","GriggShaun","Kamdyn","Mcintosh","KamdynMcintosh","McintoshKamdyn","Brett","Deledio","BrettDeledio","DeledioBrett","Alex","Rance","AlexRance","RanceAlex","Troy","Chaplin","TroyChaplin","ChaplinTroy","Ricky","Petterd","RickyPetterd","PetterdRicky","Nick","Vlastuin","NickVlastuin","VlastuinNick","Jack","Riewoldt","JackRiewoldt","RiewoldtJack","Chris","Newman","ChrisNewman","NewmanChris","Benjamin","Griffiths","BenjaminGriffiths","GriffithsBenjamin","Ivan","Maric","IvanMaric","MaricIvan","Sam","Lloyd","SamLloyd","LloydSam","David","Astbury","DavidAstbury","AstburyDavid","Nathan","Gordon","NathanGordon","GordonNathan","Jake","Batchelor","JakeBatchelor","BatchelorJake","Dylan","Grimes","DylanGrimes","GrimesDylan","Matthew","Arnot","MatthewArnot","ArnotMatthew","Matthew","Mcdonough","MatthewMcdonough","McdonoughMatthew","Steven","Morris","StevenMorris","MorrisSteven","Kane","Lambert","KaneLambert","LambertKane","Nathan","Drummond","NathanDrummond","DrummondNathan","Chris","Knights","ChrisKnights","KnightsChris"]
westernbullpl = ["Matthew","Boyd","MatthewBoyd","BoydMatthew","Jackson","Macrae","JacksonMacrae","MacraeJackson","Luke","Dahlhaus","LukeDahlhaus","DahlhausLuke","Marcus","Bontempelli","MarcusBontempelli","BontempelliMarcus","Robert","Murphy","RobertMurphy","MurphyRobert","Lin","Jong","LinJong","JongLin","Mitchell","Wallis","MitchellWallis","WallisMitchell","Jason","Johannisen","JasonJohannisen","JohannisenJason","Michael","Talia","MichaelTalia","TaliaMichael","Stewart","Crameri","StewartCrameri","CrameriStewart","Nathan","Hrovat","NathanHrovat","HrovatNathan","Easton","Wood","EastonWood","WoodEaston","Koby","Stevens","KobyStevens","StevensKoby","Mitch","Honeychurch","MitchHoneychurch","HoneychurchMitch","Liam","Picken","LiamPicken","PickenLiam","Tory","Dickson","ToryDickson","DicksonTory","Will","Minson","WillMinson","MinsonWill","Jake","Stringer","JakeStringer","StringerJake","Jordan","Roughead","JordanRoughead","RougheadJordan","Lukas","Webb","LukasWebb","WebbLukas","Thomas","Boyd","ThomasBoyd","BoydThomas","Jarrad","Grant","JarradGrant","GrantJarrad","Dale","Morris","DaleMorris","MorrisDale","Brett","Goodes","BrettGoodes","GoodesBrett","Jack","Redpath","JackRedpath","RedpathJack","Ayce","Cordy","AyceCordy","CordyAyce"]
gwsgiantspl = ["Lachie","Whitfield","LachieWhitfield","WhitfieldLachie","Adam","Treloar","AdamTreloar","TreloarAdam","Toby","Greene","TobyGreene","GreeneToby","Callan","Ward","CallanWard","WardCallan","Joshua","Kelly","JoshuaKelly","KellyJoshua","Dylan","Shiel","DylanShiel","ShielDylan","Heath","Shaw","HeathShaw","ShawHeath","Tom","Scully","TomScully","ScullyTom","Devon","Smith","DevonSmith","SmithDevon","Stephen","Coniglio","StephenConiglio","ConiglioStephen","Ryan","Griffen","RyanGriffen","GriffenRyan","Tomas","Bugg","TomasBugg","BuggTomas","Nick","Haynes","NickHaynes","HaynesNick","Rhys","Palmer","RhysPalmer","PalmerRhys","Phil","Davis","PhilDavis","DavisPhil","Shane","Mumford","ShaneMumford","MumfordShane","Cameron","McCarthy","CameronMcCarthy","McCarthyCameron","Joel","Patfull","JoelPatfull","PatfullJoel","Curtly","Hampton","CurtlyHampton","HamptonCurtly","Jeremy","Cameron","JeremyCameron","CameronJeremy","Aidan","Corr","AidanCorr","CorrAidan","Nathan","Wilson","NathanWilson","WilsonNathan","Adam","Tomlinson","AdamTomlinson","TomlinsonAdam","Andrew","Phillips","AndrewPhillips","PhillipsAndrew"]
melbdemonspl = ["Jack","Viney","JackViney","VineyJack","Nathan","Jones","NathanJones","JonesNathan","Daniel","Cross","DanielCross","CrossDaniel","Tom","McDonald","TomMcDonald","McDonaldTom","Viv","Michie","VivMichie","MichieViv","Dom","Tyson","DomTyson","TysonDom","Aaron","Vandenberg","AaronVandenberg","VandenbergAaron","Heritier","Lumumba","HeritierLumumba","LumumbaHeritier","Jeremy","Howe","JeremyHowe","HoweJeremy","Bernie","Vince","BernieVince","VinceBernie","Ben","Newton","BenNewton","NewtonBen","Christian","Salem","ChristianSalem","SalemChristian","Jack","Watts","JackWatts","WattsJack","Jeff","Garlett","JeffGarlett","GarlettJeff","Lynden","Dunn","LyndenDunn","DunnLynden","Colin","Garland","ColinGarland","GarlandColin","Jesse","Hogan","JesseHogan","HoganJesse","Chris","Dawes","ChrisDawes","DawesChris","Jay","Kennedy-Harris","JayKennedy-Harris","Kennedy-HarrisJay","Angus","Brayshaw","AngusBrayshaw","BrayshawAngus","Neville","Jetta","NevilleJetta","JettaNeville","Dean","Kent","DeanKent","KentDean","Sam","Frost","SamFrost","FrostSam","Mark","Jamar","MarkJamar","JamarMark","Jimmy","Toumpas","JimmyToumpas","ToumpasJimmy"]
brisblionspl = ["Dayne","Beams","DayneBeams","BeamsDayne","Daniel","Rich","DanielRich","RichDaniel","Dayne","Zorko","DayneZorko","ZorkoDayne","Jack","Redden","JackRedden","ReddenJack","Mitch","Robinson","MitchRobinson","RobinsonMitch","Allen","Christensen","AllenChristensen","ChristensenAllen","Tom","Rockliff","TomRockliff","RockliffTom","Marco","Paparone","MarcoPaparone","PaparoneMarco","James","Aish","JamesAish","AishJames","Stefan","Martin","StefanMartin","MartinStefan","Jed","Adcock","JedAdcock","AdcockJed","Claye","Beams","ClayeBeams","BeamsClaye","Lewis","Taylor","LewisTaylor","TaylorLewis","Daniel","Merrett","DanielMerrett","MerrettDaniel","Rohan","Bewick","RohanBewick","BewickRohan","Zac","O'Brien","ZacO'Brien","O'BrienZac","Joshua","Green","JoshuaGreen","GreenJoshua","Jaden","McGrath","JadenMcGrath","McGrathJaden","Justin","Clarke","JustinClarke","ClarkeJustin","Ryan","Lester","RyanLester","LesterRyan","Darcy","Gardiner","DarcyGardiner","GardinerDarcy","Harris","Andrews","HarrisAndrews","AndrewsHarris","Matthew","Maguire","MatthewMaguire","MaguireMatthew","Daniel","McStay","DanielMcStay","McStayDaniel","Matthew","Leuenberger","MatthewLeuenberger","LeuenbergerMatthew","Sam","Mayes","SamMayes","MayesSam","Brent","Staker","BrentStaker","StakerBrent","Michael","Close","MichaelClose","CloseMichael"]


#Teams:
#collingwood = "collingwood_fc","collingwoodfc","aflpies","aflcollingwood","collingwoodfootball","collingwoodpies","gocollingwood","collingwoodsuck","piessuck","gopies","piesftw","piesrule","thepies"
#geelong = "aflcats","aflgeelong","geelongfootball","geelongfc","geelong_fc","geelongcats","gogeelong","geelongsuck","geelongrule","thecats","gocats","catssuck"
#richmond = "afltigers","aflrichmond","richmondfootball","richmondtigers","richmondfc","richmond_fc","gorichmond","richmondftw","richmondsuck","richmondrule","tigerssuck","tigersftw","tigersrule","thetigers"
#northmelb = "aflkanga","aflnorth","northmelbournefootball","northmelbournefc","northmelbourne_fc","gonorthmelbourne","gonorth","northftw","northmelbourneftw","northmelbournerule","northmelbornesuck","thekangaroos","gokangaroo","kangaroosftw","kangaroosrule","kangaroossuck"
#westernbulldogs ="afldogs","aflbulldogs","aflwesternbulldogs","footscrayfootball","westernbulldogs","footscrayfc","footscray_fc","gofootscray","gowesternbulldogs","gobulldogs","bulldogsftw","footscrayftw","westernbulldogsftw","westernbulldogsrule","bulldogsrule","bulldogssuck"
#stkilda = "stkildafc","stkilda_fc","stkildafootball","stkildafootball","aflstkilda","aflkilda","aflsaint","aflthesaints","gostkilda","gosaints","gokilda","stkildaftw","saintsftw","saintsrule","kildarule","kildasuck","saintssuck","thesaints"
#essendon = "afldon","aflbomber","aflessendon","essendonfootball","essendonfc","essendon_fc","goessendon","gobombers","godons","essendonftw","bombersftw","donsftw","essendonrule","bombersrule","donsrule","bomberssuck","donssuck","essendonsuck","thedons","thebombers"
#sydney = "aflswans","sydneyswans","theswans","swansrule","swanssuck","aflsydneyswans","goswans","sydneyswansftw","swansftw"
#carlton = "aflblues","aflcarlton","carltonfootball","carltonblues","carltonfc","carlton_fc","gocarlton","carltonftw","carltonsuck","carltonrule","goblues","bluessuck"
#goldcoast = "aflsuns","aflgoldcoast","goldcoastfootball","goldcoastfc","goldcoast_fc","thesuns","sunssuck","goldcoastsuck","gosuns","sunsrule","gogoldcoast","goldcoastrule","sunsftw","goldcoastftw"
#brisbane = "afllions","aflbrisbane","brisbanefc","brisbanefootball","brisbane_fc","thelions","brisbanelions","brisbaneftw","brisbanerule","lionsftw","lionsrule","golions","gobrisbane","lionssuck","brisbanesuck"
#hawthorn = "aflhawthorn","aflhawk","aflhawks","hawthornhawks","hawthornfootball","hawthornfc","hawthorn_fc","gohawks","gohawthorn","hawksftw","thehawks","hawthornftw","hawksrule","hawthornrule","hawthornsuck","hawkssuck"
#westcoast = "westcoastfootball","westcoastfc","westcoast_fc","afleagles","aflwestcoast","westcoasteagles","goeagles","gowestcoast","eaglesftw","westcoastftw","westcoastrule","eaglesrule","eaglessuck","westcoastsuck"
#gwsgiants = "aflgiant","giantsfc","gws_fc","gwsfc","giants_fc","aflgwsgiant","gwsgiant","thegiants","greaterwesternsydney","gogiants","gogwsgiants","giantsftw","giantsrule","gwsrule","giantssuck","gwssuck","aflgws"
#melbourne = "afldemon","afldee","melbournefootball","melbournefc","melbourne_fc","godemon","godee","demonsftw","deesftw","deessuck","deesrule","demonssuck","thedemons"
#fremantle = "afldocker","aflfreo","aflfremantle","fremantlefootballclub","fremantlefc","fremantle_fc","gofremantle","gofreo","fremantleftw","fremantlesuck","fremantlerule","freosftw","freossuck","freosrule","dockersftw","dockersrule","dockerssuck","godockers","dockers"
#adelaide = "afladelaide","aflcrow","adelaidefootball","adelaidefc","adelaide_fc","goadelaide","gocrow","adelaideftw","crowsftw","adelaiderule","crowsrule","adelaidesuck","crowssuck"
#portadelaide = "aflportadelaide","aflport", "aflpower","portadelaidefootball","portadelaidefc","portadelaide_fc","goportadelaide","gopower","portadelaideftw","powersftw","portadelaiderule","powersrule","portadelaidesuck","powerssuck" 


#matches:
#round 4:
carltonvsstkilda= ["stkildafc","stkilda_fc","carlton blues","carltonblues","carltonfc","carlton_fc","St Kilda Football Club","stkildafootballclub","The Saints","thesaints","gocarlton","carltonftw","goblues","thebluesftw","bluesftw","bluesrule","aflbluessaints","aflsaintsblues"]
collingwoodvsessendon = ["aflbomberspies","aflpiesbombers","afldonspies","aflpiesdons","Collingwood Football Club","collingwoodfc","collingwood_fc","The Magpies","magpies","themagpies","the pies","thepies","gocollingwood","gomagpies","gopies","magpiesftw","piesftw","thebombers","piesrule","dons","bombers","magpiesrule","thedons","essendonfootballclub","essendonfc","essendon_fc","goessendon","gobombers","godons","essendonftw","bombersftw","donsftw","essendonrule","bombersrule","donsrule","collingwood suck","essendon suck","essendonsuck","collingwoodsuck","pies suck","magpies suck","magpiessuck","piessuck","bomberssuck","donssuck","bombers suck","dons suck"]

#round 5:
collingwoodvscarlton = ["aflbluespies","aflpiesblues","aflblues","aflpies","aflmagpies","aflcarlton","aflcollingwood","carltonfootball","carltonblues","carltonfc","carlton_fc","gocarlton","carltonftw","collingwoodfootball","collingwoodfc","collingwood_fc","collingwoodpies","thepies","gocollingwood","carltonsuck","collingwoodsuck","magpiessuck","piessuck","carltonrule","collingwoodrule","goblues","bluessuck","magpiesrule","magpies","gomagpies","gopies","magpiesftw","piesftw","piesrule"]
richmondvsgeelong = ["aflcatstigers","afltigerscats","aflcats","afltigers","aflrichmond","aflgeelong","richmondfootball","thetigers","richmondtigers","richmondfc","richmond_fc","gorichmond","richmondftw","geelongfootball","geelongfc","geelong_fc","thecats","geelongcats","gogeelong","gocats","geelongsuck","catssuck","richmondsuck","tigerssuck","geelongrule","richmondrule"]
sydneyvswesternbulldogs = ["aflswansdogs","afldogsswans","aflswansbulldogs","aflbulldogsswans","aflswans","afldogs","aflbulldogs","aflwesternbulldogs","sydneyswans","footscrayfootball","westernbulldogs","theswans","footscrayfc","footscray_fc","gofootscray","gowesternbulldogs","gobulldogs","bulldogsftw","footscrayftw","westernbulldogsftw","westernbulldogsrule","bulldogsrule","swansrule","swanssuck","bulldogssuck"]
goldcoastvsbrisbane = ["aflsunslions","afllionssuns","aflsuns","afllions","aflbrisbane","aflgoldcoast","goldcoastfootballclub","brisbanefc","brisbane_fc","goldcoastfc","goldcoast_fc","thesuns","thelions","brisbanelions","brisbaneftw","brisbanerule","lionsftw","lionsrule","golions","gobrisbane","lionssuck","sunssuck","brisbanesuck","goldcoastsuck"]
northmelbvshawthorn = ["aflnorthhawks","aflhawksnorth","aflkangarooshawks","aflhawkskangaroos","aflhawks","aflkangaroos","northmelbournefootballclub","northmelbournefc","northmelbourne_fc","gokangaroo","gonorthmelbourne","gonorth","kangaroosftw","northftw","northmelbourneftw","kangaroosrule","northmelbournerule","hawthornhawks","hawthornfootballclub","hawthornfc","hawthorn_fc","gohawks","gohawthorn","hawksftw","thehawks","thekangaroos","hawthornftw","hawksrule","hawthornrule","hawthornsuck","hawkssuck","northmelbornesuck","kangaroossuck"]
westcoastvsgws = ["afleaglesgiants","aflgiantseagles","aflgiants","afleagles","aflgreaterwesternsydney","aflwestcoasteagles","aflwestcoast","aflgwsgiants","gwsgiants","thegiants","greaterwesternsydney","westcoasteagles","gogiants","gogwsgiants","goeagles","gowestcoast","giantsftw","eaglesftw","westcoastftw","westcoastrule","eaglesrule","giantsrule","gwsrule","eaglessuck","giantssuck","westcoastsuck","gwssuck"]
stkildavsessendon = ["aflsaintsbombers","aflbomberssaints","aflbommbersaints","aflsaintbomber","afldonssaints","aflsaintsdons","aflsaintdons","afldonsaint","aflstkilda","aflkilda","aflsaint","aflthesaints","stkildafc","stkilda_fc","stkildafootballclub","stkildafootball","afldon","aflbomber","aflessendon","essendonfootballclub","essendonfc","essendon_fc","gostkilda","gosaints","gokilda","stkildaftw","saintsftw","saintsrule","kildarule","kildasuck","saintssuck","goessendon","gobombers","godons","essendonftw","bombersftw","donsftw","essendonrule","bombersrule","donsrule","bomberssuck","donssuck","essendonsuck","thedons","thebombers","thesaints"]
adelaidevsportadelaide = ["aflpowerscrows","aflcrowspowers","aflcrowpower","aflpowercrow","pafc","aflportadelaide","aflport", "aflpower","portadelaidefootball","portadelaidefc","portadelaide_fc","afladelaide","aflcrow","adelaidefootball","adelaidefc","adelaide_fc","goadelaide","gocrow","adelaideftw","crowsftw","adelaiderule","crowsrule","adelaidesuck","crowssuck","goportadelaide","gopower","portadelaideftw","powersftw","portadelaiderule","powersrule","portadelaidesuck","powerssuck"]
melbournevsfremantle = ["afldeesfreo","aflfreodee","afldeesdockers","afldockersdee","aflfreosdee","afldeefreo","afldemon","afldee","melbournefootball","melbournefc","melbourne_fc","godemon","godee","demonsftw","deesftw","deessuck","deesrule","demonssuck","thedemons","afldocker","aflfreo","aflfremantle","fremantlefootballclub","fremantlefc","fremantle_fc","gofremantle","gofreo","fremantleftw","fremantlesuck","fremantlerule","freosftw","freossuck","freosrule","dockersftw","dockersrule","dockerssuck","godockers","dockers"]




#round6
collingwoodvsgeelong = ["aflcatspies","aflmagpiescat","aflcatsmagpie","aflpiescats","aflcatpies","aflpiecats","geelongfc","collingwood_fc","geelong_fc","collingwoodfc","aflpies","aflmagpies","aflcollingwood","aflgeelong","collingwoodfootball","collingwoodpies","gocollingwood","collingwoodsuck","geelongfootball","geelongrule","geelongcats","gogeelong","geelongsuck","catssuck","gocats","thecats","piessuck","gopies","piesftw","piesrule","thepies"]
northmelbvsrichmond = ["afltigerskangaroo","aflnorthtiger","aflnorth","aflkangaroostiger","aflkangastigers","afltigerskanga","afltigerkanga","afltiger","aflrichmond","richmondfootball","richmondtigers","richmondfc","richmond_fc","gorichmond","richmondftw","richmondsuck","richmondrule","aflkanga","aflkangaroos","northmelbournefootball","northmelbournefc","northmelbourne_fc","gonorthmelbourne","northftw","northsuck",'northrule',"northmelbourneftw","northmelbournerule","northmelbornesuck","thekangaroos","gokangaroo","kangaroosftw","kangas","kangaroosrule","kangaroossuck","tigerssuck","tigersftw","tigersrule","thetigers","northvsrichmond","northvrich"]
westernbulldogsvsstkilda = ["aflsaintsdogs","afldogssaints","afldogsaint","aflsaintdog","stkildafc","stkilda_fc","stkildafootball","stkildafootball","aflstkilda","aflkilda","aflsaint","aflthesaints","gostkilda","gosaints","gokilda","stkildaftw","saintsftw","saintsrule","kildarule","kildasuck","saintssuck","thesaints","afldogs","aflbulldogs","aflwesternbulldogs","footscrayfootball","westernbulldogs","footscrayfc","footscray_fc","gofootscray","gowesternbulldogs","gobulldogs","bulldogsftw","footscrayftw","westernbulldogsftw","westernbulldogsrule","bulldogsrule","bulldogssuck"]
gwsvshawthorn = ["aflgiantshawks","aflhawksgiants","aflgianthawk","aflhawkgiant","aflgiant","giantsfc","gws_fc","gwsfc","giants_fc","aflgwsgiant","gwsgiant","thegiants","greaterwesternsydney","gogiants","gogwsgiants","giantsftw","giantsrule","gwsrule","giantssuck","gwssuck","aflgws","aflhawks","hawthornhawks","hawthornfootball","hawthornfc","hawthorn_fc","gohawks","gohawthorn","hawksftw","thehawks","hawthornftw","hawksrule","hawthornrule","hawthornsuck","hawkssuck","aflhawthorn","aflhawk"]
goldcoastvsadelaide = ["aflsunscrows","aflcrowssuns","aflsuncrow","aflcrowsun","crowsvssuns","goldcoastvsadelaide","afladelaide","aflcrow","adelaidefootball","adelaidefc","adelaide_fc","goadelaide","gocrow","adelaideftw","crowsftw","adelaiderule","crowsrule","adelaidesuck","crowssuck","aflsuns","aflgoldcoast","goldcoastfootball","goldcoastfc","goldcoast_fc","thesuns","sunssuck","goldcoastsuck","gosuns","sunsrule","gogoldcoast","goldcoastrule","sunsftw","goldcoastftw"]
melbvssydney = ["afldemonsswans","aflswansdemons","aflswandemon","afldemonswan","afldeesswan","aflswansdee","aflswandee","afldeeswan","afldemon","afldee","melbournefootball","melbournefc","melbourne_fc","godemon","godee","demonsftw","deesftw","deessuck","deesrule","demonssuck","thedemons","aflswans","sydneyswans","theswans","swansrule","swanssuck","aflsydneyswans","goswans","sydneyswansftw","swansftw"]
fremantlevsessendon = ["afldonsdocker","afldockerdon","aflfreodon","afldonfreo","afldondocker","afldockersdon","aflfreosdon","afldonsfreo","aflbomberdocker","aflbombersdocker","afldockerbomber","afldockersbomber","aflfreobomber","aflbombersfreo","aflbomberfreo","aflfreosbomber","afldocker","aflfreo","aflfremantle","fremantlefootballclub","fremantlefc","fremantle_fc","gofremantle","gofreo","fremantleftw","fremantlesuck","fremantlerule","freosftw","freossuck","freosrule","dockersftw","dockersrule","dockerssuck","godockers","dockers","afldon","aflbomber","aflessendon","essendonfootball","essendonfc","essendon_fc","goessendon","gobombers","godons","essendonftw","bombersftw","donsftw","essendonrule","bombersrule","donsrule","bomberssuck","donssuck","essendonsuck","thedons","thebombers"]
carltonvsbrisbane = ["aflBluesLion","afllionsblue","afllionblue","aflbluelion", "aflblues","aflcarlton","carltonfootball","carltonblues","carltonfc","carlton_fc","gocarlton","carltonftw","carltonsuck","carltonrule","goblues","bluessuck","afllions","aflbrisbane","brisbanefc","brisbanefootball","brisbane_fc","thelions","brisbanelions","brisbaneftw","brisbanerule","lionsftw","lionsrule","golions","gobrisbane","lionssuck","brisbanesuck"]
portadelaidevswestcoast = ["aflporteagle","afleaglesport","afleagleport","aflportseagle","aflpowerseagle","afleaglespower","aflpowereagle","afleaglepower","aflportadelaide","aflport", "aflpower","portadelaidefootball","portadelaidefc","portadelaide_fc","goportadelaide","gopower","portadelaideftw","powersftw","portadelaiderule","powersrule","portadelaidesuck","powerssuck","westcoastfootball","westcoastfc","westcoast_fc","afleagles","aflwestcoast","westcoasteagles","goeagles","gowestcoast","eaglesftw","westcoastftw","westcoastrule","eaglesrule","eaglessuck","westcoastsuck" ]


#round7
essendonvsnorthmelb = ["aflkangaroosdons","afldonskanga","aflbomberskanga","aflkangaroobomber","aflnorthdon","aflnorthbomber","aflbomber","aflkanga","aflnorth","northmelbournefootball","northmelbournefc","northmelbourne_fc","gonorthmelbourne","northftw","northsuck",'northrule',"northmelbourneftw","northmelbournerule","northmelbornesuck","thekangaroos","gokangaroo","kangaroosftw","kangas","kangaroosrule","kangaroossuck","afldon","aflbomber","aflessendon","essendonfootball","essendonfc","essendon_fc","goessendon","gobombers","godons","essendonftw","bombersftw","donsftw","essendonrule","bombersrule","donsrule","bomberssuck","donssuck","essendonsuck","thedons","thebombers"]
adelaidevsstkilda = ["aflcrowssaints","aflsaintscrows","aflcrowsaint","aflsaintcrow","afladelaide","aflcrow","adelaidefootball","adelaidefc","adelaide_fc","goadelaide","gocrow","adelaideftw","crowsftw","adelaiderule","crowsrule","adelaidesuck","crowssuck","stkildafc","stkilda_fc","stkildafootball","stkildafootball","aflstkilda","aflkilda","aflsaint","aflthesaints","gostkilda","gosaints","gokilda","stkildaftw","saintsftw","saintsrule","kildarule","kildasuck","saintssuck","thesaints"]
hawthornvsmelbourne = ["aflhawksdee","aflhawksdemon","afldemonhawk","afldeehawk","afldeeshawk","afldemonshawk","aflhawkdee","aflhawkdemon","afldemon","afldee","melbournefootball","melbournefc","melbourne_fc","godemon","godee","demonsftw","deesftw","deessuck","deesrule","demonssuck","thedemons","aflhawthorn","aflhawk","aflhawks","hawthornhawks","hawthornfootball","hawthornfc","hawthorn_fc","gohawks","gohawthorn","hawksftw","thehawks","hawthornftw","hawksrule","hawthornrule","hawthornsuck","hawkssuck"]
carltonvsgwsgiants = ["aflbluegiant","aflbluesgiant","aflgaintblue","aflgiantsblue","aflgiant","aflblue","aflcarlton","carltonfootball","carltonblues","carltonfc","carlton_fc","gocarlton","carltonftw","carltonsuck","carltonrule","goblues","bluessuck","aflgiant","giantsfc","gws_fc","gwsfc","giants_fc","aflgwsgiant","gwsgiant","thegiants","greaterwesternsydney","gogiants","gogwsgiants","giantsftw","giantsrule","gwsrule","giantssuck","gwssuck","aflgws"]
sydneyvsgeelong = ["aflswanscats","aflcatsswans","aflcatswan","aflswancat","aflcat","aflswan","sydneyswans","theswans","swansrule","swanssuck","aflsydneyswans","goswans","sydneyswansftw","swansftw","aflcats","aflgeelong","geelongfootball","geelongfc","geelong_fc","geelongcats","gogeelong","geelongsuck","geelongrule","thecats","gocats","catssuck"]
westcoastvsgoldcoast = ["aflsunseagle","aflsuneagle","afleaglessun","afleaglesun","afleagle","aflsun","aflgoldcoast","goldcoastfootball","goldcoastfc","goldcoast_fc","thesuns","sunssuck","goldcoastsuck","gosuns","sunsrule","gogoldcoast","goldcoastrule","sunsftw","goldcoastftw","westcoastfootball","westcoastfc","westcoast_fc","afleagles","aflwestcoast","westcoasteagles","goeagles","gowestcoast","eaglesftw","westcoastftw","westcoastrule","eaglesrule","eaglessuck","westcoastsuck"]
westernbulldogvsfremantle = ["afldogsfreo","afldogfreo","afldogsdocker","afldogdocker","afldockerdog","afldockersdog","aflfreodog","aflfreosdog","afldog","afldocker","aflfreo","aflfremantle","fremantlefootballclub","fremantlefc","fremantle_fc","gofremantle","gofreo","fremantleftw","fremantlesuck","fremantlerule","freosftw","freossuck","freosrule","dockersftw","dockersrule","dockerssuck","godockers","dockers","afldogs","aflbulldogs","aflwesternbulldogs","footscrayfootball","westernbulldogs","footscrayfc","footscray_fc","gofootscray","gowesternbulldogs","gobulldogs","bulldogsftw","footscrayftw","westernbulldogsftw","westernbulldogsrule","bulldogsrule","bulldogssuck"]
richmondvscollingwood = ["afltigerpie","afltigerspie","aflpietiger",'aflpiestiger',"collingwood_fc","collingwoodfc","aflpies","aflmagpies","aflcollingwood","collingwoodfootball","collingwoodpies","gocollingwood","collingwoodsuck","piessuck","gopies","piesftw","piesrule","thepies","afltigers","aflrichmond","richmondfootball","richmondtigers","richmondfc","richmond_fc","gorichmond","richmondftw","richmondsuck","richmondrule","tigerssuck","tigersftw","tigersrule","thetigers"]
brisbanevsportadelaide = ["afllionpower","afllionspower","aflpowerlion","aflpowerslion","afllion","aflportadelaide","aflport", "aflpower","portadelaidefootball","portadelaidefc","portadelaide_fc","goportadelaide","gopower","portadelaideftw","powersftw","portadelaiderule","powersrule","portadelaidesuck","powerssuck","afllions","aflbrisbane","brisbanefc","brisbanefootball","brisbane_fc","thelions","brisbanelions","brisbaneftw","brisbanerule","lionsftw","lionsrule","golions","gobrisbane","lionssuck","brisbanesuck" ]

#round8
#round9
#round10
fremantlevsrichmond =[ "aflfreotiger","aflfreostigers","afldockerstigers","afltigerfreo","afltigersfreos","afltigersdockers","afldocker","aflfreo","aflfremantle","fremantlefootballclub","fremantlefc","fremantle_fc","gofremantle","gofreo","fremantleftw","fremantlesuck","fremantlerule","freosftw","freossuck","freosrule","dockersftw","dockersrule","dockerssuck","godockers","dockers","afltigers","aflrichmond","richmondfootball","richmondtigers","richmondfc","richmond_fc","gorichmond","richmondftw","richmondsuck","richmondrule","tigerssuck","tigersftw","tigersrule","thetigers"]

couch = couchdb.Server()
couch = couchdb.Server('http://127.0.0.1:5984/')
db = couch['tweetsdb']

auth = OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)
api = tweepy.API(auth,wait_on_rate_limit=True)
features = []
maxTweets = 10000000 
tweetsPerQry =100
plist=[]
fplist =[]

sinceId = None
max_id = -1L

tweetCount = 4992
count = 0 
check =0;
maxval = -1L

def combos(S,n):
    if (n <= 0): return
    for s in S:
        if len(s) <= n: yield s
        yield "#"+s

def playerlist(list1,n):
    if(n<=4): return
    for l in list1:
        if len(l) <= n: yield l
        yield "#"+l

brisbanevsportadelaide1 = []            
for x in combos(brisbanevsportadelaide,1000000): 
    brisbanevsportadelaide1.append(x)



for u in playerlist(brisblionspl,100000):
    plist.append(u)

for u in playerlist(portadelaidepl,100000):
    plist.append(u)    
    

    
print brisbanevsportadelaide1     

rtcount1 =0
rtcount2 =0
fcount1 =0
fcount2 =0
maxhcount = 100    
winteam1 =0
winteam2 =0
ftag = []
flist = []
worthy =0
playerrec =[]
maxrt1 = 0
maxrt2 = 0
mostrt1 =""
mostrt2 =""
for k in plist:
    i =0
    playerrec.append(i)

print playerrec
    
while tweetCount < maxTweets: 
    #results =  tweepy.Cursor(api.search,q=word,rpp=100,result_type="mixed",since_id=sinceid,include_entities=True,lang="en",geocode = "-37.814251,144.963165,30000mi").items()
     
    for word in brisbanevsportadelaide1:
        searchQuery = word
        print word
        hcount =0
        recent=""
        
        try:
            if (max_id <= 0):
                if (not sinceId):
                    new_tweets =tweepy.Cursor(api.search,q=word,count=tweetsPerQry,lang="en").items()
                else:
                    new_tweets = tweepy.Cursor(api.search,q=word,count=tweetsPerQry,since_id=sinceId,lang="en").items()
            else:
                if (not sinceId):
                    new_tweets = tweepy.Cursor(api.search,q=word,count=tweetsPerQry,max_id=str(max_id-1),lang="en").items()
                else:
                    new_tweets = tweepy.Cursor(api.search,q=word,count=tweetsPerQry,max_id=str(max_id-1),since_id=sinceId,lang="en").items()
            if not new_tweets:
                print("No more tweets found")
                break
            count =0
            for tweet in new_tweets:
                try:
                        
                    json_tweet = json.dumps(tweet._json)
                        
                    json_val = json.loads(json_tweet)
                    #if check==0:
                    #    maxval = json_val["id"]
                    #    check=-1
                    date = str(json_val["created_at"])
                    #(("May 09" in date) or ("May 10" in date) or ("May 11" in date))
                    if(("May 14" in date) or ("May 15" in date) or ("May 16" in date) or ("May 17" in date)):
                        text = json_val["text"]
                        rtcount = json_val["retweet_count"]
                        _id = str(json_val["id"]).encode('utf-8').strip()
                        
                        i=0
                        for w in plist:
                            
                            if(text.find(w)>=0):
                                playerrec[i]=playerrec[i]+1
                                #print playerrec
                                if(playerrec[i]>200):
                                    if(w not in fplist):
                                        fplist.append(w)
                            i = i+1
                            
                        if(hcount>500):
                            if(word not in flist):
                                flist.append(word)
    
                        
                        hcount = hcount +1
                        if(maxhcount<hcount and recent != word):
                            maxhcount = hcount
                            recent = word
                            ftag.append(word)
                            print ftag
                        
                        #(text.find("adelaide")>=0) or (text.find("crow")>=0)
                        #(text.find("port")>=0) or (text.find("power")>=0)        
                        #((word.find("western")>=0) or (word.find("giant")>=0) or(word.find("gws")>=0))    
                        #((word.find("hawthorn")>=0)or (text.find("hawk")>=0))
                        #(word.find("gold")>=0)or (text.find("sun")>=0)
                        #(text.find("sydney")>=0) or (text.find("swan")>=0)
                        #(text.find("melb")>=0) or (text.find("demon")>=0)or (text.find("dee")>=0)
                        #(text.find("fremantle")>=0) or (text.find("freo")>=0)or (text.find("docker")>=0)
                        #(text.find("essendon")>=0) or (text.find("don")>=0)or (text.find("bomber")>=0)
                        #(text.find("brisbane")>=0) or (text.find("lion")>=0)
                        #(text.find("carlton")>=0) or (text.find("blue")>=0)
                        #(text.find("west")>=0) or (text.find("eagle")>=0)
                        #(text.find("north")>=0) or (text.find("kanga")>=0)
                        #(text.find("kilda")>=0) or (text.find("saint")>=0)
                        #(text.find("richmond")>=0) or (text.find("tiger")>=0)
                        
                        if((text.find("brisbane")>=0) or (text.find("lion")>=0)):
                            if((text.find("brisbane")>=0) or (text.find("lion")>=0)):
                                if(rtcount>maxrt1):
                                    maxrt1 = rtcount1
                                    mostrt1 = _id
                                rtcount1 = rtcount1 +rtcount
                                fcount1 = fcount1 + 1
                                if(text.find("win")>=0):
                                    winteam1 = winteam1+1
                                if(text.find("cong")>=0):
                                    winteam1 = winteam1+1  
                                if(text.find("lead")>=0):
                                    winteam1 = winteam1+1        
                        if((text.find("port")>=0) or (text.find("power")>=0) )    :
                            if((text.find("port")>=0) or (text.find("power")>=0) )    :
                                if(rtcount>maxrt2):
                                    maxrt2 = rtcount2
                                    mostrt2 = _id
                                rtcount2 =rtcount2+rtcount
                                fcount2 = fcount2 + 1    
                                if(text.find("win")>=0):
                                    winteam2 = winteam2 + 1
                                if(text.find("cong")>=0):
                                    winteam2 = winteam2+1
                                if(text.find("lead")>=0):
                                    winteam2 = winteam2+1
                                        
                        screen_name = (json_val["user"]["screen_name"]).encode('utf-8').strip()
                        
                        user_id = str(json_val["user"]["id"]).encode('utf-8').strip()
                        geo = str(json_val["geo"]).encode('utf-8').strip()
                        coordinates = str(json_val["coordinates"]).encode('utf-8').strip()
                        user_location = (json_val["user"]["location"]).encode('utf-8').strip()
                        place_tweet = str(json_val["place"]).encode('utf-8').strip()
                        user_description = (json_val["user"]["description"]).encode('utf-8').strip()
                                
                        #doc = {"_id":_id,"date":date,"user_id":user_id,"screen_name":screen_name,"tweet_text":text,"geo":geo,"coordinates":coordinates,"tweet_location":place_tweet,"user_location":user_location,"user_description":user_description}
                        json_val['doc_type'] = "tweet"
     
                        db["tweet:%d" % json_val['id']] = json_val
                        #db.save(doc)
                        tweetData = open('brisbanevsportadelaideTweets.csv','a')
                        tweet_details = str(_id)+":::"+str(date)+":::"+((text).encode('utf-8').strip())+":::"+str(geo)
                        print tweet_details
                        tweetData.write(tweet_details)
                        tweetData.write('\n')
                        tweetData.close()
                        
                        #tweetData = open('TweetsDB.csv','a')
                        #tweet_details = str(_id)+":::"+str(date)+":::"+((text).encode('utf-8').strip())+":::"+str(geo)
                        #print tweet_details
                        #tweetData.write(tweet_details)
                        #tweetData.write('\n')
                        #tweetData.close()
                        
                        count = count+1
                        
                         
                except tweepy.TweepError as e:
                    time.sleep(60*15)
                except couchdb.http.ResourceConflict:
                    print"SKIPPING DUPLICATE"    
            
            tweetCount = tweetCount + count
            print("Downloaded tweets:"+str(tweetCount))
            max_id = -1L
            if(tweetCount>2000):
                
                tweetstats = open('STATS_round7.csv','a')
                
                if((rtcount1-savert1 > 200) or (rtcount2-savert2 >200) or (fcount1-savefc1 >200) or (fcount2-savefc2 > 200) or (winteam1-savewt1 >30) or (winteam2-savewt2 >30) or saveft != str(ftag) or savefl != str(flist) or savemr1 != mostrt1 or savemr2 != mostrt2 or savefp != str(fplist)):
                    savert1 = rtcount1
                    savert2 = rtcount2
                    savefc1 = fcount1
                    savefc2 = fcount2
                    savewt1 = winteam1
                    savewt2 = winteam2
                    saveft = str(ftag)
                    savefl = str(flist)
                    savemr1 = mostrt1
                    savemr2 = mostrt2
                    savefp = str(fplist)
                    #print(str(get_indentifier_name_missing_function(collingwoodvscarlton)))
                    tweetstats.write('brisbane vs portadelaide')
                    
                    
                    tweetstats.write('\n')
                    tweetstats.write(str(tweetCount))
                    tweetstats.write('\n')
                    stats1 = "ftag:::"+str(ftag)
                    tweetstats.write(stats1)
                    tweetstats.write('\n')
                    stats2 = "rtcount1:::"+str(rtcount1)+"rtcount2:::"+str(rtcount2)+"fcount1:::"+str(fcount1)+"fcount2:::"+str(fcount2)+"wteam1:::"+str(winteam1)+"wteam2:::"+str(winteam2)
                    tweetstats.write(stats2)
                    tweetstats.write('\n')
                    stats3 ="flist:::"+str(flist)
                    tweetstats.write(stats3)
                    tweetstats.write('\n')
                    stats4 = "fplist:::"+str(fplist)
                    tweetstats.write(stats4)
                    tweetstats.write('\n')
                    stats5 = "mostrt1:::"+str(mostrt1)+"  mostrt2:::"+str(mostrt2)
                    tweetstats.write(stats5)
                    tweetstats.write('\n')
                    tweetstats.write(str(playerrec))
                    tweetstats.write('\n\n\n')
                    
                    tweetstats.close()
            
            continue
        
            
                            
        except tweepy.TweepError as e:
            time.sleep(60*15)
        except StopIteration:
            break   
        
