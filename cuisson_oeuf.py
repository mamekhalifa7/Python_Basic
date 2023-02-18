import time

print ("Cuisson des oeufs")
print("1 - Oeufs à la coque : 3 minutes")
print("2 - Oeufs mollets : 6 minutes")
print("3 - Oeufs durs : 9 minutes")
choix = input("Votre choix : ")

duree = 0
if choix == "1":
    duree = 3*60
elif choix =="2":
    duree = 6*60
else:
    duree = 9*60

while True:
    for i in range(5):
        time.sleep(1)
        print(".", end="", flush=True)
    print("")