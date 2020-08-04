#Evalua una clave de acceso numerica, para sacar dinero de un cajero.

def key_access(key):
    if key == 2958:
        print('Pedes retirar dinero.')
    else:
        print('Clave incorrecta.')

if __name__ == "__main__":
    key = int(input('Ingresa la clave de acceso: '))
    key_access(key)