
h=int(input('Introduce las horas '))

m=int(input('Introduce minutos '))

s=int(input('Introduce segundos '))


t=int(input('Introduce el trayecto en segundos '))

h2=h*3600
m2=m*60
totalIni=h2+m2+s

totalFin=totalIni+t

hF=totalFin//3600
mF=(totalFin%3600)//60
sF=totalFin%60
print(hF, ":",mF,":",sF)




