
def demander_nom():
    nom=""
    while nom == "":
        try:
            nom = input("quel est votre nom ? ")
        except:
            print("ERROR :le nom ne doit pas etre vide")
    return nom


def demander_age():
    # CONVERSION D'UNE CHAINE EN ENTIER
    # GESTION DES ERREURS
    age=0
    while age== 0:
        age = input("quel est votre age ? ")
        try:
            # en convertissant aussi on peut mettre
            # age=int(input("quel est votre age  f"))
            age= int(age)
        except ValueError:
            print("ERREUR: vous devez entrer un nombre pour l'age")
    return age


#Appel des fonctions
nom=demander_nom()
age=demander_age()

print(f"vous vous appelez {nom} et vous avez {age} ans")
print("l'annee prochaine vous aurez "+str(age+1)+" ans")
print("MERCI")