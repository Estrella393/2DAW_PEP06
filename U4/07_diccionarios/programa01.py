
diccionario = {}
print( type(diccionario))

persona = {
    "nombre": "María",
    "edad": 25,
    "pais": "España"#no se pueden repetir las claves
}

persona2 = dict(nombre="Ana", edad=30, pais="España")
print(type(persona2))
print("Nombre:", persona["nombre"])
print("Edad:", persona["edad"])
print("País:", persona.get("pais"))#con valor por defecto("pais", "no dispinible")


for clave in persona:
    print(clave)

for valor in persona.values():
    print(valor)

for clave, valor in persona.items():
    print(clave, ":", valor)