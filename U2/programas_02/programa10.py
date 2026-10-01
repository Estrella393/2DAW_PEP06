

import random


ale=random.randrange(17, 22)

numJugadores=int(input("Cunatos jugadores quieres?"))

for i in range(1,numJugadores+1):
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
    print("Jugador ",i,": has sacado un ",suma)
    if suma>21 or suma<ale:
        print("Perdiste")
    else:
        print("Ganaste") 