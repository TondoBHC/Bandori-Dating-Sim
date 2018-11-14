# The script of the game goes in this file.

init python:
    def max_points(*values):
        return [ i for i, v in enumerate(values) if v == max(values) ]

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define e = Character("Eileen")

define principal = Character("Principal")
define fullName = Character("[first_name] [last_name]")
define mom = Character("Mom")
$ user = None

define k = Character("Kaoru")
define t = Character("Tomoe")
define h = Character("Hina")
define s = Character("Sayo")
define a = Character("Arisa")
define ta = Character("Tae")

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

# The game starts here.

label start:
    stop music
    play music "music/introScreen.mp3"
    show screen ui_top_buttons
    menu:
        "Which pronouns do you prefer using?"

        "They/Them":
            $ pronoun = theyThem

        "He/Him":
            $ pronoun = heHim

        "She/Her":
            $ pronoun = sheHer
    label nameplayer:
        "What name would you like to go by?"
        $ first_name = renpy.input("First name")
        $ first_name = first_name.strip()
        $ last_name = renpy.input("Last name")
        $ last_name = last_name.strip()
        if (first_name == (("Jonathan") or ("Joseph") or ("Johnny")) and last_name == ("Joestar")) or (first_name == ("Jotaro") and last_name == ("Kujo")) or (first_name == ("Josuke") and last_name == ("Higashikata")) or (first_name == ("Jolyne") and last_name == ("Cujoh")):
            $ user = ("JoJo")
        elif first_name == ("Giorno") and last_name == ("Giovanna"):
            $ user = ("GioGio")
        else:
            $ user = Character("[first_name]")
        "So [fullName], is that right?"    
        menu:
            "Yes, [fullName]":
                pass
            "No":
                "Well then, enter the correct one."
                call nameplayer
    
    ## To use the pronoun variable they have to be incased in brackets[], friendly reminder that arrays start from 0.
    stop music
    play music "music/firstDayMorning.mp3"
    scene mc bedroom with fade
    pause 5.0
    stop music
    play music "music/8AM.mp3"
    "Oh boy, my first day at my new school! I can\'t wait to see what it has in store for me!"
    "I\'ll probably get to meet all sorts of cool people and make a bunch of new friends. Although..."
    "I do miss my old ones, but they did say our friendship was over until I made at least 3 new friends so it\'s do or die."
    "I wonder what type of people go there. Maybe some cool rocker punks, or maybe some pure cinnamon buns, or maybe..."
    mom "Honey it\'s already 8 o\'clock, you don\'t want to be late on your first day, do you?"
    "WHAT!? Oh shit, it is already 8! This is bad, I better hurry the fuck up or I\'ll make a bad first impression."
    user "Coming!"
    stop music
    play music "music/Finder_Prism_and_Lens.mp3"
    scene school front outside with fade
    "Phew! Just made it, and with 2 minutes to spare."
    if pronoun == theyThem:
        principal "Ah, there [pronoun[4]] are, the new student. Just in time."
    else:
        principal "Ah, there [pronoun[4]] is, the new student. Just in time."
    scene bg staff room with fade
    principal "I must say, it is quite odd to have a new transfer student at this time of the school year, but don't let that bring you down! I'm sure you'll make friends quickly!"
    principal "Now let\'s see here, [fullName]? Well that\'s a pretty nice name, you\'re already on a roll!"
    "Yeah, if you ignore the fact I was almost late on my first day."
    if (user == (("JoJo") or ("GioGio"))):
        user "Oh, btw, people tend to call me [user], feel free to call me that too."
        principal "Alright then, [user] it is!"
    else:
        pass
    principal "Okay, so... according to this, you transfered to our school via a student exchange program, you had a lot of choices, yet you still chosen us! What made you choose this school?"
    menu:
        "What made you choose this school?"
        "My mother attended Hanasakigawa when she was a student.":
            jump fd_hanasakigawa
        "I like the study program Haneoka offers.":
            jump fd_haneoka
return

