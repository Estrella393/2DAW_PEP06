import random

#1 tesoro 2 trampa 3 descansoi
def generar_evento(energia):
    aleatorio=random.randrange(1, 6)
    if (energia<10):
        match aleatorio:
            case 1:
                return 1
            case 2|3:
                return 2
            case 4|5:
                return 3
    else:
        match aleatorio:
            case 1|2|3:
                return 1
            case 4:
                return 2
            case 5:
                return 3

def valor_tesoro(energia):
    return energia + random.randrange(1, 6) 

                


   