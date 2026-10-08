
n=int(input('Introduce un numero '))

n1=int(n/10) 
#pasar sacar division sin resto y sin cast -> //
n2=n%10

print(n2,n1)

#tambien se podria pasar a sting y utilizar la funcion reversed(), que devuelve caracteres separados que puedes unir con "".join 

texto = str(n)
n3 = "".join(reversed(texto))
print(n3)

