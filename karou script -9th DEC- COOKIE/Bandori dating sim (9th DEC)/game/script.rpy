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
define affection = 0

define k = Character("Kaoru")
define t = Character("Tomoe")
define h = Character("Hina")
define s = Character("Sayo")
define a = Character("Arisa", color="#800080")
define ta = Character("Tae")
define ka = Character("Kasumi", color="#ff0000")

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
    principal "Okay, so... according to this, you transferred to our school via a student exchange program, you had a lot of choices, yet you still chosen us! What made you choose this school?"
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
    "We step outside of the teachers lounge and into the empty hallway, presumably because everyone is in class."
    "For a, not-so-brief, moment we stare each other down like lions in a pit."
    s "..."
    user "..."
    s "Did you even bother to try and look decent for a new school? All your buttons are done up the wrong way."
    s "Will you excuse yourself as to look presentable, or shall I redo them for you?"
    menu:
        "Wha... I didn\'t notice, I-I\'ll be right back.":
            call herbivore
        "I dare you to.":
            call carnivore
        "...":
            call passive

    s "We’ve wasted enough time here, please pay more attention to your appearance in the future."
    "We descend a flight of stairs and arrive at the library."
    s "This is the library. The books range from print to electronic, fiction to non-fiction..."
    "They have Kindles!?"
    "A cuckoo clock on the wall next to us chimes, and I watch the bird pop in and out and back in again."
    "The poster reads “Doki Doki Literature Club: Join Us Now!”"
    "My mind begins to note everything but her voice, and it’s too late when I realise this."
    s "Why are you even here? Why don’t you go back to wherever you came from?"
    jump hostClub
    return


label herbivore: # You redo your buttons yourself
    "I do them up again, this time, hopefully, correct. My reflection has four buttons, two on each side."
    "As I leave the washroom, I see [s] waiting for me outside, the expression on her face is an interesting mix of contempt and amusement."
    return

label carnivore:
    s "You\'re insufferable, the washroom is down the corridor. Go on now."
    "And so off I went."
    "I came back to the same haughty expression."
    return

label passive:
    s "You remind me of my insufferable younger twin. Make haste and come on over."
    "I watch as she undoes my buttons and deftly does them up again. My lips form some sort of protest, but they dissolve in my mouth."
    return

