
# Declare characters used by this game. The color argument colorizes the
# name of the character.
init python:
    class player(object):
        def __init__(self,host,grade,gold):
            self.host=host#host club quality
            self.grade=grade#school performance
            self.gold=gold#money
        def getHost(self):
            return self.host #to get value of host club performance
        def getGrade(self):
            return self.grade
        def getGold(self):
            return self.gold
        def increaseHost(self,x):
            self.host+= x #will increase value of host based on x
        def decreaseHost(self,x):
            self.host-= x #will decrease value of host based on x
        def changeGrade(self,x):
            self.grade==x #will change value of grade based on x
        def increaseGold(self,x):
            self.gold+=x
        def decreaseGold(self,x):
            self.gold-=x
    class date(object):
        def __init__(self,bp,date,heartbroken):
            self.bp=bp#bond points
            self.date=date#date number
            self.heartbroken=heartbroken#used to store if girl is heartbroken or not - might be moved out of class later
        def nextDate(self,x):
            #this will both change the date number and the bp needed for the next date
            #eg: player unlocks date 3. using this function after they unlock date 3 will increase the date number to 4 and increase the corresponding bp needed
            self.bp+=x
            self.date+=1
        def makeHeartbroken(self):
            #this will make a girl heartbroken. tried to make this persistent variable like wanted.
            self.heartbroken==True
            renpy.register_persistent('sadDoki', self.heartbroken)






define e = Character("Eileen")

define principal = Character("Principal")
define fullName = Character("[first_name] [last_name]")
define mom = Character("Mom")
$ user = None
define affection = 0

define k = Character("Kaoru")
define t = Character("Tomoe")
define h = Character("Hina")
define s = Character("Sayo")
define a = Character("Arisa", color="#800080")
define ta = Character("Tae")
define ka = Character("Kasumi", color="#ff0000")
define hi = Character("Himari", color="#FFA0B4")
define ga = Character ("Girl A")
define gb = Character ("Girl B")
define unk = Character ("???")

#additional guest character variables (cookie)

define gu = Character("Guest")
define gu1 = Character("Guest A")
define gu2 = Character("Guest B")
define gu3 = Character("Guest C")

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
