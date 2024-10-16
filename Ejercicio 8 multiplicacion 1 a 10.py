"""
Escribe un programa que solicite al usuario
ingresar un número y luego muestre la tabla
de multiplicar de ese número del 1 al 10

"""
def tablaMultiplicar():
    print('Multiplica un numero de 1 hasta 10.')
    numero = int(input('Ingrese un numero :'))

    for i in range (1,11):
        multiplicacion = numero * i
        print(f'{numero} x {i} = {multiplicacion}')

if __name__ == ('__main__'):
    tablaMultiplicar()
