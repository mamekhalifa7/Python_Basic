
nom=input("quel est votre nom ? ")

#CONVERSION D'UNE CHAINE EN ENTIER

#GESTION DES ERREURS
age_prochain=0
while age_prochain == 0:
    age = input("quel est votre age ? ")
    try:
    #en convertissant aussi on peut mettre
    #age=int(input("quel est votre age  f"))
        age_prochain= int(age)+1
    except ValueError:
        print("ERREUR: vous devez entrer un nombre")
else:
    print(f"vous vous appelez {nom} et vous avez {age} ans")
    print("l'annee prochaine vous aurez "+str(age_prochain)+" ans")
    print("MERCI")