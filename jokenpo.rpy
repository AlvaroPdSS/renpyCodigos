init python:
    from random import randint
    mao = ""

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define naomi = Character("Naomi", image = "naomi")
image bg patio = "images/patio.png"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg patio:
        zoom 1.5

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show naomi normal

    naomi "Vamos jogar pedra-papel-tesoura?"

    python:
        sorteio = randint(1,3)

    if sorteio == 1:
        $mao = "pedra"
    elif sorteio == 2:
        $mao = "papel"
    else:
        $mao = "tesoura"
    menu:
        "Pedra":

            "Naomi mostrou : [mao]"
            if sorteio == 1:
                naomi "Empate!"
            elif sorteio == 2:
                naomi "Você perdeu"
            else:
                naomi "Você venceu"
        "Papel":
            "Naomi mostrou : [mao]"
            if sorteio == 1:
                naomi "Você venceu"
            elif sorteio == 2:
                naomi "Empate!"
            else:
                naomi "Você perdeu"
        "Tesoura":
            "Naomi mostrou : [mao]"
            if sorteio == 1:
                naomi "Você perdeu"
            elif sorteio == 2:
                naomi "Você venceu"
            else:
                naomi "Empate!"




    # This ends the game.

    return
