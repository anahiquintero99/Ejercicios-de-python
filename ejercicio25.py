#Recibe caracter e indica si es un numero o una letra.

def run():
    while True:
        number = input('''
        
            Ingresa caracter: 
            [$] Presiona s para salir
            
            ''')
        
        if number.replace('.', '').isdigit():
            print('Es un numero')
        elif number.isalpha():
            print('Es una letra')
        elif number == '$':
            break
        else:
            print('Es otra cosa')


if __name__ == "__main__":
    run()