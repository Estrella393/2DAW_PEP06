

import random


ale=random.randrange(1, 21)
num=0
cont=0

while num!=ale and cont<3:#no pongo igual porque se incrementa abajo
    num=int(input("Adivina el número"))
    if ale>num:
        print("El número aleatorio es mayor")
    elif ale<num:
        print("El número aleatorio es menor")  
    else:
        print("Has acertadooo")  

    cont+=1

