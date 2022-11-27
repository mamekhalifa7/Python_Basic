def afficher(nom,age,taille=0):
#on peut aussi ajouter un parametre qui sera optionnel en l'initialisant
# dans ce cas quand on lappelle on aura besoin de l'appeler
#si on veut
    print("votre nom est : "+nom+" et vous avez "+str(age)+" ans l'an prochain vous aurez: "+str(age+1)+" ans")
    if age<18:
        print("vous etes mineur")
    else:
        print("vous etes majeur")
    if not taille== 0:
        print("vous mesurez "+str(taille))

def demander_nom():
    nom=""
    while nom == "":
        try:
            nom = input("quel est votre nom ? ")
        except:
            print("ERROR :le nom ne doit pas etre vide")
    return nom



#on peut aussi passer un parametre a notre fonction
def demander_age(name):
    # CONVERSION D'UNE CHAINE EN ENTIER
    # GESTION DES ERREURS
    age=0
    while age== 0:
        age = input(name+" quel est votre age ? ")
        try:
            # en convertissant aussi on peut mettre
            # age=int(input("quel est votre age  f"))
            age= int(age)
        except ValueError:
            print("ERREUR: vous devez entrer un nombre pour l'age")
    return age


#Appel des fonctions
#une fonction peut etre appeler plusieurs fois

"""
nom1=demander_nom()
nom2=demander_nom()
age1=demander_age(nom1)
age2=demander_age(nom2)

print(f"vous vous appelez {nom1.upper()} et vous avez {age1} ans")
print("l'annee prochaine vous aurez "+str(age1+1)+" ans")

print(f"vous vous appelez {nom2} et vous avez {age2} ans")
print("l'annee prochaine vous aurez "+str(age2+1)+" ans")
print("MERCI")
"""
for i in range(0,5):
    nom="personne "+str(i+1)
    age=demander_age(nom)
    afficher(nom,age,1.12)


