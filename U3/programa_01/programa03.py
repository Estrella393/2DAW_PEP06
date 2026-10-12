
def mostrar_menu ():
    print("1. Calcular el área de un círculo \n"
    "2. Calcular el área de un triángulo \n"
    "3. Calcular el área de un rectángulo \n"
    "4. Salir \n"
    "Introduce una opción (1-4): \n")

def calcular_area_circulo(r):
    area=3.14*r**2
    print(f"El área del círculo es: {area}") 

def calcular_area_triangulo(b,a):
    area=(b*a)/2 
    print(f"El área del triángulo es: {area}")

def calcular_area_rectangulo(b,a):
    area=b*a 
    print(f"El área del rectangulo es: {area}") 

def main():
    opc=0#inicializar
    while opc!=4:
        mostrar_menu()
        opc=int(input("Elige"))
        if (opc<1 or opc>4):
            print("No seleccionaste ninguna opción")
        else:
            match opc:
                case 1:
                    opcion1()
                case 2:
                    opcion2()
                case 3:
                    opcion3()
                         

      
def opcion1():
    r=float(input("Introduce el radio"))
    if (r>0):
        calcular_area_circulo(r)
    else:
        print("El radio tiene que ser mayor de 0")    

def opcion2():
    b=float(input("Introduce la base"))
    a=float(input("Introduce la altura"))
    if (b>0 and a>0):
        calcular_area_triangulo(b,a)
    else:
        print("Tiene que ser mayor de 0")  

def opcion3():
    b=float(input("Introduce la base"))
    a=float(input("Introduce la altura"))
    if (b>0 and a>0):
        calcular_area_rectangulo(b,a)
    else:
        print("Tiene que ser mayor de 0")                


main()        