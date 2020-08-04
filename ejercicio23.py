#Evalua si un caracter si es una vocal minuscula

def vocal_min():
    while True:
        vocal = str(input('''

            BIENVENIDO A LAS VOCALES
            Ingresa una vocal:
            [s] Presiona s para salir

            '''))
        
        if vocal == 'a':
            print('A')
        elif vocal == 'e':
            print('E')
        elif vocal == 'i':
            print('I')
        elif vocal == 'o':
            print('O')
        elif vocal == 'u':
            print('U')
        elif vocal == 's':
            break
        else:
            print('No ingresaste vocal.')

if __name__ == "__main__":
    
    vocal_min()
    
