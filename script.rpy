# The script of the game goes in this file.

init python:
    def max_points(*values):
        return [ i for i, v in enumerate(values) if v == max(values) ]
$ import variables as var
# The game starts here.

#****DAY 1****

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
                $persistent.playername = "[first_name] [last_name]"
            "No":
                "Well then, enter the correct one."
                call nameplayer
        if $ persistent.playerName = "[first_name] [last_name]" and $ persistent.completedTimes > 1:
            "Have we met before?"
        elif $ persistent.completedTimes > 1:
            "Hmm we know someone that had the same name as you. weird."
        else:
            "Have fun!"

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
    "WHAT!? It's already 8, damn it! This is bad, I better hurry up or I\'ll make a bad first impression."
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
    principal "Okay, so... according to this, you transferred to our school via a student exchange program, you had a lot of choices, yet you still chosen us! What made you choose this school?"
    menu:
        "What made you choose this school?"
        "My mother attended Hanasakigawa when she was a student.":
            jump fd_hanasakigawa
        "I like the study program Haneoka offers.":
            jump fd_haneoka
return

#Changed the name of the label to avoid any confusion with the variable itself.
label showAffection:
    "Your affection level is [affection]"
    # This ends the game.
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
#         "Who do you want to bond with?"
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
