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
#variable that hanasakigawa has been chosen as school (COOKIE)
#    $ hanasakigawa = 1
#Not really needed since the game knows what school you picked when you chose it. -Tondo
#SAYO START
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
    user "S-sorry.. ma'am?"
    s "Drop the honorific, it’s Hikawa to you. We’ve wasted enough time here, please pay more attention to your appearance in the future."
    "We descend a flight of stairs and arrive at the library."
    s "This is the library. The books range from print to electronic, all books arranged according to the Dewey Decimal."
    "..."
    "The poster on the other wall reads “Literature Club: Making Poetry Lovers Doki Doki Since 2017!”"
    "It looks familiar."
    "My thoughts drown out her voice, and it’s too late when I realise this. Hikawa-san looks as if she’s going to eat me alive."
    "She merely sighs and shakes her head."
    "We leave the library."
    "The Hanasakigawa campus is a good bit fancier than what I’m used to.  They have Macs in every classroom and a lift at each end of the corridors."
    if pronoun == sheHer:
        "Otonokizaka didn’t even have a heating system."
    else:
        pass
    "I try to pay attention as she tours me around, asking the least stupid questions I can, and she answers me patiently enough."
    "Sometimes I even notice a hint of a smile."
    "It’s {w}not{w=1.0} unattractive."
    "I ask if we could go up a set of metal staircases."
    s "T-There’s no reason not to..."
    "Here on the rooftop are two telescopes too expensive for my civilian hands."
    "Just to acknowledge my guide I ask about the telescopes."
    s "Astronomy club."
    "Her spat response came with a withering glance at the telescope on the left."
    "Damn, she must hate stars. Or... is it me?"
    "Before I could say anything she spins aggressively towards the staircase and runs down it in a way that isn’t entirely disciplinary committee."
    "Her long legs far outpace me, but I manage to catch up."
    user "Hikawa-san, are you alright? I’m sorry..."
    s "Who are you to care? You're no one to me."
    user "I..."
    "The bell rings, and she leaves without looking back."
    "Sayo Hikawa, cold as her name."
    "I trudge to my class, 2A on the second floor. On the corkboard in the corridor is a poster I never noticed."
    "It says Hanasakigawa Host Club, and on it are two girls dressed as French maids serving tea."
    "Hikawa-san’s in the middle dressed as a butler, turquoise hair pulled back in a ponytail."
    "She’s smiling at invisible royalty."
    #Missing the Sayo intro -> post class transition.
    jump arisa
    jump Tae
    return

