

for i in range(0, 11):
    if i % 2 == 0:
        print(i)

for i in range(0, 11):
    if i % 2 != 0:
        continue#salta y continua 
    print(i)        


i = 0
while i <= 10:
    if i % 2 == 0:
        print(i)
    i = i + 1

z = 0
while z <= 10:
    if z % 2 != 0:
        z = z + 1
        continue
    print(z)
    z = z + 1