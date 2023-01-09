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
# avec une fonction pour dessiner des escaliers
def escalier (taille,nb):
    for i in range(0, nb):
        t.forward(taille)
        t.left(90)
        t.forward(taille)
        t.right(90)
        #on peut à chaque tour diminuer la taile de marche de l'escalier
        taille-=5
    t.forward(taille)

#pour dessiner un carré
def carre(taille):
    for i in range(0,taille):
        t.forward(50)
        t.right(90)


#escalier(30,5)
carre(4)
turtle.done()



