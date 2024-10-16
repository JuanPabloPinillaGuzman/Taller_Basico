"""
Crea un programa que pida al usuario ingresar el nombre de un país y luego
determine en qué continente se encuentra.Utiliza estructuras condicionales
para asociar cada país con su respectivo continente y muestra un mensaje 
con el continente correspondiente.

"""

def continentes():
    print('Paises disponibles :\nColombia\nEspaña\nChina\nNueva Zelanda\nCanada\nSenegal\nArgentina\nRusia\nEstados Unidos\n')
    sA = 'Sur america'
    nA = 'Norte america'
    asia = 'Asia'
    europa = 'Europa'
    oceania = 'Oceania'
    africa = 'Africa'
    pais = str(input('Ingrese el nombre de un pais para conocer su continente :')).lower()
    
    if pais == 'colombia':
        print(f'El continente al que pertenece {pais} es {sA}.')
    elif pais == 'españa':
        print(f'El continente al que pertenece {pais} es {europa}.')
    elif pais == 'china':
        print(f'El continente al que pertenece {pais} es {asia}.')
    elif pais == 'nueva zelanda':
        print(f'El continente al que pertenece {pais} es {oceania}.')
    elif pais == 'canada':
        print(f'El continente al que pertenece {pais} es {nA}.')
    elif pais == 'senegal':
        print(f'El continente al que pertenece {pais} es {africa}.')
    elif pais == 'argentina':
        print(f'El continente al que pertenece {pais} es {sA}.')
    elif pais == 'rusia':
        print(f'El continente al que pertenece {pais} es {europa}.')
    elif pais == 'estados unidos':
        print(f'El continente al que pertenece {pais} es {nA}.')
    else : 
        print('Error, ingrese un pais valido.')
    

if __name__ == '__main__':
    continentes()