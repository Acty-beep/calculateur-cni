code = input()
resultat = 0
i = -1
facteur = [7, 3, 1]

for car in code:
    if car == "<":
        valeur = 0
        i += 1
    elif car in "0123456789":
        valeur = int(car)
        i += 1
    elif car in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        valeur = ord(car)-55
        i += 1
    else:
        print("Caractere hors bornes")
        break
        
    resultat += valeur * facteur[i%3]
print(resultat % 10)
