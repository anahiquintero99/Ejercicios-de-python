# Escriba un programa que convierta de centímetros a pulgadas. Una pulgada es igual a 2.54 centímetros.

def conversion(centimeters):
    inch = centimeters / 2.54

    return inch

if __name__ == "__main__":
    print('C E N T I M E T R O S  A  P U L G A D A S ')
    centimeters = float(input('Centimetros: '))
    answer =conversion(centimeters)
    print(f'{centimeters} centimetros = {answer} pulgadas')
