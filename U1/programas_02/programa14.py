n=B = int(input("Introduce el número de bytes: "))

#se va dividiendo entre 1000 (decimal) o entre 1024(binrio)
gb=n//1000**3
mb=(n%1000**3) //1000**2 #sacarlo con el resto, no pide calcularlo completo en cada unidad
kb=(n%1000**2)//1000
b=n%1000

gib=n//1000**3
mib=(n%1000**3) //1000**2 #sacarlo con el resto, no pide calcularlo completo en cada unidad
kib=(n%1000**2)//1000
b2=n%1000


bin=format(n, "b") #o un printf(f"{B} es ...)
print(bin," bytes en sistema decimal (SI): ",gb," GB,",mb," MB,",kb," KB,",b," bytes")
print(bin," bytes en sistema binario (IEC): ",gib," GiB,",mib," MiB,",kib," KiB,",b2," bytes")