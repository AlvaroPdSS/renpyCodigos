init python:
    if(persistent.cap1 == None):
        persistent.cap1 = True
    if(persistent.cap2 == None):
        persistent.cap2 = False
    if(persistent.cap3 == None):
        persistent.cap3 = False


define naomi = Character("Naomi", image="menina")


label start:

    call screen capitulos

    return

label capitulo1:
    show menina

    naomi normal "Este é o capitulo 1"

    naomi "Falará sobre o inicio"
    naomi "é o fim do Capitulo 1"
    $persistent.cap2 = True
    return

label capitulo2:
    show menina feliz

    naomi "Este é o capitulo 2"
    naomi "Falará sobre um grande mistério!"
    naomi "Fim do capitulo 2"
    $persistent.cap3 = True
    return

label capitulo3:
    show menina feliz

    naomi "Este é o ultimo capitulo e grande final!"
    naomi "Contará sobre o herói que salva a princesa"
    naomi "É o fim do ultimo capitulo"

    return


screen capitulos:
    add "images/background.png"
    imagemap:
        ground "images/capitulos idle.png"
        hover "images/capitulos hover.png"

        hotspot(33,58,359,151) action Jump("capitulo1")
        if(persistent.cap2 == True):
            hotspot(450,63,360,145) action Jump("capitulo2")
        if(persistent.cap3 == True):
            hotspot(874,60,360,148) action Jump("capitulo3")