label fd_hanasakigawa: # First day at Hanasakigawa (Tae, Arisa, Sayo)
    principal "Oh [user], such a deep reason! Surely Hanasakigawa is a school with many loving memories from past generations!"
    "Hopefully I\'ll get to make some loving memories of my own."
    principal "Now then, let me get some paperwork sorted out and you can be on your way."
    user "Is it okay if I explore the school a bit, to familiarize myself with it that is."
    principal "Actually, we have a volunteer student who\'s very excited to show you around the school, hopefully, she could be your first friend."
    principal "Her name is Sayo Hikawa, and she should be arriving here any moment now."
    s "Excuse me, sorry for being late, I was caught up doing some work."
    principal "Oh don\'t worry about that, I was just telling [user] here about you."
    s "I see, [user] is it?"
    user "Ah yes, I\'m [fullName]. It\'s a pleasure to meet you."
    principal "Marvelous, I can tell you two are going to be great friends!"
    principal "Now then, [s], why don\'t you take [user] on a tour of the school while I finish up some work of my own."
    s "Of course, [last_name], after you."
    "We step outside of the teachers lounge and into the empty hallway, pressumably because everyone is in class."
    "For a, not-so-brief, moment we stare each other down like lions in a pit."
    s "..."
    user "..."
    s "Did you even bother to try and look decent for a new school? All your buttons are done up the wrong way."
    s "Will you excuse yourself as to look presentable, or shall I redo them for you?"
    menu:
        "Wha... I didn\'t notice, I-I\'ll be right back.":
            jump herbivore
        "I dare you to.":
            jump carnivore
        "...":
            jump passive

    label herbivore: # You redo your buttons yourself
        "I do them up again, this time, hopefully, correct. My reflection has four buttons, two on each side."
        "As I leave the washroom, I see [s] waiting for me outside, the expression on her face is an interesting mix of contempt and amusement."
        s "The writers have yet to write what goes after, I\'m afraid you can\'t progress any further."
    return

    label carnivore:
        s "You\'re insufferable, the washroom is down the corridor. Go on now."
        "And so off I went."
        "Hmm, it seems the writers have yet to write what goes after, I\'m sure they\'re working hard writing the script. For now I\'ll go to the main menu."
    return

    label passive:
        "¯\\_(^^)_/¯"
    return
    
return

label fd_haneoka: # First day at Haneoka (Kaoru, Tomoe, Hina)
    principal "How diligent of you, [user]! We are proud of our students here in Haneoka, I trust you'll excel in all your classes."
    "I sure hope so."
    return



# label points:
#     $ k_points = 0
#     $ t_points = 0
#     $ h_points = 0
#     # $ persistent.bond = 'Random' # reload persistent
#     scene bg room
#     show eileen happy
#     e "testing to define main menu bg UI, based on player's choices"
#     e "first choice"
#     call bondmenu
#     e "second choice"
#     call bondmenu
#     e "third choice"
#     call bondmenu
#     e "points so far are: \n Kaoru: [k_points] \n Tomoe: [t_points] \n Hina: [h_points]"
#     e "max bond value is: [max_bond]"
#     e "persistent value is: [persistent.bond]"
#     e "save now"
#     return
#
# label bondmenu:
#     menu:
#         "Who do you want tho bond to?"
#         "Bond with Kaoru":
#             $ k_points += 1
#             k "Thank you little kitten"
#             call high_points
#         "Bond with Tomoe":
#             $ t_points += 1
#             t "Oh! Nice! thanks!"
#             call high_points
#         "Bond with Hina":
#             $ h_points += 1
#             h "Boopin!"
#             call high_points
# return



# label high_points:
#     $ max_bond = max_points(k_points, t_points, h_points)
#     if max_bond == [0]:             # Kaoru
#         $ persistent.bond = 'Kaoru'
#     elif max_bond == [1]:           # Tomoe
#         $ persistent.bond = 'Tomoe'
#     elif max_bond == [2]:           # Hina
#         $ persistent.bond = 'Hina'
#     else:                           # Neither
#         $ persistent.bond = 'Random'
#     $ renpy.save_persistent()
# return
