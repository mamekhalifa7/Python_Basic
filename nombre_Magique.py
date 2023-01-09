def nombre_magique(min,max):
    nbre=input(f"entrer le nombre magique entre {min} et {max} ")
    nbre_int=int(nbre)
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