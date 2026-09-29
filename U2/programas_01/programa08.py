import random

j1d1 = random.randrange(1, 7)
j1d2 = random.randrange(1, 7)
print("Jugador1:",j1d1,j1d2)

j2d1 = random.randrange(1, 7)
j2d2 = random.randrange(1, 7)
print("Jugador2:",j2d1,j2d2)

suma1 = j1d1+j1d2
suma2 = j2d1+j2d2
#funcion max para sacar el maximo
m1=max(j1d1,j1d2)
m2=max(j2d1,j2d2)

if suma1 > suma2:
    print("Gana el jugador 1")
elif (suma2 > suma1):
    print("Gana el jugador 2")
else:
    print("Empate en la suma")
    if m1>m2 :
        print("Gana el jugador 1")
    elif (m2>m1):
        print("Gana el jugador 2")
    else:   
        print("Empate")