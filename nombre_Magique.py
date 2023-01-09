def nombre_magique(min,max):
    nbre_int=0
    while nbre_int==0:
        nbre=input(f"entrer le nombre magique entre {min} et {max} ")
        try:
            nbre_int=int(nbre)
        except:
            print("ERROR: vous devez entrer un nombre ")
    return nbre_int


nmin=1
nmax=10
nmag=5

nombre=0
while not nombre==nmag:
    nombre=nombre_magique(nmin,nmax)
    if nombre>nmag:
        print("le nombre magique est plus petit")
    elif nombre<nmag:
        print("le nombre magique est plus grand")
    else:
        print("Bravo ! vous avez gagné")