
import random


ale=random.randrange(17, 22)
carta=0
suma=0
continuar=True

while continuar :
    opc=input("Quieres sacar una carta?")
    if opc=="Si":
        carta=random.randrange(1, 6)
        suma=suma+carta

    else: 
        continuar=False

print("La banca ha sacado un ",ale)
print("tu has sacado un ",suma)
if suma>21 or suma<ale:
    print("Perdiste")
else:
    print("Ganaste") 