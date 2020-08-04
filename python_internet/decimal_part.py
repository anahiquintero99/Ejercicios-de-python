#Escriba un programa que entregue la parte
#decimal de un número real ingresado por el usuario.
import math

def decimal_part(number):
    decimal_part, int_part = math.modf(number)
    print(f'Numero: {number}\n Numero entero:{int_part}\n Numero decimal: {decimal_part}')


if __name__ == "__main__":
    print('N U M E R O S  D E C I M A L E S')
    number = float(input('Ingresa numero: '))
    decimal_part(number)