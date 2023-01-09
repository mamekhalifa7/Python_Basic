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
    for i in range(0,4):
        t.forward(taille)
        t.right(90)

#plusiers carres
def carres (tailledepart,nb):
    for i in range(0,nb):
        taille=(i+1)*tailledepart
        carre(taille)


#escalier(30,5)
#carre(100)
carres(10,10)
turtle.done()



