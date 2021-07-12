from tkinter.constants import NUMERIC


def cuenta_atras(numero):
    numero -= 1
    if numero > 0:
        print(numero)
        cuenta_atras(numero)
    else: 
        print ("llegaste al 0")
#cuenta_atras(10)


def calcular_factorial(numero):
    print (f"orden de liberacion:{numero}!")
    if numero >1:
        numero = numero * calcular_factorial(numero-1)
    return numero
    
    
#print (calcular_factorial(13))

def sucesion(numero):
    numero *= 2
    if -100<numero<100:
        print(numero)
        sucesion(numero)
    else:
        print('esta sucesion acaba aqui')
    print (f"orden de liberacion:{numero}")

print(sucesion(-10))

