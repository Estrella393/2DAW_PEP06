import batalla.jugador#separar con ,
from batalla.enemigo import generar_enemigo, ataque_enemigo, mostrar_enemigo


print("=== BATALLA DE MAGIA ===")
nombre = input("Introduce tu nombre: ")
conocimiento = int(input("Introduce el conocimiento (un numero del 1 al 10): "))
energia = int(input("Introduce la energía inicial (un numero del 1 al 5): "))

batalla.jugador.mostrar_jugador(nombre, conocimiento, energia)
n,c,e=generar_enemigo()
mostrar_enemigo(n,c,e)

ronda=1
while ronda<=3:
    print(f"--- RONDA {ronda} ---")
    ronda += 1
    magiaJugador=batalla.jugador.ataque_jugador (conocimiento, energia)
    magiaEnemigo=ataque_enemigo (c, e)
    if magiaJugador>magiaEnemigo:
        e-=1
        print(f"{nombre} lanza un hechizo poderoso! (-1 energía enemigo)")
    elif magiaJugador<magiaEnemigo:
        energia-=1
        print(f"{n} responde con un conjuro devastador! (-1 energía jugador)")
    else:
        print("Ninguno pierde energía.")
print("=== FIN DEL DUELO ===") 
if energia>e:
    print(f"¡{nombre} ha vencido a {n}!")
elif e> energia:
    print(f"¡{n} ha vencido a {nombre}!")
else:
    print("Empate")


"""ENTORNO VIRTUAL:
python -m venv .venv
.venv\Scripts\Activate.ps1  o .venv\Scripts\activate(en cmd)
deactivate

tambien vale:
py -3.12 -m venv .venv
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted
.venv\Scripts\Activate.ps1


NOTA:if __name__ == "__main__":
    main()
"""   