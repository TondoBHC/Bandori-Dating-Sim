$ import variables as var

label Job():
    scene parttime
    "Welcome to your job."
    if not resumeGiven:
        "Working part time here is the only way to make gold in the game."
        "You must give in your resume to get hired."
        "Would you like to hand in your resume?"
        menu:
            "Yes":
                "You have given in your resume. Come back next day to earn the moneys."
                $ resumeGiven = True
            "No":
                call map from _call_map_4
    else:
        "Would you like to work today?"
        menu:
            "Yes":
                "You worked hard..."
                $ inventory.money += 10
                "You earned 10 gold!"
            "No":
                call map from _call_map_5


    return