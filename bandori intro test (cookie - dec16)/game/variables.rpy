
init python:
    ## a list that will store all the gifts,convos,dates,guests in game -
    #will adjust length based on the instances of each object automatically

    gifts = [ ]
    convos = [ ]
    dates = [ ]
    guests = [ ]

    ##object variables - gift, inventory, convo, dates, guests

    #the gift object
    class gift(object):
        def __init__(self,name,cost,desc,image):
            #properties
            self.name=name
            self.cost=cost
            self.desc=desc#22 characters max per each desc - 11 characters per para
            #(2 paras max) - see sample define
            self.image=image
            self.ID=None#look at CONVO for ref when doing IDs
            #line to add this object to the gifts
            gifts.append(self)
        def setID(self):
            x = gifts.index(self)
            self.ID=x

    #the inventory object - will control purchasing,
    #storing, etc. but is mainly temp right now - still need to change a few thingys
    class Inventory(object):
        def __init__(self,money=10):
            self.money=money
            self.gift=[]#gift object as subclass
        def buy(self, item):
            if self.money >= item.cost:
                self.gift.append(item)
                self.money -= item.cost


    #the convo object - stores convo topics
    class convo(object):
        def __init__(self,topic):
            self.topic=topic#the name of the topic
            self.questions=[]#subclass where questions will be stored
            self.ID=None#used to identify item via a number - this is so that it can be
            #identified if a guest/girl likes a topic
            convos.append(self)
        def setID(self):
            x = convos.index(self)#returns the index of the value - this sets the autonumber for ID
            self.ID=x
        def addQ(self,q,options=[],correct=[]):
            self.questions.append(question(q,options,correct))
    class question(object):
        def __init__(self,question,options=[],correct=[]):
            self.question=question#the actual question
            self.options=options#the options
            self.correct=correct#is the option right or nah?
            #options and correct are stored as a set of 1d arrays and thus the
            # index of option should correspond with the index of correct when filling out
            #see sample define

    #the guest object
    class guest(object):
        def __init__(self,desc,image,convoPref=[],giftPref=[]):
            x = len(convos)
            self.desc=desc
            self.img=image #guest image - if we only have one guest sprites, this will suffice
            if convoPref is None:
                self.giftPref=[renpy.random.randint(1, x),renpy.random.randint(1, x),renpy.random.randint(1, x)]
                #three random convo topics for pref if none is set
            else:
                self.convoPref=convoPref
            if giftPref is None:
                self.giftPref=[renpy.random.randint(1, x),renpy.random.randint(1, x),renpy.random.randint(1, x)]
                #likewise
            else:
                self.giftPref=giftPref
            guests.append(self)

    #the date object - for storing dating options prefs and bp
    class date(object):
        def __init__(self,bp,convoPref=[],giftPref=[]):
            self.bp=bp
            self.convoPref=convoPref#unlike guests, convo and gift prefs always need passed in
            self.giftPref=giftPref
            dates.append(self)

    gifts = [ ]
    convos = [ ]
    dates = [ ]
    guests = [ ]

    ##object define (samples included)
    #samples
    #gift define sample
    giftsample = gift("Gift 1",1,"eeeeeeeeeee{p}eeeeeeeeeee","gui/inv.png")#goes name,price,desc,image
    giftsample.setID()
    #convo + question define sample
    convosample = convo("Topic 1")#add topic here
    convosample.setID()
    convosample.addQ("Question 1",["Answer 1","Answer 2","Answer 3"],[True,False,False])
    #when you want to add a question to a convo - use the sample above
    #the TRUE, FALSE, FALSE indicates the right answer (true) - it is a corresponding 1d array
    #to the answer paramaters

    #date define sample
    date(0,[1,2,3],[1,2,3])
    #guest define sample
    guest("Desc","images/guest.png",[1,2,3],[1,2,3])#if you wish, you can just pass in
    #the first two paramaters for randomly assigned interests


    #real defines
    #date defines
    kStats=date(0,[0,0,0],[0,0,0])#this is for kaoru
    hStats=date(0,[0,0,0],[0,0,0])#hina
    sStats=date(0,[0,0,0],[0,0,0])#sayo
    taStats=date(0,[0,0,0],[0,0,0])#tae
    aStats=date(0,[0,0,0],[0,0,0])#arisa
    hiStats=date(0,[0,0,0],[0,0,0])#himari
    tStats=date(0,[0,0,0],[0,0,0])#tomoe

    #inventory define
    inventory = Inventory()


#persistent variables
$ persistent.candy = int(0)
$ persistent.completedTimes = int(0)


#character define
#mc
define fullName = Character("[first_name] [last_name]")
$ persistent.playername = None
$ user = None
#side
define principal = Character("Principal")
define mom = Character("Mom")
define ga = Character ("Girl A")
define gb = Character ("Girl B")
define unk = Character ("???")
define ka = Character("Kasumi", color="#ff0000")
#additional guest character variables (cookie)
define gu = Character("Guest")
define gu1 = Character("Guest A")
define gu2 = Character("Guest B")
define gu3 = Character("Guest C")
#dates
define k = Character("Kaoru")
define t = Character("Tomoe")
define h = Character("Hina")
define s = Character("Sayo")
define a = Character("Arisa", color="#800080")
define ta = Character("Tae")
define hi = Character("Himari", color="#FFA0B4")



## Here I've created and defined 3 arrays holding the various
## conjugations of the main pronouns we are going to be using throughout the game.
define theyThem = ["They", "Them", "Their", "They\'re", "they", "them", "their", "they\'re"]
define heHim = ["He", "Him", "His", "He\'s", "he", "him", "his", "he\'s"]
define sheHer = ["She", "Her", "Her", "She\'s", "she", "her", "her", "she\'s"]
## Empty variable that will hold the array chosen later for ease of use when coding pronouns.
$ pronoun = None

# Backgrounds
image bg staff room = "backgrounds/bgStaffRoom.jpg"
image mc bedroom = "backgrounds/mcBedroom.jpg"
image school front outside = "backgrounds/schoolFrontOutside.jpg"
image back = "backgrounds/back.jpg"