# MOVED HANEOKA OPTION DOWN HERE SO IT IS CLEANER

    label fd_haneoka: # First day at Haneoka (Kaoru, Tomoe, Hina)
        principal "How diligent of you, [user]! We are proud of our students here in Haneoka, I trust you'll excel in all your classes."
        "I sure hope so."

        #scene for hallway
        user "(The principal told me I would find my tour guide ‘Seta Kaoru’ upstairs in the drama club room, so I guess that’s my next stop.)"
        user "(I walk down the hallway to find the staircase. As I climb up each step, I count out loud out of mere curiosity.)"
        user "One {w}Two{w=1.0} Three {w}Four{w=1.0}"
        user "Five {w}Six{w=1.0} Seven {w}Eight{w=1.0}"
        user "Nine {w}Ten{w=1.0} Eleven {w}Twelve{w=1.0}"
        user "(  Just as I was about to bring my other foot up...)"
        #defining karou as unknown (as player does not yet know them)
        $ k = "???"
        k "Thirteen!"
        user "(An alluring voice called out. Startled by the voice, I lose my balance and start to stumble backwards.)"
        user "Crap!"
        with vpunch
        user "(This is it.)"
        user "(I’m going to die by stairs.)"
        user "(I close my eyes and brace for the painful impact of the hard floor until something- or rather, someone- grabbed my waist.)"
        show karou_smile
        k "Are you alright, my little kitten?"


        #image will show without and the player can admire it as much as they want until they click to move on
        hide karou_smile
        window hide
        show placeholder_karou_cg with fade
        $ renpy.pause ()

        #game continues when player clicks
        window show
        user "(My eyes open to see a purple haired girl gripping the railing of the staircase to prevent the both of us from falling.)"
        user "U-um... yeah..."
        user "(Flustered by the intimate contact, I couldn’t help but blush. It didn’t help that her crimson eyes stared into my own.)"
        $ k = "Purple haired girl"
        k "I’m relieved. It would be an injustice if a cute little kitten such as yourself were to be harmed."
        user "(She pulled me up and guided me safely to the top of the staircase.)"
        hide placeholder_karou_cg

        show karou_idle
        user "(Her voice sounded familiar though{p}...Ah.{p=1.0})"
        user "(I remember that someone said “Thirteen” which surprised me and made me lose my balance. Her voice was the same voice.)"
        user "Although I wouldn’t have tripped if you didn’t surprise me by calling out ‘Thirteen’ like that..."
        hide karou_idle
        show karou_suprised
        k "What?"
        k "I haven’t uttered a word."
        hide karou_suprised
        show karou_pride2
        k "Perchance I was on my way downstairs that I’ve come across you, my damsel,  in a moment of distress and risked life and limb to save you."
        user "(Eeehhh?)"
        user "(I did hear rushing footsteps and there’s no one else here. If that’s true...)"
        user "If you didn’t say that then who did? There isn’t anyone else here."
        hide karou_pride2
        show karou_suprised
        user "(The purple haired girl froze. Her face paled at my words.)"
        hide karou_suprised
        show karou_scared
        k "I-it might have been nothing."
        hide karou_scared
        show karou_idle
        k "Well if you look at the time, I must be going to the principal’s office. I have to pick up what I’ve forgotten for a new student."
        user "(She forgot something? And it’s something for a new student? {p}Could she be..?{p=1.0})"
        user "Are you Seta Kaoru?"
        $ k = "Kaoru"
        k "Why yes, I am."
        hide karou_idle
        show karou_pride
        k "Now that you know my name, may I have the honor of knowing yours, my little kitten?"
        user "I’m [fullName], the new student. The principal gave me what you left behind and told me to meet you in the drama club room."
        hide karou_pride
        show karou_pride2
        k "Ah yes, as leader of the host club, it’s my duty as a prince to show a lovely little kitten like you around the school."
        hide karou_pride2
        show karou_scared
        k "If I may, I believe what I forgot was your schedule."
        user "(I hand over my schedule and she looks over it.)"
        hide karou_scared
        show karou_pride2
        k "Ah I see. How fleeting."
        user "(She hands my schedule back to me.)"
        hide karou_pride2
        show karou_pride
        k "Let us embark now on a journey around the school."
        user "(We began the tour of the school.)"
        hide karou_pride

        user "(We stopped by the gym)"
        #here we would use scene x with fade. this will be done when all backgrounds are done
        user "(We stopped by the auditorium)"
        user "(We stopped by the classrooms)"
        user "(We stopped by the the drama club)"


        #scene should return to hallway after tour
        user "Are there other clubs here at the school?"
        show karou_idle
        k "Yes. Off the top of my head, there’s the enthusiastic dance club, the dedicated student council, and the vigorous tennis club."
        user "(I don’t think I can deal with the busy work the student council is given. The dance club and tennis club seems to be really active given what Kaoru said. And I don’t think I have it in me to act so dramatic or act realistically.)"
        user "Are there any other clubs?"
        k "Of course, there are other clubs. In fact, I myself am a part of another club."
        user "(Oh yeah, that’s right.)"
        user "You mentioned being the leader of the host club. But what is this ‘host club’?"
        hide karou_idle
        show karou_pride2
        k "The host club is-"
        user "(Before she could finish, the bell rang.)"
        hide karou_pride2
        show karou_smile
        k "I guess this is the end of the tour. It’s best if we head to class."
        hide karou_smile
        show karou_pride
        k "Adieu, my little kitten."
        hide karou_pride
        user "(She flashed a princely smile before she left. I decide to head to class too but one thing on my mind remains unanswered.)"
        user "(What the hell is the host club?)"

        jump hostClub
        return

