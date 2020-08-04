#Escriba un programa que pida al usuario un entero de tres dígitos.
#Entregue el número con los dígitos en orden inverso.

def inverted_number(number):
    list_number = list(number)
    return list_number[::-1]

if __name__ == "__main__":
    number = input('Ingresa numero de tres digitos: ')

    new_number = inverted_number(number)
    print(''.join(new_number))