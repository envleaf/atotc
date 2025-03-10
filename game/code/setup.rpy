# this file is run at the begining of the game to define characters and get the mc's name
label setup:
    label setup.name:
        #prompt for name and store in $ name variable. 16 char limit.
        $ name = renpy.input("Please input your name! (No more than 16 characters.)", length=16)
        $ name = name.strip()
        menu confirm_name:
            "Your name is [name], yes?"

            "Yep!":
                jump setup.define

            "Nevermind, let me change it.":
                jump setup.name
    label setup.define:
    define l = Character("Luna")
    jump prologue1