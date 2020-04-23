#written by cookie - referred to renpy doc and this: https://lemmasoft.renai.us/forums/viewtopic.php?t=23071
$ import variables as var


#for convo segment with variables before meeting in 08/02/20
screen convo():

    modal True #used so player cant click on anything outside the screen

    frame:
        xpadding 10
        ypadding 10
        xalign 0.5
        yalign 0.5
        xysize(500,557)


        vpgrid:
            #grid define + spacing
            cols 1
            spacing 10


            #code for normal convov1
            #for each convov1 topic - do this
            for i in convos:
                    vbox:
                        textbutton "[i.topic]":
                            xysize(450,20)
                            action Confirm("Is this topic the one you want?",Return(i),NullAction())


label convoAdv(topicC,guestC):
    if topicC.level == 1:
        "I need some advice..."
        if topicC.level == 1:
            "I can give advice!"
            "Because the player has studied [topicC.topic] to level 1, they can answer this question!"
        else:
            "Ah poop sorry bud."
            "Because the player hasn't studied [topicC.topic] to level 1, they cant give advice."
            "So, for the next time the guest visits, they should try and level up their knowledge in [topicC.topic]!"
        return
