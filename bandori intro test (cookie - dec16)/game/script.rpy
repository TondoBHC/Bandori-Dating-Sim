$ import variables as var


label start:


    menu:
        "Which pronouns do you prefer using?"
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
            "No":
                "Well then, enter the correct one."
                call nameplayer
        #if player name is equal to the old name...
        if  (persistent.playername == (fullName)) and (persistent.CompletedTimes > 0):
            "Have we met before?"
        #if player completed games more than once....
        elif persistent.completedTimes > 0:
            "Hmm we know someone that had the same name as you. weird."
        #first time
        else:
            "Have fun!"
    $persistent.completedTimes += 1
    $persistent.playername = "[fullName]"

    return
