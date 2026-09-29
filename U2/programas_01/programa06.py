d = int(input("Introduce el día"))
m = int(input("Introduce el mes"))
a = int(input("Introduce el año"))

correcto=False
if a>0:
    if m>0 and m<12:
            if (((d>0 and d<=30) and m in [1,3,5,7,8,10,12]) or ((d>0 and d<=31) and m is [4,8,9,11]) or ((d>0 and d<=28) and m=2 )):
                correcto=True
    
