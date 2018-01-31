define n = Character("Naomi", image="naomi")
define y = Character("Yumi", image="yumi")

image side naomi normal = im.Scale("images/naomi normal.png", 600, 450, xoffset=-200, yoffset=100)
image side yumi normal = im.Scale("images/yumi normal.png", 600, 450, xoffset=-200, yoffset=100)
label start:
    show naomi at left
    
    n normal "Oi tudo bem?"

    show yumi at right
    y normal "Tudo bem, e você?"

    return