# MOVED HANEOKA OPTION DOWN HERE SO IT IS CLEANER
#All the kaoru sprits seem to be a bit unaligned, some play testing would need to be done to adjust them. -Tondo
#I am aware that the kaoru sprites are unaligned but they are only placeholder so I kept that as is. This will be fixed when we get proper sprites. (COOKIE)
label fd_haneoka: # First day at Haneoka (Kaoru, Tomoe, Hina)
#variable for haneoka choice (COOKIE)
#    $ haneoka = 1
#Again, this variable ain't really needed. -Tondo
    #KAORU START
    principal "How diligent of you, [user]! We are proud of our students here in Haneoka, I trust you'll excel in all your classes."
    "I sure hope so."

    #scene for hallway
    "The principal told me I would find my tour guide ‘Seta Kaoru’ upstairs in the drama club room, so I guess that’s my next stop."
    "I walk down the hallway to find the staircase. As I climb up each step, I count out loud out of mere curiosity."
    user "One {w}Two{w=1.0} Three {w}Four{w=1.0}"
    user "Five {w}Six{w=1.0} Seven {w}Eight{w=1.0}"
    user "Nine {w}Ten{w=1.0} Eleven {w}Twelve{w=1.0}"
    "Just as I was about to bring my other foot up..."
    #defining karou as unknown (as player does not yet know them)
    #All the girls can be defined as ??? when first defined up top, and later redefined with their proper names as the player gets to know them, to avoid
    #multiple redefinings. -Tondo
    $ k = "???"
    k "Thirteen!"
    "An alluring voice called out. Startled by the voice, I lose my balance and start to stumble backwards."
    user "Crap!"
    with vpunch
    "This is it."
    "I’m going to die by stairs."
    "I close my eyes and brace for the painful impact of the hard floor until something- or rather, someone- grabbed my waist."
    show old_karou_smile
    k "Are you alright, my little kitten?"


    #image will show without and the player can admire it as much as they want until they click to move on
    hide old_karou_smile
    window hide
    show placeholder_karou_cg with fade
    $ renpy.pause ()

    #game continues when player clicks
    window show
    "My eyes open to see a purple haired girl gripping the railing of the staircase to prevent the both of us from falling."
    user "U-um... yeah..."
    "Flustered by the intimate contact, I couldn’t help but blush. It didn’t help that her crimson eyes stared into my own."
    $ k = "Purple haired girl"
    k "I’m relieved. It would be an injustice if a cute little kitten such as yourself were to be harmed."
    "She pulled me up and guided me safely to the top of the staircase."
    hide placeholder_karou_cg

    show old_karou_idle
    "Her voice sounded familiar though{w}...Ah."
    #There was a new paragraph created just for the closing parenthesis, I don't know if that's what you intended but it looked kinda odd, so I removed it.
    #Thank for editing - was supposed to be wait. Changed. (COOKIE)
    "I remember that someone said “Thirteen” which surprised me and made me lose my balance. Her voice was the same voice."
    user "Although I wouldn’t have tripped if you didn’t surprise me by calling out ‘Thirteen’ like that..."
    hide old_karou_idle
    show old_karou_suprised
    k "What?"
    k "I haven’t uttered a word."
    hide old_karou_suprised
    show old_karou_pride2
    k "Perchance I was on my way downstairs that I’ve come across you, my damsel,  in a moment of distress and risked life and limb to save you."
    "Eeehhh?"
    "I did hear rushing footsteps and there’s no one else here. If that’s true..."
    user "If you didn’t say that then who did? There isn’t anyone else here."
    hide old_karou_pride2
    show old_karou_suprised
    "The purple haired girl froze. Her face paled at my words."
    hide old_karou_suprised
    show old_karou_scared
    k "I-it might have been nothing."
    hide old_karou_scared
    show old_karou_idle
    k "Well if you look at the time, I must be going to the principal’s office. I have to pick up what I’ve forgotten for a new student."
    "She forgot something? And it’s something for a new student? {w}Could she be..?"
    user "Are you Seta Kaoru?"
    $ k = "Kaoru"
    k "Why yes, I am."
    hide old_karou_idle
    show old_karou_pride
    k "Now that you know my name, may I have the honor of knowing yours, my little kitten?"
    user "I’m [fullName], the new student. The principal gave me what you left behind and told me to meet you in the drama club room."
    hide old_karou_pride
    show old_karou_pride2
    k "Ah yes, as leader of the host club, it’s my duty as a prince to show a lovely little kitten like you around the school."
    hide old_karou_pride2
    show old_karou_scared
    k "If I may, I believe what I forgot was your schedule."
    "I hand over my schedule and she looks over it."
    hide old_karou_scared
    show old_karou_pride2
    k "Ah I see. How fleeting."
    "She hands my schedule back to me."
    hide old_karou_pride2
    show old_karou_pride
    k "Let us embark now on a journey around the school."
    "We began the tour of the school."
    hide old_karou_pride

    "We stopped by the gym"
    #here we would use scene x with fade. this will be done when all backgrounds are done
    #Which would work better, 4 lines each with it's own scene or 1 line split into 4 paragraphs and a scene for each paragraph with the pause/wait function? -Tondo
    #I think 4 lines (COOKIE)
    "We stopped by the auditorium"
    "We stopped by the classrooms"
    "We stopped by the the drama club"


    #scene should return to hallway after tour
    user "Are there other clubs here at the school?"
    show old_karou_idle
    k "Yes. Off the top of my head, there’s the enthusiastic dance club, the dedicated student council, and the vigorous tennis club."
    "I don’t think I can deal with the busy work the student council is given. The dance club and tennis club seems to be really active given what Kaoru said. And I don’t think I have it in me to act so dramatic or act realistically."
    user "Are there any other clubs?"
    k "Of course, there are other clubs. In fact, I myself am a part of another club."
    "Oh yeah, that’s right."
    user "You mentioned being the leader of the host club. But what is this ‘host club’?"
    hide old_karou_idle
    show old_karou_pride2
    k "The host club is-"
    "Before she could finish, the bell rang."
    hide old_karou_pride2
    show old_karou_smile
    k "I guess this is the end of the tour. It’s best if we head to class."
    hide old_karou_smile
    show old_karou_pride
    k "Adieu, my little kitten."
    hide old_karou_pride
    "She flashed a princely smile before she left. I decide to head to class too but one thing on my mind remains unanswered."
    "What the hell is the host club?"

    jump hostClubHaneoka
    return

