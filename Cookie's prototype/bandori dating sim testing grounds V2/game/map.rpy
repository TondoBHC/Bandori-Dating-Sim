$ import variables as var

screen map():
    modal True
    imagemap:
        hbox:
            imagebutton auto "gui/planner_%s.png" xpos 1100 ypos 600 action ToggleScreen("Planner",dissolve)#show screen planner
            imagebutton auto "gui/gift_%s.png" xpos 825 ypos 600 action ToggleScreen("giftInv",dissolve)#show inv
            imagebutton auto "gui/stats_%s.png" xpos 550 ypos 600 action ToggleScreen("TopicsStat",dissolve)#show screen planner
            imagebutton auto "gui/save_%s.png" xpos 275 ypos 600 action ShowMenu('save') #open save menu
        hbox:
            frame:
                background "gui/datebar.png"
                xpos 50
                ypos 32
                vbox:
                    text "[weekdays[0]], [months[0]] [day], [time[0]]" size 17 text_align 0.5
                    ypos 15
                    xpos 15
        ground "images/map.png" xfill True yfill True
        #home
        hotspot (223, 159, 319, 199) clicked Confirm("This will end the day. Are you sure you want to go home?",Call("endDay"),NullAction())
        #school
        hotspot  (676, 382, 320, 202) clicked Call("School")
        #shop
        hotspot (673, 159, 321, 201) clicked Call("Shop")
        #job
        hotspot (226, 384, 317, 198) clicked Call("Job")

screen TopicsStat():
    tag Stats
    modal True #used so player cant click on anything outside the screen
    add "gui/overlay/confirm.png"
    frame:
        xpadding 10
        ypadding 10
        xalign 0.5
        yalign 0.5
        xysize(500,557)
        top_padding 45

        vbox:
            text "Topics"
            vbox:
                for i in convos:
                        text "[i.topic]: [i.level]":
                            xysize(450,20)
        imagebutton auto "gui/exit_%s.png":
            action ToggleScreen("Stats",dissolve)
            xalign 0.025
            yalign 0.5
            ypos -23
        hbox:
            xalign 0.5
            yalign 0.99
            imagebutton auto "gui/buttonL_%s.png" :
                action ToggleScreen("BondStats",dissolve)
            imagebutton auto "gui/buttonR_%s.png":
                action ToggleScreen("OtherStats",dissolve)

screen BondStats():
    tag Stats
    modal True #used so player cant click on anything outside the screen
    add "gui/overlay/confirm.png"

    frame:
        xpadding 10
        ypadding 10
        xalign 0.5
        yalign 0.5
        xysize(500,557)
        top_padding 45
        vbox:
            text "Bond Points"
            vbox:
                for i in dates:
                        text "[i.name]:[i.bp]":
                            xysize(450,20)
        imagebutton auto "gui/exit_%s.png":
            action ToggleScreen("Stats",dissolve)
            xalign 0.025
            yalign 0.5
            ypos -23
        hbox:
            xalign 0.5
            yalign 0.99
            imagebutton auto "gui/buttonL_%s.png" :
                action ToggleScreen("OtherStats",dissolve)
            imagebutton auto "gui/buttonR_%s.png":
                action ToggleScreen("TopicsStat",dissolve)
screen OtherStats():
    tag Stats
    modal True #used so player cant click on anything outside the screen
    add "gui/overlay/confirm.png"
    frame:
        xpadding 10
        ypadding 10
        xalign 0.5
        yalign 0.5
        xysize(500,557)
        top_padding 45
        vbox:
            text "School and Host Club"
            vbox:
                text "Host Club Points: [hostPoints]"
                text "Study Points: [studyPoints]"
                text "Grade: [schoolPoints]"
                text "Money: [inventory.money]"
                text "Candy: [persistent.candy]"
        imagebutton auto "gui/exit_%s.png":
            action ToggleScreen("Stats",dissolve)
            xalign 0.025
            yalign 0.5
            ypos -23
        hbox:
            xalign 0.5
            yalign 0.99
            imagebutton auto "gui/buttonL_%s.png" :
                action ToggleScreen("TopicsStat",dissolve)
            imagebutton auto "gui/buttonR_%s.png":
                action ToggleScreen("BondStats",dissolve)

screen Planner():
    tag Plan
    modal True
    add "gui/overlay/confirm.png"
    frame:
        xpadding 10
        ypadding 10
        xalign 0.5
        yalign 0.5
        xsize(1200)
        add "gui/calender.png" xalign 0.5
    if testOn:
        add "gui/test.png" pos(900, 335)#test
    if dateOrganised:
        add "gui/date.png" pos(140, 335)#date
    imagebutton auto "gui/exit_%s.png":
        action ToggleScreen("Planner",dissolve)
        xalign 0.045
        yalign 0.5
        ypos 280

label map():
    window hide
    $ _skipping = False
    call screen map
    return

label School():
    $ _skipping = True
    scene class
    if time[0] == "Morning":
        if day == 1:
            "We have a test this week."
            $ testOn = True
        if day == 5:
            "Test on."
            if studyPoints > 2:
                "I passed!"
            else:
                "I don't think I done well..."
        else:
            "It was a normal day of class."
        call advance()
        call map
    if time[0] == "Afternoon":
        "Welcome to school."
        menu:
            "Study.":
                scene library
                "Welcome to the library"
                call library from _call_library
            "Host club":
                scene hostclub
                "Welcome to the host club."
                call hostClub from _call_hostClub
                return
            "Back to map.":
                call map from _call_map
    return

label Shop():
    $ _skipping = True
    scene store
    "Welcome to the shop."
    menu:
        "Buy gifts.":
            $ buying = True
            while buying:
                call screen giftscreenBuy
                call buy(_return) from _call_buy
                "Do you want to buy more?"
                menu:
                    "Yes":
                        pass
                    "No":
                        $ buying = False
            call map from _call_map_1

        "Back to map.":
            call map from _call_map_2
    return
