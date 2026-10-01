num=int(input("Introduce un numeros"))
suma=0
cont=1#ya ha introduccido un numero aunque sea 0, y asi no divido entre 0
'''en este caso cuento 0 como otro numero mas par la media,
 pero si no lo inicializaria a 0 y en los resultados pondria la condicion cont>0'''
while num!=0:
    suma=suma+num
    cont+=1
    num=int(input("Introduce un numeros. Para terminar escribe 0"))
    
media=suma/cont
print("La suma es ",suma)
print("La media es ",media)        



num=int(input("Introduce un numeros"))
suma=0
cont=1
while True:
    if num==0:
        break
    suma=suma+num
    cont+=1
    num=int(input("Introduce un numeros. Para terminar escribe 0"))

media=suma/cont
print("La suma es ",suma)
print("La media es ",media)        