label hostClubHanasaki:
    # GUEST(S) ARRIVE
    #Remember that to use backgrounds and the scene function, you first have to define the image, for organization it's done below line 33. -Tondo
    scene back
    "It looks like a guest just arrived. I better go and impress them!"
    show old_kasumi_wave
    ka "Hi hi!"
    hide old_kasumi_wave
    show old_kasumi_excited
    ka "Wow! It's so big and fancy in here!"
    hide old_kasumi_excited
    show old_kasumi_determined
    ka "Oi! You must be a host here!"
    user "Uh, yeah..."
    "I'm still not used to this whole 'host' thing but I have to get into it!"
    "This time, I give a big smile to the girl."
    user "I mean, welcome to the host club! Have a seat!"
    hide old_kasumi_determined
    show old_kasumi_idle
    ka "Okay okay!"
    hide old_kasumi_idle
    "I feel eyes on me, so I turn around."
    show old_arisa_cross
    "Is that...Arisa watching me?"
    hide old_arisa_cross
    "No it couldn't be...right? Anyway, I have to go and talk to this guest."
    show old_kasumi_idle
    ka "Sooo..."
    hide old_kasumi_idle
    show old_kasumi_curious
    ka "What do we do now? Are you going to perform a trick for me?"
    user "Not quite. Well I mean, I hope I can bewitch you with my hosting skills!"
    "...that was so corny."
    hide old_kasumi_curious
    show old_kasumi_excited
    ka "Wah! So cool! Alright, I'm ready! Let's go!"
    user "Okay let's talk about..."
    # PLAYER CHOOSES WHAT TO TALK ABOUT
    menu:
        # SAFE OPTION ; NETURAL AFFECTION
        "Music":
            #Instead of having multiple choice variable then rewarding or punishing the player at the end of this interaction, we could just reward or
            #punish the player as they make the choices and use an if statement to varify the amount of points and, based on that, what reaction to use.
            $ affection = affection + 0
            hide old_kasumi_excited
            show old_kasumi_determined
            ka "Gah! I love music! I can sing and play guitar!"
            hide old_kasumi_determined
            show old_kasumi_curious
            ka "What do you play?"
            user "I play trumpet."
            hide old_kasumi_curious
            show old_kasumi_excited
            ka "Wow! Amazing, amazing! I've not met someone who has played trumpet!"
            hide old_kasumi_excited
            show old_kasumi_idle
            jump after_menu
        #RISKY OPTION ; +- AFFECTION
        "Bonsai":
            # A label isn't really needed here, plus it uses less resources.
            hide old_kasumi_excited
            show old_kasumi_curious
            ka "Bon...sai?"
            hide old_kasumi_curious
            show old_kasumi_idle
            ka "Ah, ah! I know! That's what Arisa likes!"
            "She knows Arisa? I didn't think Arisa would be able to stand people like her, maybe I was wrong."
            hide old_kasumi_idle
            show old_kasumi_curious
            ka "Hey hey! Give me a bonsai style!"
            menu:
                #BEST CHOICE
                "Chokkan.":
                    $ affection = affection + 5
                    user "Chokkan is probably one of the most common."
                    hide old_kasumi_curious
                    show old_kasumi_idle
                    user "Chokkan trees have upright trunks, like ones in nature, and are considered pretty formal."
                    jump after_menu
                #BAD CHOICE
                "Rikka.":
                    $ affection = affection - 5
                    user "Rikka is a popular one."
                    hide old_kasumi_curious
                    show old_kasumi_idle
                    user "It has nine branches to show parts of nature and how beautiful it is."
                    jump after_menu
                #WORST CHOICE
                "Ikebana.":
                    $ affection = affection - 10
                    user "Ikebana is a good one."
                    hide old_kasumi_curious
                    show old_kasumi_idle
                    user "Ikebana is an arrangement which give life to flowers!"
                    "Wait, is this really bonsai? Oh well, Kasumi doesn't seem to notice the difference so it will be fine."
                    jump after_menu
    return

    label after_menu:
        #GUEST LEAVES
        hide Kasumi
        hide old_kasumi_idle
        show old_kasumi_determined
        ka "Anyway, let me tell you about myself instead!"
        hide old_kasumi_determined
        "Kasumi talks about the iconic moment of her life when she went to see the stars."
        show kasumi_idle
        ka "That was fun!"
        hide old_kasumi_idle
        show old_kasumi_wave
        ka "Bye bye!"
        user "Thank you for coming!"
        hide old_kasumi_wave
        "Kasumi left with a smile on her face"
        jump arisa_reaction
    return

    #GIRL REACTIONS
    #Theres no need to use multiple ifs, you can use one if, multiple elifs, then one final else.
    label arisa_reaction:
        # + AFFECTION
        if (affection > 0):
            show old_arisa_happy
            a "You know about bonsai trees?"
            user "Ah, yes!"
            hide old_arisa_happy
            show old_arisa_cross
            a "I mean, of course you'd KNOW of them, but..."
            hide old_arisa_cross
            show old_arisa_impressed
            a "I didn't think YOU would know what Chokkan was!"
            hide old_arisa_impressed
            "Arisa walks away, grinning to herself. She seems impressed. I must have made a good impression!"
            jump showAffection
        # NETURAL AFFECTION
        elif affection == 0:
            show old_arisa_happy
            a "You didn't do too bad there."
            hide old_arisa_happy
            show old_arisa_cross
            a "But don't think that means you can slack off! There's always room for improvement!"
            hide old_arisa_cross
            "Arisa is the same as always"
            jump showAffection
        # - AFFECTION
        elif (affection < 0) and (affection > -6):
            show old_arisa_cross
            a "You know Rikka is flower arrangement, right?"
            user "Huh?"
            hide old_arisa_cross
            show old_arisa_angry
            a "You know? Rikka is part of Ikebana!"
            user "I must have mixed the two up! Good thing Kasumi didn't notice!"
            hide old_arisa_angry
            show old_arisa_sad
            a "Yeah..."
            hide old_arisa_sad
            "Arisa walks off, disappointed."
            jump showAffection
        # -- AFFECTION
        else:
            show old_arisa_angry
            a "Are you stupid? An idiot can tell the difference between flower arranging and bonsai!"
            hide old_arisa_angry
            show old_arisa_cross
            a "I expected more from you, jeez!"
            hide old_arisa_cross
            "Arisa storms off, she is really mad!"
            return
        jump Tae

