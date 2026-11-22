
minutos = int(input("Introduce una cantidad de minutos: "))
horas = int(minutos / 60) #o hacer division sin decimales://
resto = minutos - horas * 60
print("Equivale a ", horas ," horas y ", resto ," minutos")


n1 = int(input("Introduce un número entero: "))
n2 = float(input("Introduce un número decimal: "))
n3 = str(input("Introduce una cadena de texto: "))#input ya devulve siempre cadena asique no es necesario str
print(f"{type(n1)}: {n1}")
print(f"{type(n2)}: {n2}")
print(f"{type(n3)}: {n3}")
#las tres variables booleanas:
comprobar1 = type(n1)==int
comprobar2 = type(n2)==float
comprobar3 = type(n3)==str
#indicando si todas las comprobaciones son correctas
"""REPASO:
and:
True	True	True
True	False	False
False	True	False
False	False	False

or(Devuelve el primer valor que sea verdadero (True). Si el primero es falso, pasa al segundo):
True	True	True
True	False	True
False	True	True
False	False	False
nota;0 también se considera falso
"""
comprobarTodo= comprobar1 and comprobar2 and comprobar3
#Si todas son correctas, el programa debe mostrar la suma del número entero y el número decimal
#ERROR(print devuelve si no esta vacia siempre devuelve true):print(f"Todas son correctas. Suma: {n1+n2}") or print("Error en alguna")
resultado = comprobarTodo and f"Todas son correctas. Suma: {n1+n2}"
mensaje = resultado or "Error en alguna"
#ejemplo si es correcto : (True and True) or True:True
print(mensaje)