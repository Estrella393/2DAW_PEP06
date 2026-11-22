import random



vidas=3
puntos=0
nivel=1
while vidas>0:
    print(f"El jugador tiene {vidas} vidas")
    print("Elige un tipo de ataque:\n" 
    "fuerza\n" 
    "precisión\n" 
    "riesgo")
    opc=input()
    match opc:
        case "fuerza":
            jugador=random.randrange(5, 11)#no llega al ultimo numero
            villano=random.randrange(3, 11)
        case "precisión":
            jugador=random.randrange(3, 9)
            villano=random.randrange(2, 10)    
        case "riesgo":
            jugador=random.randrange(1, 11)
            villano=random.randrange(1, 9) 
        case _:
            print("Opción no válida")
            continue  
    print(f"Has sacado: {jugador}") 
    print(f"El villano ha sacado: {villano}")      
    if jugador>villano:
         puntos+=1
         print(f"Has ganado y ahora tienes {puntos} puntos")
         if puntos%3==0 :#cada vez que sea un multipli de 3
             """o tambien:
             puntosNivel += 1
                if puntosNivel == 3:
                    nivel += 1
                    puntosNivel = 0"""
             nivel+=1
             print(f"Nivel: {nivel}")
             if vidas<3:
                vidas+=1
                print(f"Has recuperado una vida. Vidas: {vidas}")
    elif villano>jugador:
         vidas-=1
         print(f"Has perdido y ahora tienes {vidas} vidas") 
    else:
        print("Ha habido un empate")
    

print(f"Vidas restantes: {vidas}")
print (f"El juego a finalizado, tienes {puntos} puntos")
print(f"Puntuación final: {puntos}")
print(f"Has llegado al nivel: {nivel}")
        