#TAE START
#tae is said to start after school so put code here. added variable so this is triggered if player is in hanasakigawa (COOKIE)
#ALIGNMENT IS OFF BUT NOT CORRECTED SINCE PLACEHOLDER (COOKIE)
label Tae:
    "I think i should make my way home now."
    "Huh…?"
    "Walking past it I notice a girl in the middle school pet room."
    show tae_smile
    "Draped over the Hanasakigawa high school uniform is waist-length dark hair."
    "I don’t know many people with waist-length hair in high school, yet on this girl it works like a charm."
    hide tae_smile
    show tae_glad
    $ ta = "Dark-haired girl"
    ta "mn… you are so cute..."
    "For some reason I’ve been seized by an urge to take this girl into my arms and protect her from all the evils in the world."
    ta "So cute.. I want to take you home so bad..must..resist..but..."
    "I watch as she sets a rabbit free from its cage, then two --{w}Wait… Is she trying to steal!?"
    "I can’t just leave the rabbits at her mercy and go home!"
    "I rush towards her."
    with hpunch
    user "Stop! Thief!"
    hide tae_glad
    show tae_curious
    ta "Huh? I’m not a thief."
    "She looks as if she has more to say, but trails off at the sight of a lop eared rabbit snuffling her hand."
    hide tae_curious
    show tae_smile
    "She ignores me altogether and pets the creature."
    user "You know stealing is bad right?"
    hide tae_smile
    show tae_serious
    ta "Who doesn’t?"
    "She still goes to get more rabbits out of the cage."
    user "What if the middle school kids knew you were stealing their rabbits? Worse still, the teachers? You could get suspended, you could get expelled, you could-"
    hide tae_serious
    show tae_smile
    ta "They know."
    "She cuddles the rabbit, not seeming concerned with my accusations." #adding new monologe for the ** parts (COOKIE)
    user "What? And they are okay with that?"
    #made if statement to try and tidy things up (COOKIE)
    #IF STATEMENT DOES NOT WORK. INTENDED PURPOSE IS THAT WHEN PRONOUNS ARE HEHIM THEN SPECIAL DIALOUGE APPEARS, AND IF NOT THE DIALOUGE IS SKIPPED AND IGNORED WITH THE IF. (COOKIE)
    #The reason it wasn't working is becuase you were using one = instead of 2, when using 1 = then you're assigning a value to a variable (see lines 9-37)
    #when using 2 == you're checking if the variable is has that value (see line 94) -Tondo
    if pronoun == heHim:
        "I guess I transferred to a different planet. Girls’ schools are an ...experience. If I slapped myself this will all be my imagination and whoever this girl is will not be stealing bunny rabbits from 13 year olds."
    else:
        pass
    ta "Yeah, You can feed them too, you know?"
    user "That’s why i sai- huh? What?"
    "She fumbles around in her pocket to reveal carrot sticks."
    hide tae_smile
    show tae_serious
    ta "Now hold him for me."
    "The lop eared rabbit in my lap is brown. Fluffy. Surprisingly warm, and a good bit heavier than I imagined."
    user "Eh? So you are not going to steal them?"
    "It sniffs the air and snuggles close to me as if in response."
    hide tae_serious
    show tae_curious
    ta "Why would i do that? How could I do such a cruel thing to them?"
    "So she isn’t stealing them…?"
    "She wanted to take them home. I saw her open the cages with my own two eyes. I saw her taking them from the cages. She has carrot sticks with her. There’s only one reason she could be doing th-"
    "How has it never occured to me that she didn’t actually mean to take the rabbits home?{p}...Fuck me. "
    "It’s an age-old habit of mine, jumping to conclusions and embarrassing myself."
    "Maybe I should’ve listened to my thirteen-year-old self and gone through with my plans to disappear into some uncharted cave and die."
    hide tae_curious
    show tae_serious
    ta "There, there. Eat up, Fluffycheeks!"
    user "...Fluffycheeks?"
    "I watch in a trance as Fluffycheeks eats up."
    "I wish I was anywhere but right in front of this girl."
    hide tae_serious
    show tae_smile
    ta "Good boy."
    "I gingerly reach out a hesitant finger to pet Fluffycheeks on its head."
    with fade
    "Long minutes tick by, and eventually she returns all the rabbits to their hutch with a kiss on their foreheads."
    hide tae_smile
    show tae_glad
    ta "Good boy."
    "She puts the last rabbit in its cage and closes it."
    hide tae_glad
    show tae_smile
    ta "Thank you for helping me feed them."
    user "Eh? Ah... You’re welcome."
    hide tae_smile
    show tae_thinking
    ta "Hmm.. By the way..."
    "Is she going to make fun of me for what happened?"
    hide tae_thinking
    show tae_smile
    $ ta = "Tae"
    ta "My name is Hanazono Tae."
    ta "Hope we meet again."
    hide tae_smile
    user "Ah...yes..."
    "I come to my senses, but Hanazono Tae has disappeared without a trace."
    jump showAffection
    return
