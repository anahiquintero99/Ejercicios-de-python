# Hacer un programa para administrar una Lista de datos  :

# 1.	Insertar un elemento a la lista
# 2.	Mostrar la lista 
# 3.	Buscar un elemento en la lista por nombre indicando la posición en la que lo encontró
# 4.	Actualizar los datos de un elemento lista 
# 5.	Borrar un elemento de la lista .
# 6.	Ordenar los datos de la Lista
# 7.	Salir

def insert_element(element):
    list_elements.append(element)
    return list_elements



if __name__ == "__main__":

    print('L I S T A S  D E  D A T O S ')

    while True:

        option = int(input('''
    
        1.	Insertar un elemento a la lista
        2.	Mostrar la lista 
        3.	Buscar un elemento en la lista por nombre indicando la posición en la que lo encontró
        4.	Actualizar los datos de un elemento lista 
        5.	Borrar un elemento de la lista .
        6.	Ordenar los datos de la Lista
        7.	Salir

        '''))

        if option == 1:

            list_elements = [] 

            while True:
                element = input('Inserta un numero: ')
                insert_element(element)

                other_element = int(input('''
                
                ¿Deseas agregar otro elemnto a la lista?
                
                [1] Si
                [2] No
                
                '''))

                if other_element == 2:
                    break 

        elif option == 2:
            try:
                print('L I S T A   C R E A D A')
                print_list = (list_elements)
                print(list_elements)
            except NameError:
                print('Aun no creas una lista, ingresa al punto uno para crearla sonso')
        
        elif option == 3:
            print('B U S C A R   E L E M E N T O   E N   L I S T A ')

            try:
                element_found = input('Ingresa elemento a buscar: ')
                position_element = list_elements.index(element_found)
                print(f'El elemento {element_found} se encuentra en la posicion: {position_element}')
            except ValueError:
                print('Elemneto no encontrado en la lista')
        
        # elif option == 4:
        elif option == 5:
            print('E L I M I N A R    E L E M E N T O')
            element_found = input('Ingresa elemento a eliminar: ')
            position_element = list_elements.index(element_found)
            list_elements.pop(position_element)
            print(list_elements)

        elif option == 6:
            list_elements.sort()
            print(list_elements)




