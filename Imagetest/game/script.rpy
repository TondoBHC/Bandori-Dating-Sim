# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define t = Character("placeholder")


# The game starts here.

label start:


    show tomoe - happy
    t "this is tomoe's sprite"
    hide tomoe - happy
    show arisaSummerGrin
    t "this is arisa's sprite"
    hide arisaSummerGrin
    show hinaIdle1
    t "this is hina's sprite"
    hide hinaIdle1
    show tae_angry
    t "this is tae's sprite"
    hide tae_angry
    t "this is sayo's sprite"
    show summer uniform - angry 3
    # This ends the game.

    return
