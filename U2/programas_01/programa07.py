
a = int(input("Introduce el año: "))

if (a%4==0 and a%100!=0)or a%400==0:#no es necesario paraentesis en el if
    print("Es bisiesto")
else:
    print("No es bisiesto") 