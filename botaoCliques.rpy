
init python:
    botao = 0


define e = Character("eileen", color="#e3e3e3")
define a = Character("Angela", color="#f00")
label start:



    scene black



    centered "Clique 10 vezes o botão!"

    centered "Lá vai!"
    show screen button
    while botao < 10:
        "Clique no botão 10 vezes!"
    hide screen button
    if botao >= 10:
        centered "é acho que deu certo!"



    return



screen button:

    textbutton "Clique [botao] vezes" clicked SetVariable("botao", botao+1)align (.95,.04)
    if botao == 9:
        textbutton "Clique [botao] vezes" clicked [SetVariable("botao", botao+1), Return("foi")] align (.95,.04)
