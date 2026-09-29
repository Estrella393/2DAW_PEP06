n = int(input("Introduce un número entre 1 y 10"))

while n<1 or n>10:
    n = int(input("Vuleve a intentaro"))

#si sale del bucle se ejecuta for, si no no
for i in range(1, n+1):
    print(i)