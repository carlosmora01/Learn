def saludar(nombre, lenguaje):
    if lenguaje == 'es':
        print('Hola', nombre)
    elif lenguaje == 'fr':
        print('Salut', nombre)
    elif lenguaje == 'en':
        print('Hello', nombre)
    elif lenguaje == 'pt':
        print('OLA', nombre)
    else:
        print('Lenguaje no disponible')

def bienvenida():
    print('Bienvenido(a) a este programa')

usuario = 'Julian'
saludar(usuario, 'fr')
saludar(usuario, 'it')
