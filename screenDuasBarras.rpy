screen barraAmizade(amizade):
    #frame caso queira fundo preto, caso fundo transparente é só tirar o "frame:"
    frame:
        #hbox para que os dois vbox fiquem um do lado do outro
        hbox: 
            #espaço entre as barras
            spacing 20
            vbox:
                #espaço entre o texto "amizade" e a barra
                spacing 10
                text "Amizade"

                $ ui.vbar(100, amizade, xmaximum=5, ymaximum=200, top_bar=Frame("images/topt.png", 25, 25), bottom_bar=Frame("images/bottomt.png", 25, 25), xalign=0.5, yalign=0.5)
            #segunda barra
            vbox:
                spacing 10
                text "Amor"
                $ ui.vbar(100, 20, xmaximum=5, ymaximum=200, top_bar=Frame("images/topt.png", 25, 25), bottom_bar=Frame("images/bottomt.png", 25, 25), xalign=0.5, yalign=0.5)
