from exploracion.explorador import calcular_energia,calcular_puntos,mostrar_explorador
from exploracion.isla import generar_evento,valor_tesoro


nombre=input("Introduce tu nombre:")
fuerza = int(input("Introduce la fuerza (un numero del 1 al 10): "))
energia = int(input("Introduce la energía inicial (un numero del 1 al 5): "))

#Probar exception:
#energia= calcular_energia (fuerza, 0)

#guardo el valor de la energia inicial porque lo voy a necesitar despues
energia= calcular_energia (fuerza, energia)
energiaInicial=energia

puntos=0
ronda=1
while ronda<=4:
    
    print (f"---JORNADA{ronda}---")
    ronda+=1
    mostrar_explorador(nombre, energia, puntos)
    resultado=generar_evento(energia)
    if(resultado==1):#tesoro
        print("Has encontrado un tesoro")
        tesoro=valor_tesoro(energia)
        puntos+=tesoro
        if energia>=10 :#soloo si la energia es mayor o igua a 10 de aplica bonificacion
            print("Ha conseguido una bonicación")
            puntos+=calcular_puntos(tesoro, 5)
    if resultado==2 :#trampa
        print("Has caído en una trampa")
        if energia>=2:
            print("Menos dos puntos")
            energia-=2
    if resultado==3 or energia==0 :#descanso. Tambien si empieza la ronda sin energia
        print("Has encontrado un lugar de descanso")
        if energia-2>=energiaInicial:
            print("Mas dos puntos")
            energia+=2

    print(f"Energía: {energia}")
    print(f"Puntos acumulados: {puntos}")

print("---FIN DE LA EXPEDICIÓN---")
mostrar_explorador(nombre, energia, puntos)

    

    


