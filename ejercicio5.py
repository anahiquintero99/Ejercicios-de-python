def calculate():
    base = int(input('Ingresa la base: '))
    height = int(input('Ingresa la altura: '))
    perimeter = (base * 2) + (height * 2) 
    area  = base * height

    print(f'El area es: {area}\n El perimetro es: {perimeter}')
if __name__ == "__main__":
    print('Base y altura del rectangulo')
    calculate()
    