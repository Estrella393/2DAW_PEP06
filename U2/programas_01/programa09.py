import random


print("1. Piedra")
print("2. Papel")
print("3. Tijera")
n = int(input("Seleccione una opción (1, 2 o 3): "))

ale=random.randrange(1,4)#no uncluye 4
print(ale)
#1 gana 3,2 gana 1 y 3 gana a 2; en ortos casos pierde

if ale==n:
    print ("Empate")
elif (n==1 and ale==3) or (n==2 and ale==1)or(n==3 and ale==2):
    print("Ganaste")
else:
    print("Perdiste")