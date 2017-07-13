init python:
    senhaCerta = "555"
    senhaDigitada = ""

define e = Character("Eileen")
image bg = "images/bg.png"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg
    while senhaDigitada != senhaCerta:
        python:
            senhaDigitada = renpy.input("Digite a senha para abrir o baú!")
        if senhaDigitada != senhaCerta:
            "Você errou a senha!"

    "Você abriu o baú"
    centered "{color=#f00}No baú tinha 100 mil reais!{/color}"






    return
