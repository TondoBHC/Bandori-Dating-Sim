#written by cookie - referred to renpy doc and this: https://lemmasoft.renai.us/forums/viewtopic.php?t=23071

$ import variables as var
# example use:

label hostClub():

    $guestChosen = renpy.random.choice(guests)#chooses random guest to visit
    if guestChosen.ID == 1:
        call yukinaGuest
    jump dateInteraction
    return

#gift IDS - 1 = strawberry shortcake, 2=earl grey, 3=green tea, 4=jello
label yukinaGuest():
    show y default

    #gift segment
    call screen giftscreenGuest
    $giftChosen = _return #variable to hold the gift chosen by the user
    if giftChosen == 1:
        show y blush
        user "I kinda added too much sugar to this batch...I hope that’s okay."
        "She probably didn’t hear that. She’s stuffing forkful after forkful in her mouth...it can’t be that good, can it?"
        show y default
    elif giftChosen ==4:
        "She pokes at it with her spoon hesitantly."
        y "It’s too wobbly for my palate."
    elif giftChosen==3:
        "She frowns at the first sip."
        y "T-thanks, but - *cough* - Could I have some water?"
    elif giftChosen==2:
        "She finishes her tea in a few silent gulps."
        y "I actually prefer coffee, but thanks."

    #convo segment
    call screen convo
    $topicChosen = _return
    if topicChosen.ID == 1:
        "Did you know that cats are solitary animals?"
        show y blush
        y "T-That could be why I like them so much…"
        y "I had a cat when I was younger."
        y "It was really...really cute...Too bad they aren’t with us any more..."

    if topicChosen.ID in guestChosen.convoPref:
        "We had a good conversation!"
        call convoAdv(topicChosen,guestChosen)
    else:
        "We had a boring conversation..."

    hide y

    return
