# I changed the name of the file so it doesn't interfere with the actual script.
# I'll have this in it's own file then copy paste the code in the actual script.

define a = Character("Arisa", color="#800080")
define ka = Character("Kasumi", color="#ff0000")
#As a heads up, in the code we use user to call the players name, unless a character specifically calls MC something else,
#but here p for player is fine since it's a prototype.
define p = Character("Player")

# Used $ instead of define because, much like the pronouns and user, its used to define an empty variable.
$ affection = 0

#I've adjusted the indentation so it fits better with the already existing code.
label hostClub:
    # GUEST(S) ARRIVE
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
        if affection > 0:
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