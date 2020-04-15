$ import variables as var

label fd_allscript:
    jump base
    return

label base:
    #here is the base code for each script - with commentary by yours truly! (cookie)

    #note that all images are defined and callable by the names assigned to them on the variables.rpy file - please refer to this!

    #showing a background - "dissolve" is our go-to transistion for scenes
    scene rooftop with dissolve

    #showing arisas default sprite - "fade" is our go-to transistion for sprites
    show a default with fade

    #dialogue from arisa (denoted with a) and the user (denoted with user)
    a "Hello world."
    a "Ugh, who even says that?"

    #showing new arisa expression - all arisa sprites are grouped together so no need to hide images, etc
    show a sweats with fade

    a "Anyway, I'm here to teach you how the script should go for most scripts...Whatever that means."
    user "It's a little cold up here - we should move."
    a "Seriously? We're moving already? This whole thing is already getting on my nerves..."

    #new background
    scene class day with dissolve

    #use renpy notify to text at the top right of the screen - i think we should use renpy notify for telling the player where they are - like so
    $renpy.notify("Classroom")

    show a annoyed with fade
    a "Okay, happy now?"

    #choice menu
    menu:
        "It was better outside":
            #dialogue that appears for this choice
            show a angry with fade
            a "Are you kidding me? I can't believe this!"
            user "Hey - I'm only kidding."
            show a annoyed with fade
            a "Pshaw - Okay, okay. Got it."
        "Yes. Thank you.":
            #dialogue that appears for the other choice
            show a embarassed with fade
            a "Wha - W-Why are you thanking me for nothing?"
            show a annoyed with fade
            a "Idiot."

    #dialogue that appears after the choice - will appear no matter the choice made
    #a new characters enters the scene - move the other sprite to the side (either at l to display at left or at r to display at right). use the ianctive
    #expression for a sprite when the character is not actively speaking. the move transistion will be used when we move a character
    show a inactive at l with move
    show s default2 at r with fade
    s "What's going on over here?"

    #when a sprite becomes inactive, dont use the fade transistion (it looks a little weird for me)
    show s inactive
    show a sweats with fade

    #when the player is being referred to by first name, use var user
    a "Ah - Sayo! Uh, nothing is going on, right, [user]?"
    user "Yeah."
    show a inactive
    show s angry3 with fade
    s "Okay, but just so you know, you both are being really loud. So, can you at least lower your voices?"
    show s inactive
    show a embarassed with fade

    #when the players pronouns are being used, call the pronoun array and the corresponding index. see the variable.rpy for the pronoun indexs
    a "Huh? [pronoun[3]] the one making all the noise!"
    show a inactive
    show s default1 with fade
    s "Whatever you say."

    #to remove a sprite off screen, use the hide statement - using easeoutright as sayo was showing at right and is going to exit to the right
    hide s with easeoutright

    #re-centering arisa as she is now the only character on screen
    show a default at center with move

    #for the players inner dialogue, just don't use tags
    "And with that, Sayo left."

    show a annoyed with fade
    a "Who does she think she is?"
    show a sweats with fade

    #if the user is being to referred to by last name, use var last_name
    a "Jeez - Now I feel like everyone is watching me...L-Let's just go, [last_name]!"

    user "Right."
    "Arisa and I go to leave...But..."
    show a embarassed with fade

    #to shake the screen (for drama), use the transistion vpunch
    with vpunch

    a "Gah!"

    #transistion easeoutbottom for arisa to move down the the bottom of the screen before disappearing - as if she actually fell!
    hide a with easeoutbottom

    "Arisa fell over!"
    user "A-Arisa! Are you alright?"

    #image will show without textbox and the player can admire it as much as they want until they click to move on
    window hide
    show placeholder with dissolve
    $ renpy.pause ()
    #game continues when player clicks - the window reappears and the dialogue continues
    window show
    a "Y-Yeah! I'm fine! Just --"
    a "Stop looking at me!!"

    #the return statement ends the current script (and in this case, the game)
    return
