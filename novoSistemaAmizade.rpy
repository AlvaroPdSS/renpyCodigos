# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
init python:
    # variáveis globais, serão alteradas dinamicamente
    yokoAmizade = 0
    aliceAmizade = 0
    pontoAnterior = 0


define a = Character("Alice", image = "alice", color="#f00")
define y = Character("Yoko", image="yoko")
image bg room = "images/room.png"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    $ contador = 0
    scene bg room:
        zoom 1.5
    show alice feliz
    a "Olá seja bem vindo, este é o sistema de Amizade por barra!"
    menu:
        "Chamar ela de linda":
            centered "{size=+10}Você ganhou {color=#f00}15{/color} pontos de amizade com Alice{/size}"
            python:
                aliceAmizade += 15
            call chamarBarraMais(aliceAmizade)
        "Dar um presente":
            centered "{size=+10}Você ganhou {color=#f00}20{/color} pontos de amizade com Alice{/size}"
            python:
                aliceAmizade += 20
            call chamarBarraMais(aliceAmizade)

    menu:
        "Chamá-la para sair":
            centered "{size=+10}Você ganhou {color=#f00}15{/color} pontos de amizade com Alice{/size}"
            python:
                aliceAmizade += 15
            call chamarBarraMais(aliceAmizade)
        "Xingá-la":
            centered "{size=+10}Você perdeu {color=#f00}10{/color} pontos de amizade com Alice{/size}"
            python:
                aliceAmizade -= 10
            call chamarBarraMenos(aliceAmizade)


    a "testando barra"
    a "Agora ela sumiu!"

    # This ends the game.

    return

label chamarBarraMais(valorBarra):
    $pontoAnterior = valorBarra
    while contador < valorBarra:
        $contador += 1
        show screen barraAmizade(contador)
        pause 0.001
    $renpy.pause(2)
    hide screen barraAmizade
    return

label chamarBarraMenos(valorBarra):
    if valorBarra > 100:
        $valorBarra = 100
    if(valorBarra < pontoAnterior):
        $contador = pontoAnterior
        while contador > valorBarra:
            $contador -= 1
            show screen barraAmizade(contador)
            pause 0.001
        $renpy.pause(1)
        hide screen barraPontos

    elif(valorBarra > pontoAnterior):
        $contador = pontoAnterior
        while contador < valorBarra:
            $contador += 1
            show screen barraAmizade(contador)
            pause 0.001
        $renpy.pause(2)
        hide screen barraPontos
    return

screen barraAmizade(amizade):
    frame:
        hbox:
            spacing 20
            vbox:
                spacing 10
                text "Amizade"

                $ ui.vbar(100, amizade, xmaximum=5, ymaximum=200, top_bar=Frame("images/topt.png", 25, 25), bottom_bar=Frame("images/bottomt.png", 25, 25), xalign=0.5, yalign=0.5)
