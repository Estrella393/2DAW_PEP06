n=int(input("Introduce tu nota"))
match n:
    case _ if 0 <= n < 4:# no deja poner case range(0,4), en todo caso case _ if n in range(1, 6):
        print("Insuficiente")
    case 5:
        print("Suficiente")
    case 6:
        print("Bien")
    case 7|8:
        print("Notable")
    case 9|10:
        print("Sobresaliente")
    case _:#ELSE 
        print("El numero no esta en el rango 0-10")
