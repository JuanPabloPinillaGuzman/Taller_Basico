"""
En su casa le solicitan que
realice un algoritmo en Python,
que permita calcular el valor a
pagar por concepto de energía
eléctrica. Los datos que se
conocen son los siguientes:
-Mes de consumo
-Valorkw
-Totalkwconsumido en el mes
-estrato

"""

def facturaEnergia():

    valorKw = int(input('Ingrese el valor del kw : '))
    totalKwConsumido = float(input('Ingrese el total de kw consumidos : '))
    mes = str(input('Ingrese el mes de consumo: '))
    estrato = int(input('Ingrese si es estrato 1, 2 ,3, 4, 5, 6 : '))
    valorSinImpuestos = (valorKw * totalKwConsumido)
    est1 = valorSinImpuestos * 1.1
    est2 = valorSinImpuestos * 1.2
    est3 = valorSinImpuestos * 1.3
    est4 = valorSinImpuestos * 1.4
    est5 = valorSinImpuestos * 1.5
    est6 = valorSinImpuestos * 1.6

    if (estrato == 1):
        print(f'El valor a pagar por concepto de energia electrica para el mes de {mes}, es de {est1}$.')
    elif (estrato == 2):
        print(f'El valor a pagar por concepto de energia electrica para el mes de {mes}, es de {est2}$.')
    elif (estrato == 3):
        print(f'El valor a pagar por concepto de energia electrica para el mes de {mes}, es de {est3}$.')
    elif (estrato == 4):
        print(f'El valor a pagar por concepto de energia electrica para el mes de {mes}, es de {est4}$.')
    elif (estrato == 5):
        print(f'El valor a pagar por concepto de energia electrica para el mes de {mes}, es de {est5}$.')
    elif (estrato == 6):
        print(f'El valor a pagar por concepto de energia electrica para el mes de {mes}, es de {est6}$.')
    else :
        print('Ingrese un estrato valido.')


if __name__ == '__main__':
    facturaEnergia()