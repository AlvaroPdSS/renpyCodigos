init python:
    horas = 9
    minutos = 15


define n = Character("Naomi", image="naomi")

image bg patio = "images/patio.png"
image bg sala = "images/sala.png"
image bg corredor = "images/corredor.png"



label start:


    show screen relogio
    jump corredor





    return

label corredor:
    if(not(horas == 9 and minutos == 15)):
        $minutos += 15
        if(minutos > 59):
            $minutos = minutos-60
            $horas += 1
            if(horas > 23):
                $horas = horas - 24




    scene bg corredor:
        zoom 1.3

    show naomi normal

    n "Bem vindo ao sistema de relógio"
    menu:
        "Ir a sala":
            jump sala
        "Ir ao pátio":
            jump patio

label sala:
    $minutos += 15
    if(minutos > 59):
        $minutos = minutos-60
        $horas += 1
        if(horas > 23):
            $horas = horas - 24

    scene bg sala:
        zoom 1.3
    show naomi
    n feliz "Que legal você veio a sala!"

    menu:
        "Ir a corredor":
            jump corredor
        "Ir ao pátio":
            jump patio


label patio:
    $minutos += 43
    if(minutos > 59):
        $minutos = minutos-60
        $horas += 1
        if(horas > 23):
            $horas = horas - 24
    scene bg patio:
        zoom 1.3
    show naomi
    n feliz "O pátio é tão calmo!"
    menu:
        "Ir a corredor":
            jump corredor
        "Ir ao sala":
            jump sala

screen relogio:
    text "{color=#ff0}{size=+20}[horas] : [minutos]{/size}{/color}" xalign 0.02 yalign 0.05
