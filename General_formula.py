#Resolver una ecuación de segundo grado; utilizando la fórmula: x=-b+/ (b)(b) - 4(a)(c)/2*(a) 
import math 

def general_formula(a, b, c):
    x1 = (-b + math.sqrt( (b**2) - 4 (a)(c)/ (2 * a)))
    x2 = (-b - math.sqrt( (b**2) - 4 (a)(c)/ 2*(a)))

    return x1, x2


if __name__ == "__main__":
    print('F O R M U L A   G E N E R A L')
    print('Ingresa los valores para obtener x1 y x2 de la formula general.')

    a = int(input('Valor a: '))
    b = int(input('Valor b: '))
    c = int(input('Valor c: '))

    answer = general_formula(a, b, c)

    print(f' x1= {x1}\nx2={x2}')