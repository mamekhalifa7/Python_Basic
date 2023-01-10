
import random

NB_MIN=1
NB_MAX=10

def poser_question():
    a=random.randint(NB_MIN,NB_MAX)
    b=random.randint(NB_MIN,NB_MAX)
    rep_str=input(f"calculer {a} + {b} = ")
    rep_int=int(rep_str)
    if rep_int==a+b:
        print("Bravo! Reponse correcte")
    else:
        print("Reponse incorrecte")

poser_question()