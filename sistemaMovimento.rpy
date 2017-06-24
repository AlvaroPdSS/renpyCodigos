# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define naomi = Character("Naomi", image = "naomi")
define takeshi = Character("Takeshi")
image bg sala = "images/sala.png"
image bg corredor = "images/corredor.png"
image bg patio = "images/patio.png"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene black
    centered "{size=+20}Sistema de Movimento Por Kleber Lucas{/size}"
    scene bg corredor:
        zoom 1.5


    show naomi normal
    with dissolve

    naomi "Hey Takeshi!!!"
    naomi "Vamos logo para a sala de aula!"
    hide naomi
    with dissolve
    "Naomi vai a sala primeiro"
    takeshi "Por que ela sempre pega no meu pé!?"

    call screen corredor
    if _return == "sala":
        jump sala
    elif _return == "patio":
        jump patio


    return

label sala:
    hide bg corredor
    scene bg sala:
        zoom 1.5
    with dissolve

    show naomi feliz
    naomi "Ainda bem que veio!"
    return

label patio:
    hide bg corredor
    scene bg patio:
        zoom 1.5
    with dissolve
    takeshi "Não aguento mais estudar!"
    return

screen corredor:
    imagemap:
        ground "images/ground.png"
        hover "images/hover.png"

        hotspot(766, 379, 62, 55) action Return("sala")
        hotspot(22, 424, 71, 58) action Return("patio")
