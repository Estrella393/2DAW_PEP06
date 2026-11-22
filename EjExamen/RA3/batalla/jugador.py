import random

def ataque_jugador (conocimiento, energia):
    return conocimiento*energia*random.randrange(1, 4)

def mostrar_jugador(nombre, conocimiento, energia):
     print(f"Jugadora: {nombre}\n"
        f"Conocimiento: {conocimiento}\n"
        f"Energía: {energia}")