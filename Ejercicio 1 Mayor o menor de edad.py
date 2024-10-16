"""
Escribe un programa que solicite al
usuario ingresar su edad y luego
determine si es mayor de edad o no
utilizando una declaraciónif. Si la edad
es mayor o igual a 18, muestra el
mensaje "Eres mayor de edad", de lo
contrario, muestra el mensaje "Eres
menor de edad".
"""
def mayorMenor():
    edad = float(input('Ingrese su edad : '))

    if edad >= 18 :
        print('Eres mayor de edad.')
    elif (edad >= 0) and (edad <=17 ):
        print('Eres menor de edad.')
    else :
        print('Ingrese una edad valida.')


if __name__ == '__main__':
    mayorMenor()