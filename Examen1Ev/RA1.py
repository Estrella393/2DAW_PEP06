nombre=input("Introduce tu nombre:")#no es necesario str porque input ya devuleve una cadena
kilometros=float(input("Introduce los kilometros recorridos:"))
ocupantes=int(input("Introduce el número de ocupantes:"))

CONSUMO_100KM=6.5
PRECIO_LITRO=1.60
DESCUENTO=10

litros=kilometros/100* CONSUMO_100KM

coste= litros+PRECIO_LITRO

descuento=DESCUENTO/100*coste

final=coste-descuento
print("Combustible consumido: ", litros ," litros")
print("Coste inicial: ", round(coste,2) ," euros")
print("Descuento aplicado: ", round(descuento,2) ," euros")
print("Coste final: ", round(final,2) ," euros")
print("Importe de cada persona: ", round(final/ocupantes,2) ," euros")

#Valor y tipo de dato
print(f"{type(nombre)}: {nombre}")
print(f"{type(kilometros)}: {kilometros}")
print(f"{type(ocupantes)}: {ocupantes}")

#Comprobaciones individuales
comprobar1 =  isinstance(nombre,str) 
comprobar2 = isinstance(kilometros,float)
comprobar3 = isinstance(ocupantes,int)

#comprobacion global
comprobarTodo= comprobar1 and comprobar2 and comprobar3
resultado = comprobarTodo and "Todas son correctas."#porque si no el texto siempre es true
mensaje = resultado or "Error en alguna" #Si la primera es verdadera escribe esa
print(mensaje)

print(f"RESUMEN: \n"
      f"Nombre del conductor: {nombre}\n"
       f"Kilometros recorridos: {kilometros}\n"
        f"Número de ocupantes: {ocupantes}\n"
         f"Importe de cada persona:  {round(final/ocupantes,2)} euros \n")