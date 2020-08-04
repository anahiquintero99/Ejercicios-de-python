import os, platform # siempre hay que importar las librerías necesarias

def menu():
    # Verificamos si estamos en Windows
    # porque los comandos cambian
    if platform.platform() == 'win32':
        os.system('cls')
    else:
        os.system('clear')
    
    print ("Selecciona una opción")
    print ("\ta - Union KUL")
    print ("\tb - Interseccion K&L")
    print ("\tc - Diferencia K-L")
    print ("\td - Diferencia L-K")
    print ("\te - Combinacion K y L")
    print ("\tf - Salir") 

while True:
    # Mostramos el menu
    menu()
    k =  {  7,  18,   3,  10 }
    l =  {  3,   6,   9,   7 }

    # solicituamos una opción al usuario
    opcionMenu = input("\nInserta una letra: >> ")

    if opcionMenu=="a":
        print (l)
        print (k)
        kul = k|l
        print(kul)
    elif opcionMenu=="b":
        knl = k&l
        print(knl)
    elif opcionMenu=="c":
        k_l = k-l
        print(k_l)
    elif opcionMenu=="d":
        l_k = l-k
        print(l_k)
    elif opcionMenu=="e":
        kyl = (k,l)
        print (kyl)
    elif opcionMenu=="f":
        print('\nBye \(ºvº).')
        break

    else:
        print("\nNo has pulsado ninguna opción correcta.")

    input('\nPulsa enter para continuar...')