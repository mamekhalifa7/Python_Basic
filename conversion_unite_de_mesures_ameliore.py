
# Raisonnement simple sans fonction
"""
print(" Ce programme vous permet d'effectuer des conversions d'unité")
print("1 - pouces vers cm")
print("2 - cm vers pouces")
choice = input("votre choix (1 ou 2): ")
if choice=="1":
    valeur_str= input(" conversion pouces vers cm. Donnez la valeur en pouces : ")
    valeur_float = float(valeur_str)
    valeur_convertie = round(valeur_float * 2.54, 2)
print(f"Resultat de conversion : {valeur_float} pouces = {valeur_convertie} cm")
"""
def conversion(unit1:str , unit2:str , facteur:float, reverse:bool = False):
    if reverse:
        unit1, unit2 = unit2, unit1
        facteur = 1/facteur

    """ 
    oubien
    
    if reverse:
        tmp=unit1
        unit1=unit2
        unit2=tmp
   """
    valeur_str= input(f"conversion {unit1} vers {unit2}. Donner la valeur en {unit1} ou q pour quitter \n")
    if valeur_str== "q":
        return True
    try:
        valeur_float= float(valeur_str)
    except:
        # Gestion des erreurs en rebouclant sur la fonction egalement appelé la recursion
        print("ERROR: vous devez entrer une valeur numerique. \n Pour les nombres decimals, mettez un point au lieu de virgule")
        #Recursion
        return conversion(unit1,unit2,facteur)
    #autre possibilité:
    # on peut aussi mettre un else a partir d'ici
    valeur_convertie= round(valeur_float * facteur,2)
    print()
    print(f"Resultat de conversion : {valeur_float} {unit1} = {valeur_convertie} {unit2}")
    return False


def demander_utilisateur(min, max):
    val_str= input(f"entrer une valeur entre {min} et {max} ")
    try:
        val_int= int(val_str)
    except:
        print("ERROR vous devez entrer une valeur numerique")
        return demander_utilisateur(min, max)
    if not min <=  val_int <= max:
        print(f"vous devez entrer un nombre entre {min} et {max} ")
    return val_int


# gerer le menu avec les collections: tuple
CONVERSION=(
    ("pouce","cm",0.39),
    ("m","cm",100),
    ("km","miles",0.621371),
)

#Menu du choix de conversion
print("********************************************************************")
print("*    Ce programme vous permet d'effectuer des conversions d'unité  *")
print("********************************************************************")

i=1
for c in CONVERSION:
    unit1=c[0]
    unit2=c[1]
    print(f"{i} - conversion {unit1} vers {unit2}")
    i += 1
    print(f"{i} - conversion {unit2} vers {unit1}")
    i += 1
valeur_maxi = i-1
choice = demander_utilisateur(1, valeur_maxi)

#Conversion des valeurs
while True:
    # Demander les valeurs à convertir à l'utilisateur
    # Si le choix de l'utilisateur est 1 alors l'index est 0 (premier item de conversion)
    # Divisé par 2, car on génére des options intermédiares de conversion inverse
    # choix =2 -> index = 0 mais reverse = True (conversion inverse)
    index = (choice - 1)//2
    #True si la valeur est pair
    reverse = choice % 2 == 0
    unit1, unit2, facteur = CONVERSION[index]
    # if inline
    if conversion(unit1, unit2, facteur, reverse):
        break

print("******************************************************")
print("*                   FIN PROGRAMME                    *")
print("******************************************************")