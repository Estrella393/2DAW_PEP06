
tupla1 = (10, 3.14, "Hola", False)
t2 = ()
t3 = (25,)#sin la coma seria un int
t4 = 10, 3.14, "Hola", False
print(type(t2))
print(type(t3))
print(type(t4))

lista = [1,2,3]
con_tupla=tuple(lista)
con_lista=list(con_tupla)

print("Primer elemento:", tupla1[0])
print("Último elemento:", tupla1[-1])
print("Subtupla:", tupla1[2:5])
print("Tupla inversa:", tupla1[::-1])
print("Número de elementos:", len(tupla1))

#las tuplas no permiten eliminar elementos ni modificarse.
del con_lista[3]
con_lista.remove("Zelda")
#y luego se volveria a pasar a tupla
print("Hola" in tupla1)
print(tupla1.index("Hola"))#devuelve la posición de la primera aparición del elemento
print(tupla1.count("Hola"))


#si tengo una lista dentro eso si lo puedo modificar
tupla=(3,2,[4,6]) 
tupla1[2][0]=10