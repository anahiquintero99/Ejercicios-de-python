#Escriba un programa que reciba como entrada las 
# longitudes de los dos catetos a y b de un triángulo rectángulo, 
# y que entregue como salida el largo de la hipotenusa c del triangulo, 
# dado por el teorema de Pitágoras: c2=a2+b2.
import math
def pythagoras(a, b):
    c = math.sqrt((a**2) + (b**2))
    return c

if __name__ == "__main__":
    print('P I T A G O R A S ')
    a = float(input('Ingresa valor de a: '))
    b = float(input('Ingresa valor de b: '))
    answer = pythagoras(a, b)
    print(f'Hipotenusa: {answer}')