#ARISA Start
#I think there are other expressions of Arisa that can be used. Not sure on hunch
#Not sure on how to add this within the script
label arisa:
    user "Man... I hope I can get some good food from the cafeteria. At least I hope I have enough money to buy something."
    "I exit the classroom into the hallway. There are a couple of other students out here too but they were travelling to different classrooms to eat with their friends."
    "I take out my wallet to check how much money I have on me when I drop it."
    "I bend down to pick it up when I notice a couple of pieces of paper."
    "Upon closer inspection, they weren’t paper but rather photos."
    "Picking one up, I see it’s a picture of a small tree. It’s really cute! All right, all safe and sound. I pat my pocket to make sure it doesn’t fall."
    "Before I could pick the other pictures up, someone swipes them off from the floor."
    user "Hey! You can’t just take these!"
    "There she was, a light chestnut-haired beauty with a blushing red face."
    #(CG of Arisa blushing and holding the pictures)
    a "What do you mean? These pictures are mine"
    a "If anything, it looks like you were gonna keep them yourself."
    "These photos are hers?"
    "Wait... back up a bit. She thinks I tried to take them. I should clear that up first."
    user "No, I just saw them and wanted to return them."
    user "I wasn’t gonna take them. I swear."
    #(End of CG)
    a "Is that so?"
    a "Then I guess you won’t mind if I count them."
    "Uh-oh. She’ll notice that there’s one missing."
    show old_arisa_angry
    "Before I could even think about pulling the photo out, her glaring eyes had told me it was too late."
    a "Where’s Tamagawa?"
    hide old_arisa_angry
    "Tamagawa? That’s a weird way to ask for the photo."
    user "Is that the name of the photo?"
    show old_arisa_cross
    a "It’s not the name of the photo, it’s the name of my bonsai tree in that photo"
    hide old_arisa_cross
    user "So this tree is named Tamagawa?"
    "I took out the photo and gave it back to her."
    user "Do the other trees have names?"
    "Her face reddened as though she realized she said something embarrassing when I asked her my question."
    a "It’s just the one that has the name. I certainly didn’t name one of my trees Yodogawa."
    "So they do have another names. That reminds me..."
    user "What’s your name?"
    a "Huh? My name? I’m Ichigaya Arisa."
    a "What about you?"
    user "What about me?"
    a "Your name?"
    user "Ah... I’m [fullName]. I’m new here"
    a "Is that so? Well, I have my photos now. I better hurry and spend the rest of the lunch period with my friends."
    user "Ok. I’ll see you around I guess."
    "With a hesitant farewell, she left."
    "She seemed pretty interesting."
    "I wonder if I’ll see her around."
    "Now what was I going to do?"
    "…"
    "Ah! That’s right! I was supposed to buy lunch."
    "Hopefully there’s still to time to get something."
    "And with that, I sprinted towards the cafeteria."
    jump Tae

label hostClubHaneoka:
    hi "Whoops, looks like there's nothing here yet. Come back later."
    jump showAffection
    return

#Changed the name of the label to avoid any confusion with the variable itself.
label showAffection:
    "Your affection level is [affection]"
    # This ends the game.
    return
    #choice that triggers after school scene dependent on school
    #I'm gonna move this to the end but effectively you can only jump to Taes intro if you chose Hanasaki so the variable isn't necessary. -Tondo

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
