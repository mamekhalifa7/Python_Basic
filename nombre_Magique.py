
import random
def nombre_magique(min,max):
    nbre_int=0
    while nbre_int==0:
        nbre=input(f"entrer le nombre magique entre {min} et {max} ")
        try:
            nbre_int=int(nbre)
        except:
            print("ERROR: vous devez entrer un nombre ")
        else:
            if nbre_int<min or nbre_int>max:
                print(f" ERROR: le nombre doit etre compris entre{min} et {max} ")
                nbre_int=0
    return nbre_int


nmin=1
nmax=10
#nmag=5
#on peut aussi choisir le nbre magique aléatoirement
#pour choisir le nombre magique aléatoirement
#il faut importer d'abord random
#ensuit random.randint permet de definir la aleatoirement
#le nbre magique entre une intervalle
nmag=random.randint(nmin,nmax)
essaie=3
nombre=0
nbre_essaie=essaie
while not nombre==nmag and nbre_essaie >0:
    print(f'il vous reste {nbre_essaie} essaies')
    nombre=nombre_magique(nmin,nmax)
    if nombre>nmag:
        print("le nombre magique est plus petit")
        nbre_essaie-=1
    elif nombre<nmag:
        print("le nombre magique est plus grand")
        nbre_essaie-=1
    else:
        print("Bravo ! vous avez gagné")
if nbre_essaie==0:
    print(f"Vous avez perdu : le nombre magique etait: {nmag}")
