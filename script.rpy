# The script of the game goes in this file.

init python:
    def max_points(*values):
        return [ i for i, v in enumerate(values) if v == max(values) ]

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define e = Character("Eileen")

define k = Character("Kaoru")
define t = Character("Tomoe")
define h = Character("Hina")

# The game starts here.

label start:
    $ k_points = 0
    $ t_points = 0
    $ h_points = 0
    # $ persistent.bond = 'Random' # reload persistent
    scene bg room
    show eileen happy
    e "testing to define main menu bg UI, based on player's choices"
    e "first choice"
    call bondmenu
    e "second choice"
    call bondmenu
    e "third choice"
    call bondmenu
    e "points so far are: \n Kaoru: [k_points] \n Tomoe: [t_points] \n Hina: [h_points]"
    e "max bond value is: [max_bond]"
    e "persistent value is: [persistent.bond]"
    e "save now"
    return

label bondmenu:
    menu:
        "Who do you want tho bond to?"
        "Bond with Kaoru":
            $ k_points += 1
            k "Thank you little kitten"
            call high_points
        "Bond with Tomoe":
            $ t_points += 1
            t "Oh! Nice! thanks!"
            call high_points
        "Bond with Hina":
            $ h_points += 1
            h "Boopin!"
            call high_points
    return

label high_points:
    $ max_bond = max_points(k_points, t_points, h_points)
    if max_bond == [0]:             # Kaoru
        $ persistent.bond = 'Kaoru'
    elif max_bond == [1]:           # Tomoe
        $ persistent.bond = 'Tomoe'
    elif max_bond == [2]:           # Hina
        $ persistent.bond = 'Hina'
    else:                           # Neither
        $ persistent.bond = 'Random'
    $ renpy.save_persistent()
return
