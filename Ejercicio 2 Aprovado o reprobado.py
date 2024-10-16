"""
Escribe un programa que solicite al
usuario ingresar su calificación en un
examen y determine si ha aprobado o
no. Si la calificación es igual o mayor a
60, muestra el mensaje "Has aprobado".
De lo contrario, muestra el mensaje "Has
reprobado".

"""
def aprobadoReprobado():
    calificacionUsuario = int(input('Ingrese su calificacion : '))

    if (calificacionUsuario >= 60) :
        print('Has aprovado.')
    elif (calificacionUsuario >= 0) and (calificacionUsuario <=59) :
        print('Has reprobado. ')
    else :
        print('Ingrese una calificación valida.')

if __name__ == '__main__':
    aprobadoReprobado()