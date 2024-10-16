"""
Crea un programa que solicite al usuario ingresar tres
longitudes y determine si esas longitudes pueden formar
un triángulo válido. Utiliza la desigualdad triangular
para realizar la comprobación y muestra un mensaje
indicando si se puede formar un triángulo o no.
La desigualdad triangular es un concepto matemático
que establece una condición necesaria para que tres
segmentos puedan formar un triángulo válido. La
desigualdad triangular establece que la suma de las
longitudes de dos lados de un triángulo siempre debe ser
mayor que la longitud del tercer lado.
En términos más precisos, si tienes tres segmentos con
longitudes a, b y c, donde a, b y c son números
positivos, entonces estos segmentos pueden formar un
triángulo válido si y solo si se cumple la siguiente
condición:
a + b > c
a + c > b
b + c > a

"""
def trianguloValido():

    long1 = float(input('Ingresa la primer longitud del triangulo :'))
    long2 = float(input('Ingresa la segunda longitud del triangulo :'))
    long3 = float(input('Ingresa la tercera longitud del triangulo :'))

    suma1 = (long1 + long2)
    suma2 = (long1 + long3)
    suma3 = (long2 + long3)

    if (suma1 > long3) and (suma2 > long2) and (suma3 > long1) :
        print('Es un triangulo valido.')
    else : 
        print('El triangulo no es valido.')

    
if __name__ == '__main__':
    trianguloValido()    