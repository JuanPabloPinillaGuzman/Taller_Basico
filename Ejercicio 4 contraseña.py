"""
Crea un programa que solicite al
usuario ingresar una contraseña y
verifique si cumple con los siguientes
requisitos: debe tener al menos 8
caracteres y contener al menos un
número. Si la contraseña cumple con
los requisitos, muestra el
mensaje"Contraseña válida". De lo
contrario, muestra el mensaje
"Contraseña inválida".

"""

def requisitosContraseña():

    contraseña = str(input('Ingrese su contraseña :'))
    caracteres = len(contraseña)
    numero='1234567890'
    contadorN = 0
    verificarN = False
    if (caracteres >= 8):
        for i in caracteres:
            contadorN += 1
            verificarN = True
            print('Su contraseña es valida')

    else :
        print('Ingrese una contraseña valida.')           




if __name__ == '__main__' :
    requisitosContraseña()