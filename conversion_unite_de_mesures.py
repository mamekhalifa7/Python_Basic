
print(" Ce programme vous permet d'effectuer des conversions d'unité")
print("1 - pouces vers cm")
print("2 - cm vers pouces")
choice = input("votre choix (1 ou 2): ")
if choice=="1":
    valeur_str= input(" conversion pouces vers cm. Donnez la valeur en pouces : ")
    valeur_float = float(valeur_str)
    valeur_convertie = round(valeur_float * 2.54, 2)
print(f"Resultat de conversion : {valeur_float} pouces = {valeur_convertie} cm")