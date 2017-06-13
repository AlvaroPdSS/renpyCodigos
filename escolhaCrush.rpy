init python:
    crush = ""

define naomi = Character("Naomi", image="naomi")
define yoko = Character("Yoko", image="yoko")
define alicia = Character("Alicia", image="alicia")
define narumi = Character("Narumi", image="narumi")
define takeshi = Character("Takeshi")
image bg cidade = "bg/cidade.png"
image bg corredor = "bg/corredor.png"
image bg rua = "bg/rua.png"
image bg quarto = "bg/quarto.png"


# The game starts here.

label start:
    call screen escolhaCrush
    python:
        crush = _return
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg quarto at center:
        xzoom 1.25


    takeshi "Hoje tive vários pesadelos sobre aquele acontecimento..."
    takeshi "Será que ele liga a mim de alguma forma?"

    takeshi "Bom preciso ir a um lugar para esquecer disto!"

    takeshi "Eu posso ir a cidade encontrar minha namorada a [crush], ou ir para a escola ver se a professora está lá. Ou até mesmo andar na rua..."

    call screen escolhaLocal
    if _return == "cidade":
        jump cidade
    elif _return == "rua":
        jump rua
    else:
        jump corredor

    # These display lines of dialogue.





    return

label cidade:
    hide bg
    show bg cidade:
        xzoom 1.25
    with dissolve
    if crush == "Alicia":
        jump alicia
    elif crush == "Naomi":
        jump naomi
    elif crush == "Narumi":
        jump narumi
    else:
        jump yoko

label alicia:
    show alicia nervosa at center:
        zoom 0.7
    alicia "Por que demorou tanto!?"
    alicia "Pensei que não viria!"
    alicia normal "Bom vamos logo, quero passar em umas lojas!"
    return

label narumi:
    show narumi feliz at center:
        zoom 0.7
    narumi "Que bom que veio, estava te esperando!"
    narumi "Que filme veremos hoje?"
    return

label naomi:
    show naomi preocupada at center:
        zoom 0.7
    naomi "Nossa, eu já estava ficando preocupada!"
    takeshi "Só acordei tarde, me desculpa"
    naomi feliz "Tudo bem! Eu fiquei aproveitando e vendo aquele artista de rua cantar!"
    return

label yoko:
    show yoko sorriso at center:
        zoom 0.7
    yoko "Você está bonito hoje!"
    takeshi "O...obrigado!"
    yoko "Não precisa ficar tímido!"
    yoko feliz "Vamos!"
    return

label rua:
    hide bg
    show bg rua:
        xzoom 1.25
    with dissolve

    takeshi "Como é bom respirar!"
    return



label corredor:
    hide bg
    show bg corredor:
        xzoom 1.25
    with dissolve

    takeshi "É..."
    takeshi "Acho que a professora não está aqui"
    return


screen escolhaCrush:
    imagemap:
        ground "images/ground.png"
        hover "images/hover.png"

        hotspot(14,118, 283, 598) action Return("Alicia")
        hotspot(302,141, 286, 576) action Return("Naomi")
        hotspot(603, 130, 360, 588) action Return("Narumi")
        hotspot(961, 129, 311, 589) action Return ("Yoko")
