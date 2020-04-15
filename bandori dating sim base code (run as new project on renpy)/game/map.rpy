$ import variables as var


screen map():
    modal True
    imagemap:
        hbox:
            imagebutton auto "gui/planner_%s.png" xpos 1100 ypos 600 action ToggleScreen("Planner",dissolve)#show screen planner
            imagebutton auto "gui/gift_%s.png" xpos 825 ypos 600 action ToggleScreen("giftInv",dissolve)#show inv

        hbox:
            frame:
                background "gui/datebar.png"
                xpos 50
                ypos 32
                vbox:
                    text "Sep 20, Afternoon" size 20 text_align 0.5
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
    tag Plan
    modal True
    add "gui/stats.png"
    hbox:
        imagebutton auto "gui/map_%s.png" xpos 1100 ypos 600 action Hide("Plan")#back to map
    hbox:
        xalign 1
        ypos 85
        imagebutton auto "gui/buttonL_%s.png" action ToggleScreen("Planner")
    vpgrid:
        #grid define + spacing
        cols 2
        spacing 20
        ypos 240
        xpos 795
        for i in convos:
                text "[i.topic]: [i.level]"
    vpgrid:
        #grid define + spacing
        cols 2
        spacing 20
        ypos 515
        xpos 815
        for i in dates:
                text "[i.name]:[i.bp]"
    vpgrid:
        #grid define + spacing
        cols 1
        ypos 240
        xpos 240
        vbox:
            spacing 20
            text "Host Club Points: [hostPoints]"
            text "Study Points: [studyPoints]"
            text "Grade: [schoolPoints]"

screen Planner():
    tag Plan
    modal True
    add "gui/plannerSept.png"
    hbox:
        imagebutton auto "gui/map_%s.png" xpos 1100 ypos 600 action Hide("Plan")#back to map
    hbox:
        xalign 0.99
        ypos 85
        imagebutton auto "gui/buttonR_%s.png" action ToggleScreen("Stats")
    hbox:
        xpos 200
        ypos 160
        add "gui/test.png"


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
