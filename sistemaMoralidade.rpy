
init python:
    moralidade = 0

define naomi = Character("Naomi", image="naomi")
image bg = "bg centro.png"


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg:
        xzoom 1.6
        yzoom 1.2

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    show naomi normal at center:
        zoom 1.3
    # These display lines of dialogue.

    "Olá Seja bem vindo ao sistema de Moralidade"

    naomi "O que faria se avistar um mendigo sendo agredido na rua?"
    menu:
        "Eu ajudaria-o!":
            $moralidade += 1
        "Não é problema meu!":
            $moralidade -= 1

    naomi "Você ajudaria uma pessoa estranha?"
    menu:
        "Eu não":
            $moralidade -=1
        "Claro que sim!":
            $moralidade +=1


    if moralidade == 2:
        naomi feliz "Você é uma boa pessoa!"
    elif moralidade == 0:
        naomi neutra "Você é normal!"
    else:
        naomi nervosa "Credo!"
        naomi "Você já ouviu falar em empatia!?"

    # This ends the game.

    return
