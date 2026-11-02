
# imports de la librería estándar
# imports de librerías de terceros
# imports de módulos propios
import operaciones
# Definición de funciones principales
def main():
    """Función principal del programa"""
    numero1 = float(input("Introduce el primer número: "))
    numero2 = float(input("Introduce el segundo número: "))

    print("Suma:", operaciones.suma(numero1, numero2))
    print("Resta:", operaciones.resta(numero1, numero2))
    print("Multiplicación:", operaciones.multiplicacion(numero1, numero2))
    print("División:", operaciones.division(numero1, numero2))

# Bloque para asegurar ejecución sólo si el archivo es el principal
if __name__ == "__main__":
# Se pueden procesar argumentos, inicializar variables, etc.
    main()    