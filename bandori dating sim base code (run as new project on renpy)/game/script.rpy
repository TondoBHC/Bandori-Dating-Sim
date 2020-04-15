# The script of the game goes in this file.

# The game starts here.

$ import variables as var

label start:
    show screen top_ui
    "Which pronouns do you prefer using?"
    menu:
        "They/Them":
            $ pronoun = theyThem
        "He/Him":
            $ pronoun = heHim
        "She/Her":
            $ pronoun = sheHer
    label nameplayer:
        "What name would you like to go by?"
        $ first_name = renpy.input("First name")
        $ first_name = first_name.strip()
        $ last_name = renpy.input("Last name")
        $ last_name = last_name.strip()
        if (first_name == (("Jonathan") or ("Joseph") or ("Johnny")) and last_name == ("Joestar")) or (first_name == ("Jotaro") and last_name == ("Kujo")) or (first_name == ("Josuke") and last_name == ("Higashikata")) or (first_name == ("Jolyne") and last_name == ("Cujoh")):
            $ user = ("JoJo")
        elif first_name == ("Giorno") and last_name == ("Giovanna"):
            $ user = ("GioGio")
        else:
            $ user = Character("[first_name]")
        "So [fullName], is that right?"
        menu:
            "Yes, [fullName]":
                pass
                $persistent.playername = "[first_name] [last_name]"
            "No":
                "Well then, enter the correct one."
                call nameplayer

    #jump to the all script label - and thus the allscript.rpy file
    jump fd_allscript
return

# The script of the game goes in this file.

label endDay:
    return
