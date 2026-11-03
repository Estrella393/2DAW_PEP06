
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

#todos sus elementos tiene que ser inmutables,osea, no puedo meter listas pero si duplas
#no sale odenado al recorerlo, a no ser que hagamos otra con sorted
#operaciones: & | - ^ etc