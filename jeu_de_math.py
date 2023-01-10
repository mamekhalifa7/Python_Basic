
import random

NB_MIN=1
NB_MAX=10
NB_QUESTION=4
def poser_question():

    a=random.randint(NB_MIN,NB_MAX)
    b=random.randint(NB_MIN,NB_MAX)
    rep_str=input(f"calculer {a} + {b} = ")
    rep_int=int(rep_str)
    if rep_int==a+b:
        return True
        #print("Bravo! Reponse correcte")
    #else:
        #print("Reponse incorrecte")
    return False

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

print(f"Votre score est de: {nb_point} / {NB_QUESTION}")
