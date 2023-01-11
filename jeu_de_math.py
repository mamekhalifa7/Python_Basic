
import random
def user_name():
    nom=""
    while nom=="":
        nom=input("Renseigner d'abord votre nom ")
    return nom

NB_MIN=1
NB_MAX=10
NB_QUESTION=4
def poser_question():

    a=random.randint(NB_MIN,NB_MAX)
    b=random.randint(NB_MIN,NB_MAX)
    o=random.randint(0,2)
    if o == 0:
        operateur_str = "+"
    elif o == 1:
        operateur_str="*"
    else:
        operateur_str="/"

    rep_str=input(f"calculer {a} {operateur_str} {b} = ")
    rep_int=int(rep_str)
    if o==0:
        calcul = a + b
    elif o == 1:
        calcul = a * b
    else:
        calcul = a / b
    if rep_int==calcul:
        return True
        #print("Bravo! Reponse correcte")
    #else:
        #print("Reponse incorrecte")
    return False

player = user_name()
#on va essayer de poser plusier questions
#calculer le nombre de point obtenu par le player
nb_point=0
for i in range(0,NB_QUESTION):
    print(f"Question n°{i} sur {NB_QUESTION}")
    if poser_question():
        print("Reponse correcte")
        nb_point+=1
    else:
        print("Reponse incorrecte")

print(f"{player} Votre score est de: {nb_point} / {NB_QUESTION}")
moyenne=int(NB_QUESTION)/2
if nb_point==NB_QUESTION:
    print(f"Excellent !!! {player}")
elif nb_point==0:
    print(f"Reviser vos leçons de math {player}")
elif nb_point > moyenne:
    print(f"pas mal {player}")
else:
    print(f"peut mieux faire {player}")
