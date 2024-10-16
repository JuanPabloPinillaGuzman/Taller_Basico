"""
Escribe un programa que solicite al usuario ingresar el día, el mes y el año de
una fecha. Luego, verifica si la fecha es válida o no. Considera los diferentes
casos, como los días de cada mes y si el año es bisiesto. Muestra un mensaje
indicando si la fecha es válida o no.

"""

def fechaValida():
    dia = int(input('Ingrese el dia : '))
    mes = int(input('Ingrese el mes : '))
    año = int(input('Ingrese el año : '))
    if mes == 2:
        if dia <= 29:
            if (año % 4 == 0) or (año % 400 == 0):
                print('La fecha es valida.')
            else:
                print('La fecha no es valida.')
        else:
            print('La fecha no es valida.')
    if (mes == 4) or (mes == 6) or (mes == 9) or (mes == 11):
        if dia <= 30:
            if año <= 2024:
                print('La fecha es valida.')
            else:
                print('La fecha no es valida.')
        else:
            print('La fecha no es valida.')
    if (mes == 1) or (mes == 3) or (mes == 5) or (mes == 7) or (mes == 8) or (mes == 10) or (mes == 12):
        if dia <= 31:
            if año <= 2024:
                print('La fecha es valida.')
            else:
                print('La fecha no es valida.')
        else:
            print('La fecha no es valida.')
    


fechaValida()