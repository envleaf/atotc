# currently this is mostly placeholder code left in by Ren'Py
# Nearly all code for this game is stored in individual files in the 'code' directory. This file is used purely as an index and calls functions from these other files. This feels wrong but idk any better ways of going about this when trying to keep dialouge organized so if you are a better programmer than me please tell me how to go about this better lmao

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
