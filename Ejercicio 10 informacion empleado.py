"""
Construya un algoritmo en Python, que
permita ingresar la información de un
empleado e imprima el nombre, los apellidos
y la antigüedad. Los datos que se deben
solicitarson los siguientes:
*Nombre* Teléfono
*Año de ingreso a la empresa*Apellidos
*Edad.

"""

def informacionEmpleado():

    nombre = str(input('Ingrese el nombre del empleado : '))
    apellido1 = str(input('Ingrese el primer apellido del empleado : '))
    apellido2 = str(input('Ingrese el segundo apellido del empleado : '))
    antiguedad = int(input('Ingrese el año de ingreso a la empresa :'))
    edad = int(input('Ingrese la edad del empleado:'))
    telefono = int(input('Ingrese el telefono del empleado:'))

    informacion = str(input('Desea verificar la informacion ingresada ? ingrese Si o No para continuar.')).lower()
    if informacion == 'si' :
        print(f'Nombre : {nombre}\nApellidos : {apellido1} {apellido2}\nAntiguedad : {antiguedad}\nEdad : {edad}\nTelefono : {telefono}')
    else :
        pass
if __name__ == ('__main__'):
    informacionEmpleado()