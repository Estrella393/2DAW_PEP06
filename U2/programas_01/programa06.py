d = int(input("Introduce el día: "))
m = int(input("Introduce el mes: "))
a = int(input("Introduce el año: "))

correcto = False

if a > 0:
    if m > 0 and m <= 12:
        if (((d > 0 and d <= 31) and m in [1, 3, 5, 7, 8, 10, 12]) or
            ((d > 0 and d <= 30) and m in [4, 6, 9, 11]) or
            ((d > 0 and d <= 28) and m == 2)):#tambien podia haber añadido las otras dos condiciones aqui y no necesitaba booleano
            
            correcto = True
if (correcto==True):
    print("Si es correcta")
else:
    print("No es correcta")