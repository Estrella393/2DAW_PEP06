

continuar=True#con T mayuscula

while continuar:
    num=int(input("Introduce un numero entre 1 y 10"))

    while (num<1 or num>10):
        print("Error")
        num=int(input("Introduce un numero entre 1 y 10"))

    for i in range(1,11):#no coje el ultimooo
        print(num, " * ",i, "=", num*i )

    opc=input("Quieres volver a introducir un numero? Respode Si o No")
    if opc=="Si":
        continuar=True
    else:
        continuar=False 


