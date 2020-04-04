#written by cookie - referred to renpy doc and this: https://lemmasoft.renai.us/forums/viewtopic.php?t=23071
$ import variables as var

screen guestScreen(i):

    frame:
        xpadding 10
        ypadding 10
        xalign 0.5
        yalign 0.5
        xysize(300,100)
        xpos 220
        ypos 100
        text "[i.desc]":#desc
            xysize (300,100)
    add "[i.img]" xalign 1.0 yalign 0.0 xpos 1150




# example use:

label hostClub:

    $guestChosen = renpy.random.choice(guests)#chooses random guest to visit
    show screen guestScreen(guestChosen)
    "my personality is [guestChosen.personality]"

    call screen giftscreenGuest

    $giftChosen = _return #variable to hold the gift chosen by the user

    "[giftChosen]"

    if giftChosen in guestChosen.giftPref:
        "Yay! I like this!"
    else:
        "Oh. This stinks."


    call screen convo
    $topicChosen = _return
    if topicChosen.ID in guestChosen.convoPref:
        "We had a good conversation!"
        call convoAdv(topicChosen,guestChosen) from _call_convoAdv
    else:
        "We had a boring conversation..."
        
    hide screen guestScreen

    call dateInteraction from _call_dateInteraction
    return
