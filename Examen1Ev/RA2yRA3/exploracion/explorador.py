import random

#devuelve su energia inicial
def calcular_energia (fuerza, energia):
    #try:
        e=fuerza*energia*random.randrange(1, 4)
        print(e)
        return e
       
"""except ValueError:
        print("No puedes introducir 0.")"""
     
def calcular_puntos(valor_tesoro,bonus):
    return valor_tesoro+bonus

def mostrar_explorador(nombre, energia, puntos):
     print(f"Jugadora: {nombre}\n"
        f"Energía: {energia}\n"
      f"Puntos: {puntos}\n")