label hostClub:
    # GUEST(S) ARRIVE
    scene back
    user "(It looks like a guest just arrived. I better go and impress them!)"
    show kasumi_wave
    ka "Hi hi!"
    hide kasumi_wave
    show kasumi_excited
    ka "Wow! It's so big and fancy in here!"
    hide kasumi_excited
    show kasumi_determined
    ka "Oi! You must be a host here!"
    user "Uh, yeah...(I'm still not used to this whole 'host' thing but I have to get into it! This time, I give a big smile to the girl.)"
    user "I mean, welcome to the host club! Have a seat!"
    hide kasumi_determined
    show kasumi_idle
    ka "Okay okay!"
    hide kasumi_idle
    user "(I feel eyes on me, so I turn around.)"
    show arisa_cross
    user "(Is that...Arisa watching me?)"
    hide arisa_cross
    user "(No it couldn't be...right? Anyway, I have to go and talk to this guest.)"
    show kasumi_idle
    ka "Sooo..."
    hide kasumi_idle
    show kasumi_curious
    ka "What do we do now? Are you going to perform a trick for me?"
    user "Not quite. Well I mean, I hope I can bewitch you with my hosting skills!"
    user "(...that was so corny.)"
    hide kasumi_curious
    show kasumi_excited
    ka "Wah! So cool! Alright, I'm ready! Let's go!"
    user "Okay let's talk about..."
    # PLAYER CHOOSES WHAT TO TALK ABOUT
    menu:
        # SAFE OPTION ; NETURAL AFFECTION
        "Music":
            #Instead of having multiple choice variable then rewarding or punishing the player at the end of this interaction, we could just reward or
            #punish the player as they make the choices and use an if statement to varify the amount of points and, based on that, what reaction to use.
            $ affection = affection + 0
            hide kasumi_excited
            show kasumi_determined
            ka "Gah! I love music! I can sing and play guitar!"
            hide kasumi_determined
            show kasumi_curious
            ka "What do you play?"
            user "I play trumpet."
            hide kasumi_curious
            show kasumi_excited
            ka "Wow! Amazing, amazing! I've not met someone who has played trumpet!"
            hide kasumi_excited
            show kasumi_idle
            jump after_menu
        #RISKY OPTION ; +- AFFECTION
        "Bonsai":
            # A label isn't really needed here, plus it uses less resources.
            hide kasumi_excited
            show kasumi_curious
            ka "Bon...sai?"
            hide kasumi_curious
            show kasumi_idle
            ka "Ah, ah! I know! That's what Arisa likes!"
            user "(She knows Arisa? I didn't think Arisa would be able to stand people like her, maybe I was wrong.)"
            hide kasumi_idle
            show kasumi_curious
            ka "Hey hey! Give me a bonsai style!"
            menu:
                #BEST CHOICE
                "Chokkan.":
                    $ affection = affection + 5
                    user "Chokkan is probably one of the most common."
                    hide kasumi_curious
                    show kasumi_idle
                    user "Chokkan trees have upright trunks, like ones in nature, and are considered pretty formal."
                    jump after_menu
                #BAD CHOICE
                "Rikka.":
                    $ affection = affection - 5
                    user "Rikka is a popular one."
                    hide kasumi_curious
                    show kasumi_idle
                    user "It has nine branches to show parts of nature and how beautiful it is."
                    jump after_menu
                #WORST CHOICE
                "Ikebana.":
                    $ affection = affection - 10
                    user "Ikebana is a good one."
                    hide kasumi_curious
                    show kasumi_idle
                    user "Ikebana is an arrangement which give life to flowers!"
                    user "(Wait, is this really bonsai? Oh well, Kasumi doesn't seem to notice the difference so it will be fine.)"
                    jump after_menu
    return

    label after_menu:
        #GUEST LEAVES
        hide Kasumi
        hide kasumi_idle
        show kasumi_determined
        ka "Anyway, let me tell you about myself instead!"
        hide kasumi_determined
        user "(Kasumi talks about the iconic moment of her life when she went to see the stars.)"
        show kasumi_idle
        ka "That was fun!"
        hide kasumi_idle
        show kasumi_wave
        ka "Bye bye!"
        user "Thank you for coming!"
        hide kasumi_wave
        user "(Kasumi left with a smile on her face)"
        jump arisa_reaction
    return

    #GIRL REACTIONS
    #Theres no need to use multiple ifs, you can use one if, multiple elifs, then one final else.
    label arisa_reaction:
        # + AFFECTION
        if (affection > 0):
            show arisa_happy
            a "You know about bonsai trees?"
            user "Ah, yes!"
            hide arisa_happy
            show arisa_cross
            a "I mean, of course you'd KNOW of them, but..."
            hide arisa_cross
            show arisa_impressed
            a "I didn't think YOU would know what Chokkan was!"
            hide arisa_impressed
            user "(Arisa walks away, grinning to herself. She seems impressed. I must have made a good impression!)"
            jump showAffection
        # NETURAL AFFECTION
        elif affection == 0:
            show arisa_happy
            a "You didn't do too bad there."
            hide arisa_happy
            show arisa_cross
            a "But don't think that means you can slack off! There's always room for improvement!"
            hide arisa_cross
            user "(Arisa is the same as always)"
            jump showAffection
        # - AFFECTION
        elif (affection < 0) and (affection > -6):
            show arisa_cross
            a "You know Rikka is flower arrangement, right?"
            user "Huh?"
            hide arisa_cross
            show arisa_angry
            a "You know? Rikka is part of Ikebana!"
            user "I must have mixed the two up! Good thing Kasumi didn't notice!"
            hide arisa_angry
            show arisa_sad
            a "Yeah..."
            hide arisa_sad
            user "(Arisa walks off, disappointed.)"
            jump showAffection
        # -- AFFECTION
        else:
            show arisa_angry
            a "Are you stupid? An idiot can tell the difference between flower arranging and bonsai!"
            hide arisa_angry
            show arisa_cross
            a "I expected more from you, jeez!"
            hide arisa_cross
            user "(Arisa storms off, she is really mad!)"
            jump showAffection
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
