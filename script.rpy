# The script of the game goes in this file.

init python:
    def max_points(*values):
        return [ i for i, v in enumerate(values) if v == max(values) ]

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define e = Character("Eileen")

define teacher = Character("Teacher")
define me = Character("[first_name] [last_name]")
define mom = Character("Mom")

define k = Character("Kaoru")
define t = Character("Tomoe")
define h = Character("Hina")

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
        "So [first_name] [last_name], is that right?"
        menu:
            "Yes, [first_name] [last_name]":
                pass
            "No":
                "Well then, enter the correct one."
                call nameplayer
    ## To use the pronoun variable they have to be incased in brackets[], friendly reminder that arrays start from 0.
    play music "music/firstDayMorning.mp3"
    scene mc bedroom with fade
    pause 5.0
    stop music
    play music "music/8AM.mp3"
    "Oh boy, my first day at my new school! I can\'t wait to see what it has in store for me!"
    "I\'ll probably get to meet all sorts of cool people and make a bunch of new friends. Although..."
    "I do miss my old ones, but they did say our friendship was over until I made at least 3 new friends so it\'s do or die."
    "I wonder what type of people go there. Maybe some cool rocker punks, or maybe some pure cinnamon buns, or maybe..."
    mom "Honey it\'t already 8 o\'clock, you don\'t want to be late on your first day, do you?"
    "WHAT!? Oh shit, it is already 8! This is bad, I better hurry the fuck up or I\'ll make a bad first impression."
    me "Coming!"
    stop music
    play music "music/Finder_Prism_and_Lens.mp3"
    scene school front outside with fade
    "Phew! Just made it, and with 2 minutes to spare."
    if pronoun == theyThem:
        teacher "Ah, there [pronoun[4]] are, the new student. Just in time."
    else:
        teacher "Ah, there [pronoun[4]] is, the new student. Just in time."
    scene bg staff room with fade
    teacher "I must say, it is quite odd to have a new transfer student at this time of the school year, but don't let that bring you down! I'm sure you'll make friends quickly!"
    teacher "Now let\'s see here, [first_name] [last_name]? Well that\'s a pretty nice name, you\'re already on a roll!"
    "Yeah, if you ignore the fact I was almost late on my first day."
    teacher "Okay, so... according to this, you transfered to our school via a student exchange program, you had a lot of choices, yet you still chosen us! What made you choose this school?"
    menu:
        "What made you choose this school?"
        "My mother attended Hanasakigawa when she was a student.":
            jump fd_hanasakigawa
        "I like the study program Haneoka offers.":
            jump fd_haneoka
return

label fd_hanasakigawa: # First day at Hanasakigawa (Tae, Arisa, Sayo)
    teacher "Oh [first_name], such a deep reason! Surely Hanasakigawa is a school with many loving memories from past generations!"
    "Hopefully I\'ll get to make some loving memories of my own."
    return

label fd_haneoka: # First day at Haneoka (Kaoru, Tomoe, Hina)
    teacher "How diligent of you, [first_name]! We are proud of our students here in Haneoka, I trust you'll excel in all your classes."
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
