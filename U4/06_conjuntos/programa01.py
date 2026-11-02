
"""
listas permiten duplicados y tienen índices 
tuplas permiten duplicados pero no se pueden modificar
conjuntos no permiten duplicados y no tienen índices.
"""
numeros = {10, 20, 30, 40, 50}
print( numeros)

conjunto_vacio = set()
print( conjunto_vacio)
print("Tipo:", type(conjunto_vacio))

numeros_repetidos = {10, 20, 20, 30, 30, 30}
print("Conjunto sin duplicados:", numeros_repetidos)

numeros.add(40)
numeros.remove(10)

