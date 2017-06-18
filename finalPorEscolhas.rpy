init python:
    escolhasCertas = 0
    rotaNaomi = 0

define naomi = Character("Naomi", image = "naomi")
define takeshi = Character("Takeshi")
image bg sala = "images/sala.png"


# The game starts here.

label start:
    scene bg sala:
        zoom 1.5
    show naomi normal

    menu:
        "Qual é a capital do Brasil?"
        "São Paulo":
            python:
                escolhasCertas = 0
            naomi "Você errou!"

        "Rio de Janeiro":
            python:
                escolhasCertas = 0
            naomi "Você errou!"

        "Brasilia":
            python:
                escolhasCertas += 1
            naomi "Incrível você certou!"

    menu:
        "Qual é a capital dos EUA"
        "New York":
            python:
                escolhasCertas = 0
            naomi "Você errou!"
        "Washington":
            python:
                escolhasCertas += 1
            naomi "Incrível você certou!"

        "California":
            python:
                escolhasCertas = 0
            naomi "Você errou!"
    if escolhasCertas == 2:
        jump finalBom
    else:
        jump finalRuim


label finalBom:
    naomi feliz "Parabéns você ganhou!"
    return

label finalRuim:
    naomi "Infelizmente você perdeu!"
    return
