"""
Crea un programa que solicite al
usuario un número entero positivo y
luego imprima los números desde ese
número hasta 1 utilizando un
buclewhile.

"""
def enteroPositivo():

    numeroEntero = int(input('Ingresa un numero entero positivo :'))
    if (numeroEntero > 0) :
        while (numeroEntero >= 1):
            print(numeroEntero)
            numeroEntero -= 1
    else :
        print('Ingrese un numero entero positivo.')
        
if __name__ == '__main__' :
    enteroPositivo()