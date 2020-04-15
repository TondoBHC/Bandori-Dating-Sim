
init:
    ## position variables for showing images
    $ l = Position(xpos=0.35)#show at left
    $ r = Position(xpos=0.65)#show at right


init python:
    ## a list that will store all the gifts,convov1s,dates,guests in game -
    #will adjust length based on the instances of each object automatically

    gifts = [ ]
    convos = []
    dates = [ ]
    guests = [ ]

    ##object variables - gift, inventory, convov1, dates, guests

    #the gift object
    class gift(object):
        def __init__(self,name,cost,desc,guest,image):
            #properties
            self.name=name
            self.cost=cost
            self.desc=desc#22 characters max per each desc - 11 characters per para
            #(2 paras max) - see sample define
            self.guest=guest #is this gift for guests or not?
            self.image=image
            self.ID=len(gifts)+1
            #line to add this object to the gifts
            gifts.append(self)

    #the inventory object - will control purchasing,
    #storing, etc. but is mainly temp right now - still need to change a few thingys
    class Inventory(object):
        def __init__(self,money):
            self.money=money
            self.gift= [ ]#gift object as subclass
        def buy(self, item):
            if self.money >= item.cost:
                self.gift.append(item)
                self.money -= item.cost


    #the convo object - new variable adjustment from meeting on 09/02/20
    class convo(object):
        def __init__(self,topic,level,rarity):
            self.topic=topic#the name of the toppic
            self.level=level#the level of knowledge the player has on the topic
            self.rarity=rarity#at what stage in the game do you unlock this topic - is it early (making it the lowest rarity, 0) or later on (>0)?
            self.ID=len(convos)+1#used to identify item via a number - this is so that it can be
            convos.append(self)

    #the guest object
    class guest(object):
        def __init__(self,desc,timesVisited,convoPref=[],giftPref=[]):
            self.desc=desc
            self.timesVisited =timesVisited #how many times has the guest come?
            self.convoPref=convoPref
            self.giftPref=giftPref
            self.ID=len(guests)+1
            guests.append(self)

    #the date object - for storing dating options prefs and bp
    class date(object):
        def __init__(self,name,bp,datesDone,giftCounter,convoCounter=[],convoPref=[],giftTrash=[],giftGood=[],giftSpecial=[]):
            self.name=name
            self.bp=bp
            self.datesDone=datesDone#the number of dates the player has done with this girl
            self.giftCounter=giftCounter#the number of gifts the player has given to the girl in a week (resets every new week)
            self.convoCounter=convoCounter#if a topic has been talked about with the girl in a week(resets every new week)
            self.convoPref=convoPref#unlike guests, convov1 and gift prefs always need passed in
            self.giftTrash=giftTrash#what gifts are trash
            self.giftGood=giftGood#what gifts are good
            self.giftSpecial=giftSpecial#what gifts are special
            self.ID=len(dates)+1#ID for date
            dates.append(self)


    ##object define (samples included)
    #samples
    #gift define sample
    giftsample1 = gift("Strawberry Shortcake",1,"eeeeeeeeeee{p}eeeeeeeeeee",True,"gui/gifts/cake.png")#goes name,price,desc,guest,image
    giftsample2 = gift("Earl Grey",1,"eeeeeeeeeee{p}eeeeeeeeeee",True,"gui/gifts/tea.png")
    giftsample3 = gift("Green tea",1,"eeeeeeeeeee{p}eeeeeeeeeee",True,"gui/gifts/tea2.png")
    giftsample4 = gift("Jello",1,"eeeeeeeeeee{p}eeeeeeeeeee",True,"gui/inv.png")
    giftsample5 = gift("Gift 5",1,"eeeeeeeeeee{p}eeeeeeeeeee",False,"gui/inv.png")


    #convov2 sample define
    convosample0 = convo("Animals",0,0)
    convosample1 = convo("Topic 2",0,0)
    convosample2 = convo("Topic 3",0,0)
    convosample3 = convo("Topic 4",0,0)
    convosample4 = convo("Topic 5",0,0)
    convosample5 = convo("Topic 6",0,0)

    #guest define sample
    guest("Desc",0,[1,2,3],[1,2,3])#if you wish, you can just pass in
    #the first two paramaters for randomly assigned interests


    #real defines
    #date defines
    kStats=date("Kaoru",0,0,0,[],[0,0,0],[0,0,0],[0,0,0],[0,0,0])#this is for kaoru - id1
    hStats=date("Hina",0,0,0,[],[0,0,0],[0,0,0])#hina - id2
    tStats=date("Tomoe",0,0,0,[],[0,0,0],[0,0,0])#tomoe - id3
    sStats=date("Sayo",0,0,0,[],[0,0,0],[0,0,0])#sayo - id4
    taStats=date("Tae",0,0,0,[],[0,0,0],[0,0,0])#tae - id5
    aStats=date("Arisa",0,0,0,[],[0,0,0],[0,0,0])#arisa - id6
    hiStats=date("Himari",0,0,0,[],[0,0,0],[0,0,0],[0,0,0],[0,0,0])#himari - id7


    #inventory define
    inventory = Inventory(10)


#persistent variables
$ persistent.candy = int(0)
$ persistent.completedTimes = int(0)


#character define
#mc
define fullName = Character("[first_name] [last_name]")
$ persistent.playerName = "[first_name] [last_name]" # used for intro
$ user = None
define hostPoints = 0
define studyPoints = 0
define schoolPoints = 0
define resumeGiven = False
define dateOrganised = False #date organised for week?
#side
define principal = Character("Principal")
define mom = Character("Mom")
define ga = Character ("Girl A")
define gb = Character ("Girl B")
define unk = Character ("???")
define ka = Character("Kasumi")
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
define a = Character("Arisa")
define ta = Character("Tae")
define hi = Character("Himari")
#guests
define y = Character("Yukina")


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
