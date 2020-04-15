# The script of the game goes in this file.

# The game starts here.


define e = Character("eileen")

label start:
    $renpy.notify("Hello")
    show screen  top_ui
    scene park
    show annoyed at l
    show sayo at r
    a "hello world"
    menu:
        "yestkjlrkfgklgbk;ldgtld;lfg":
            a "yes"
        "no":
            a "no?"
        "3":
            a "3"
        "4":
            a "4"
        "5":
            a "5"
    call map from _call_map_3
    return

label endDay:
    return
