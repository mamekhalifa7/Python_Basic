import turtle

t = turtle.Turtle()
"""
for i in range (1,5):
    t.forward(30)
    t.left(90)
    t.forward(30)
    t.right(90)
t.forward(30)
"""
# avec une fonction
def escalier (taille,nb):
    for i in range(0, nb):
        t.forward(taille)
        t.left(90)
        t.forward(taille)
        t.right(90)
    t.forward(taille)

escalier(30,5)

turtle.done()



