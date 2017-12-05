init python:
    class Protagonista:
        def __init__(self, genero, nome):
            self.genero = genero
            self.nome = nome

            if genero == "Masculino":
                self.artigo = "o"
            elif genero == "Feminino":
                self.artigo = "a"


define n = Character("Naomi")


# The game starts here.

label start:
    scene black

    menu escolherGenero:
        "Qual é seu sexo?"
        "Masculino":
            $sexo = "Masculino"
            $nome = renpy.input("Qual é o seu nome?")
            $Protagonista = Protagonista(sexo, nome)
        "Feminino":
            $sexo = "Feminino"
            $nome = renpy.input("Qual é o seu nome?")
            $Protagonista = Protagonista(sexo, nome)



    show naomi feliz at center:
        zoom 0.8

    n "Você é [Protagonista.artigo] [Protagonista.nome]"

    if Protagonista.genero == "Masculino":
        n "Você é menino"
    else:
        n "Você é menina"

    # This ends the game.

    return
