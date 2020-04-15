$ import variables as var

screen showAP:
    frame:
            xpadding 10
            ypadding 10
            xalign 0.5
            yalign 0.5
            xpos 220
            ypos 100
            text "AP = [AP]"

screen dateIntScreen(girlChosen):
    python:
        for x in dates:
            if girlChosen == x.ID:
                dateObject = x #ive made a variable to store the girl chosen - so we can get their date object and thus stats

    modal True
    frame:
        xpadding 10
        ypadding 10
        xalign 0.5
        yalign 0.5
        ypos 600
        xysize(245,50)
        hbox:
            textbutton "Talk":
                action Call("dateTalk",dateObject)
            textbutton "Gift":
                action Call("dateGift",dateObject)
            textbutton "Date":
                action Call("dateDate",dateObject) #wow great name i know
            textbutton "Back":
                action Call("interactChoose")


# example use:

label dateInteraction:
    $ AP = 5
    show screen showAP
    "The only way to interact with the dating options is after doing host club."
    "The player can choose who to interact with."
    "They have 5 AP. AP stands for action points."
    "The player can have 5 interactions with all the dating options with these AP."
    "Once the AP runs out, the day is over."
    "Let's try it out!"
    call interactChoose from _call_interactChoose
    return

label interactChoose:
    "Who do you want to talk to?"
    menu:
        "Hina":
            call sampleInteraction(2) from _call_sampleInteraction#pass in girls id as parameter - so as hina's id is 2, passed in 2!
        "Kaoru":
            call sampleInteraction(1) from _call_sampleInteraction_1
        "Tomoe":
            call sampleInteraction(3) from _call_sampleInteraction_2
        "Go home":
            "Are you sure you want to go home? This will end the day."
            menu:
                "Yes":
                    pass
                "No":
                    jump interactChoose

    return

label sampleInteraction(girlID):
    if AP >0:
        call screen dateIntScreen(girlID)
    else:
        "You have no more AP..."
        "It's time to go home."
        call endDay from _call_endDay
        return
    return

label dateDate(x):
    $ bpRequired = (x.datesDone * 10) * 1.5 #requirements for dates are subjected to change
    if x.bp >= bpRequired and not dateOrganised:
        "Do you want to organise a date?"
        "If you make a date now, you will not be able to make any other dates throughout the week."
        menu:
            "Yes":
                $ x.datesDone += 1
                $ dateOrganised = True
                $ AP -= 1
            "No":
                pass
    elif dateOrganised:
        "You already have a date organised this week."
    else:
        "You aren't close enough to ask for a date..."
    call sampleInteraction(x.ID) from _call_sampleInteraction_3

    return

label dateGift(x):
    if len(inventory.gift) >0 and x.giftCounter <= 3: #and x.datesDone >= 5: #if player has gifts in their inventory AND
    #has done 5 dates AND has not yet given the girl 3 gifts in that week, they can give gifts!
        $ x.giftCounter += 1 #giftCounter goes up by 1 for that girl
        $ AP -= 1 #and you lose AP
        call screen giftscreenDate
        $giftChosen = _return
        if giftChosen in x.giftSpecial:
            "very likey"
            $ x.bp += 8 #if your date likes the gift, you get bp!
        elif giftChosen in x.giftGood:
            "likey"
            $ x.bp += 5
        elif giftChosen in x.giftTrash:
            "EW"
            $ x.bp -= 1
        else:
            "um thanks ig???"
            $ x.bp += 2
    elif x.giftCounter > 3:
        "Haven't you given me enough gifts this week????"
        "You can't give any more gifts."
    else:
        "You can't give gifts at this point..."
        "You should try getting closer or filling up your inventory!"
    call sampleInteraction(x.ID) from _call_sampleInteraction_4
    return

label dateTalk(x):
    "Choose a topic to talk about."
    $ skipIF = False
    call screen convo
    $ selectedTopic = _return #storing the variable returned from screen
    while selectedTopic.ID not in x.convoCounter:
        $ AP -= 1 #you lose AP
        if selectedTopic.ID in x.convoPref:
            "She likes it!"
            $ x.bp += 2 * (selectedTopic.rarity + 1) * (selectedTopic.level + 1) #when you know more about a topic and it is a rare topic with
            #too, you will earn more bp!
            $ x.convoCounter.append(selectedTopic.ID) #it will be stored that you have talked about the topic already that week
            $ skipIF = True #prevents next if statement showing
        else:
            "She doesn't like it!"
            $ x.convoCounter.append(selectedTopic.ID) #it will be stored that you have talked about the topic already that week
            $ skipIF = True
    if selectedTopic.ID in x.convoCounter and not skipIF:
        "It seems that you have already talked about that this week..."
        if selectedTopic.ID in x.convoPref:
            "But she still liked it so you talk!"
            $ x.bp += 1 #only get a small boost if you have already talked to a girl on that topic that week
    call sampleInteraction(x.ID) from _call_sampleInteraction_5
    return
