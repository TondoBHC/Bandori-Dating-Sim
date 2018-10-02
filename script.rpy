# The script of the game goes in this file.

init python:
    def max_points(*values):
        return [ i for i, v in enumerate(values) if v == max(values) ]

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define e = Character("Eileen")

define teacher = Character("Teacher")
define me = Character("[first_name] [last_name]")

define k = Character("Kaoru")
define t = Character("Tomoe")
define h = Character("Hina")

# Backgrounds
image bg staff room = "backgrounds/bg_staff-room.jpg"

# The game starts here.

label start:
    show screen ui_top_buttons
    ". . . . ."
    pause .5
    "Sorry to make you wait, things are hectic after summer vacation, but all the student are still so lively. However, us teachers have to assure they behave properly."
    "It's not vacation forever after all, they need to focus on their studies too!"
    "Well... maybe I'm saying that to myself too, hehe..."
    ". . . . ."
    "Huh? And here I thought that would've made you smile a little! Geez, now I look lame!"
    play music "music/Finder_Prism_and_Lens.mp3"
    #scene bg staff room with fade
    teacher "But seriously, you don't have to be that nervous!"
    teacher "It is pretty weird to have a new transfer student at this time of the school year, but don't let that bring you down! I'm sure you'll make friends quickly!"
    call nameplayer
    teacher "See? You already have a pretty nice name! You're on a roll!"
    teacher "Okay, so... according to this, you transfered to our school by a student exchange program, you had a lot of choices, yet you still chosen us! What made you choose this school?"
    menu:
        "What made you choose this school?"
        "My mother attended Hanasakigawa when she was a student.":
            jump fd_hanasakigawa
        "I like the study program Haneoka offers.":
            jump fd_haneoka
return

label fd_hanasakigawa: # First day at Hanasakigawa (Tae, Arisa, Sayo)
    teacher "Such a deep reason! Surely Hanasakigawa is a school with many loving memories from past generations!"

    return

label fd_haneoka: # First day at Haneoka (Kaoru, Tomoe, Hina)
    teacher "How diligent of you! We are proud of our students here in Haneoka, I trust you'll excel in all your classes."

    return

label nameplayer:
    teacher "So... first things first, what was your name again?"
    $ first_name = renpy.input("What is your first name?")
    $ first_name = first_name.strip()
    $ last_name = renpy.input("What is your last name?")
    $ last_name = last_name.strip()
    teacher "So your name is [first_name] [last_name], did I get that right?"
    menu:
        "Yes, I'm [first_name] [last_name]":
            pass
        "No":
            teacher "Sorry! I got it wrong!"
            call nameplayer
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
