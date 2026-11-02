
mi_lista06=[30,"Hola",True,5.7]

print("Longitud:", len(mi_lista06))
print("Primer elemento:", mi_lista06[0])
print("Último elemento:", mi_lista06[-1])

mi_lista06[2] = False
mi_lista06.append("Adios")
mi_lista06.insert(1,"Primero")
for i in mi_lista06:
    print(i)
"""
for i in range(len(mi_lista06)):
    print(i, mi_lista06[i])
"""
nueva_lista = mi_lista06[2:5]#final-1
lista_pares = mi_lista06[::2]#principio:final:incremento
lista_inversa = mi_lista06[::-1]
mi_lista06.reverse()
print(mi_lista06)