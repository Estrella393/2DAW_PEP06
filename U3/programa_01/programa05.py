#(globales, no locales y locales

#Las variables locales sólo existen en la propia función y no son accesibles desde niveles superiores
def local():
    a = 2
    print(a)
local() 
  



#global
x = 10
def global1():
    print(x)

global1()
#o tambien:
def global2():
    global a
    print(a)#muestra 5 ya que coje la global de fuera
    a = 1#al ejecutarlo modifica la variable global que pasa a ser 1
    return
a = 5
global2()
print(a)#fuera de la funcion coje el 1

#no local aplica a variables definidas en una función externa (pero no global) y que se pueden acceder desde una función interna (anidada).
def noLocal():
    def sub_noLocal():#busca a en la funcion mayor
        print(a)
        return
    a = 3
    sub_noLocal()
    print(a)
    return
a = 4
noLocal()
print(a)#ninguna modifica global, asqie vale 4
#o
def noLocal():
    def sub_noLocal():
        nonlocal a#exactamente igual, ya que antes tamboco cambiabamos las variables mas generales
        print(a)
        return
    a = 3
    sub_noLocal()
    print(a)
    return
a = 4
noLocal()
print(a)
#si seria relevante en casos como este:
def noLocal2():
    a = 3
    def sub_noLocal2():
        nonlocal a#nonlocal a indica que queremos modificar la a de la función externa
        a = 7
    sub_noLocal2()
    print(a)

noLocal2()#daria 7