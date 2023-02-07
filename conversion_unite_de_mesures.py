
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
def conversion(unit1:str , unit2:str , facteur:float):
    valeur_str= input(f"conversion {unit1} vers {unit2}. Donner la valeur en {unit1} ou q pour quitter ")
    if valeur_str== "q":
        return True
    try:
        valeur_float= float(valeur_str)
    except:
        # Gestion des erreurs en rebouclant sur la fonction
        print("ERROR: vous devez entrer une valeur numerique. \n Pour les nombres decimals, mettez un point au lieu de virgule")
        return conversion(unit1,unit2,facteur)
    #autre possibilité:
    # on peut aussi mettre un else a partir d'ici
    valeur_convertie= round(valeur_float * facteur,2)
    print()
    print(f"Resultat de conversion : {valeur_float} {unit1} = {valeur_convertie} {unit2}")
    return False

print(" Ce programme vous permet d'effectuer des conversions d'unité")
print("1 - pouces vers cm")
print("2 - cm vers pouces")
print("q -  Quitter")
choice = input("votre choix (1 ou 2): ")
while True:
    if choice=="1":
        if conversion("pouce","cm",2.54):
            break
    else:
        if conversion("cm","pouce",0.394):
            break

