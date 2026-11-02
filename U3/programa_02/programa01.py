
import math
#from math import sin, cos, sqrt, pow, radians

opc=1
while opc>=1 and opc<=4:
    print("1. Seno de un ángulo")
    print("2. Coseno de un ángulo")
    print("3. Raíz cuadrada de un número")
    print("4. Potencia de dos números")

    opc=int(input("Selecciona una operación: "))

    if opc==1:
        #a=float(input("Introduce el ángulo: "))
        print (math.sin(math.radians(30)));#seno del angolo
    elif opc==2:
        print (math.cos(math.radians(30)));#cos del angolo
    elif opc==3:
        print (math.sqrt(81));#raiz
    elif opc==4:
        print (math.pow(2, 3));#potencia
    else:
        print("Error")