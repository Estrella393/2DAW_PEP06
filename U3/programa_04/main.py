

# imports de la librería estándar
# imports de librerías de terceros
# imports de módulos propios
from matematicas import operaciones
from matematicas import figuras
from matematicas import conversiones
# Definición de funciones principales
def main():
    """Función principal del programa"""
    numero1 = float(input("Introduce el primer número: "))
    numero2 = float(input("Introduce el segundo número: "))

    print("Suma:", operaciones.suma(numero1, numero2))
    print("Resta:", operaciones.resta(numero1, numero2))
    print("Multiplicación:", operaciones.multiplicacion(numero1, numero2))
    print("División:", operaciones.division(numero1, numero2))

    print("Área del rectángulo:", figuras.area_rectangulo(5, 7))
    print("Área del triángulo:", figuras.area_triangulo(5, 7))
    print("Área del círculo:", figuras.area_circulo(5))


# Bloque para asegurar ejecución sólo si el archivo es el principal
if __name__ == "__main__":
# Se pueden procesar argumentos, inicializar variables, etc.
    main()    