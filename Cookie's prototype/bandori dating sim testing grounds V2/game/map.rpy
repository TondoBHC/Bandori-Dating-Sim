$ import variables as var

screen map():
    modal True
    imagemap:
        hbox:
            imagebutton auto "gui/planner_%s.png" xpos 1100 ypos 600 action ToggleScreen("Planner",dissolve)#show screen planner
            imagebutton auto "gui/gift_%s.png" xpos 825 ypos 600 action ToggleScreen("giftInv",dissolve)#show inv
            imagebutton auto "gui/stats_%s.png" xpos 550 ypos 600 action ToggleScreen("Stats",dissolve)#show screen planner
        hbox:
            frame:
                background "gui/datebar.png"
                xpos 50
                ypos 32
                vbox:
                    text "[months[0]] [day], [time[0]]" size 20 text_align 0.5
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

screen Stats():
    modal True #used so player cant click on anything outside the screen
    add "gui/overlay/confirm.png"

    frame:
        xalign 0.330
        ypos 50
        textbutton "Exit":
            action ToggleScreen("Stats",dissolve)

    frame:
        xpadding 10
        ypadding 10
        xalign 0.5
        yalign 0.5
        xysize(500,557)

        vbox:
            text "Topics"
            vpgrid:
                cols 2
                spacing 10
                for i in convos:
                        text "[i.topic]: [i.level]"
            text ""
            text "Bond Points"
            vpgrid:
                cols 2
                spacing 10
                for i in dates:
                        text "[i.name]:[i.bp]"
            text ""
            text "School and Host Club"
            vbox:
                spacing 10
                text "Host Club Points: [hostPoints]"
                text "Study Points: [studyPoints]"
                text "Grade: [schoolPoints]"

screen Planner():
    tag Plan
    modal True
    add "gui/overlay/confirm.png"
    frame:
        xalign 0.1
        ypos 220
        textbutton "Exit":
            action ToggleScreen("Planner",dissolve)

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




label map():
    call screen map
    return

label School():
    scene class
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
