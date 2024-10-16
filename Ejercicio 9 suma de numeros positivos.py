"""
Crea un programa que solicite al usuario
ingresar una serie de números positivos y
luego calcule e imprima el promedio de los
números ingresados utilizando un bucle while.
El programa debe terminar cuando el usuario
ingrese un número negativo.

"""

def sumaPositivos():
    contador = 0
    suma = 0
    
    print('Ingrese numeros positivos, si quiere realizar la suma de estos ingrese un numero negativo.')
    
    while True:
        numeroPositivo = float(input('Ingrese un numero : '))
        if numeroPositivo < 0:
            break
        contador += 1
        suma += numeroPositivo
        
    if contador > 1 :
        print(f'La suma de los numeros positivos es: {suma / contador}. ')

if __name__ == '__main__':
    sumaPositivos()
