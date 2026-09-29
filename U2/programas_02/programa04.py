

#bucle que no evalue niguna condicion: while:True

n = int(input("Introduce un número"))

while n != 45:
    n = int(input("Introduce un número"))
print("Saliste del primer bucle")

while True:
    n = int(input("Introduce un número"))

    if n == 45:
        break
print("Saliste del segundo")