#making fade transistion shorter
init python:
    define.move_transitions("fade", 0.45)

init:
    ## position variables for showing images
    $ l = Position(xpos=0.35)#show at left
    $ r = Position(xpos=0.65)#show at right

init python:
    def max_points(*values):
        return [ i for i, v in enumerate(values) if v == max(values) ]

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
    giftsample1 = gift("Shortcake",1,"eeeeeeeeeee{p}eeeeeeeeeee",True,"gui/gifts/cake.png")#goes name,price,desc,guest,image
    giftsample2 = gift("Earl Grey",1,"eeeeeeeeeee{p}eeeeeeeeeee",True,"gui/gifts/tea.png")
    giftsample3 = gift("Green tea",1,"eeeeeeeeeee{p}eeeeeeeeeee",True,"gui/gifts/tea2.png")
    giftsample4 = gift("Jello",1,"eeeeeeeeeee{p}eeeeeeeeeee",True,"gui/inv.png")
    giftsample5 = gift("Gift 5",1,"eeeeeeeeeee{p}eeeeeeeeeee",False,"gui/inv.png")


    #convov2 sample define
    convosample0 = convo("Animals",0,0)
    convosample1 = convo("Music",0,0)
    convosample2 = convo("Bonsai",0,0)
    convosample3 = convo("Fashion Trends",0,0)
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

#time variables
default day = 1
default time = ["Morning", "Afternoon", "Evening", "Night"] # edit this list to rename, add or delete time of days
define end_of_day = "Night" # set this as the last time of day before new day begins
default month = 1
default months = ["Sep","Oct","Nov","Dec","Jan","Feb"]
default weekday = 1
default weekdays = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
default week = 1

#persistent variables
$ persistent.candy = int(0)
$ persistent.completedTimes = int(0)

#calender
define dateOrganised = False #date organised for week?
define testOn = False #test?

#character define
#mc + stats
define fullName = Character("[first_name] [last_name]")
$ persistent.playerName = "[first_name] [last_name]" # used for intro
$ user = None
define hostPoints = 0
define studyPoints = 0
define schoolPoints = 0
define resumeGiven = False
#side
define principal = Character("Principal")
define mom = Character("Mom")
define ga = Character ("Girl A")
define gb = Character ("Girl B")
define unk = Character ("???")
define ka = Character("Kasumi")
define ts = Character("Tsugumi")
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
## To use the pronoun variable they have to be incased in brackets[], friendly reminder that arrays start from 0.
define theyThem = ["They", "Them", "Their", "They\'re", "they", "them", "their", "they\'re"]
define heHim = ["He", "Him", "His", "He\'s", "he", "him", "his", "he\'s"]
define sheHer = ["She", "Her", "Her", "She\'s", "she", "her", "her", "she\'s"]
## Empty variable that will hold the array chosen later for ease of use when coding pronouns.
$ pronoun = None

##IMAGES
#CGs
image placeholder = "CGs/placeholder.png"

# Backgrounds
image class evening = "Backgrounds/classroom_color_evening.png"
image class day = "Backgrounds/classroom_color_morning.png"
image h bedroom evening = "Backgrounds/hina_bedroom_night.png"
image h bedroom day = "Backgrounds/hina_bedroom_day.png"
image park day = "Backgrounds/park_Day.png"
image park evening = "Backgrounds/park_Evening.png"
image rooftop = "Backgrounds/rooftop.png"

#Sprites
#arisa
image a angry = "Sprites/a_angry.png"
image a annoyed = "Sprites/a_annoyed.png"
image a crossed arms = "Sprites/a_crossed_arms.png"
image a default = "Sprites/a_default.png"
image a embarassed = "Sprites/a_embarassed.png"
image a happy = "Sprites/a_happy.png"
image a sweats = "Sprites/a_sweats.png"
image a inactive = "Sprites/a_inactive.png"
#hina
image h angry = "Sprites/h_angry.png"
image h blush1 = "Sprites/h_blush1.png"
image h blush2 = "Sprites/h_blush2.png"
image h default = "Sprites/h_default.png"
image h sad = "Sprites/h_sad.png"
image h inactive = "Sprites/h_inactive.png"
#sayo
image s angry1 = "Sprites/s_angry1.png"
image s angry2 = "Sprites/s_angry2.png"
image s angry3 = "Sprites/s_angry3.png"
image s blush = "Sprites/s_blush.png"
image s default1 = "Sprites/s_default1.png"
image s default2 = "Sprites/s_default2.png"
image s happy1 = "Sprites/s_happy1.png"
image s happy2 = "Sprites/s_happy2.png"
image s inactive = "Sprites/s_inactive.png"
#tsugumi
image ts default = "Sprites/ts_default.png"
image ts happy = "Sprites/ts_happy.png"
image ts inactive = "Sprites/ts_inactive.png"
#yukina
image y blush = "Sprites/y_blush.png"
image y default = "Sprites/y_default.png"
image y inactive = "Sprites/y_inactive.png"
