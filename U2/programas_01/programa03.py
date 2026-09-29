try:
    n1 = int(input("Introduce un número"))
    n2 = int(input("Introduce otro número"))
    print(f"La división {n1}/{n2} es = {n1/n2}")

except ZeroDivisionError:  
    print("Error: división entre 0")