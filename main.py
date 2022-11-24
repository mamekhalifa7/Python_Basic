
nom=input("quel est votre nom ")
age=input("quel est votre age ")
#CONVERSION D'UNE CHAINE EN ENTIER

#GESTION DES ERREURS
try:
    age_prochain= int(age)+1
except:
    print("ERREUR: vous devez entrer un nombre")
else:
    print(f"vous vous appelez {nom} et vous avez {age} ans")
    print("l'annee prochaine vous aurez "+str(age_prochain)+" ans")
    print("MERCI")