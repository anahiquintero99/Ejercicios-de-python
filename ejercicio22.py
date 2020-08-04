#CONVERTIR UN NUMERO ENTRE EL 1 AL 5, EN SU EQUIVALENTE EN LETRA. 

def name_numbers():
    
    while True:
        option = int(input('''
            
                Bienvenido a traduccion de numero.
                Ingresa un numero del 1 al 5.
                [0] Presiona s para salir

            '''))
        if option == 1:
            print("Uno")
        elif option == 2:
            print('Dos')
        elif option == 3:
            print('Tres')
        elif option == 4:
            print('Cuatro')
        elif option == 5:
            print('Cinco')
        elif option == 0:
            break
        else:
            print('No es un numero del 1 al 5')

if __name__ == "__main__":

    name_numbers()
