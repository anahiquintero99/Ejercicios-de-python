def area():
    base = int(input('Ingresa la base: '))
    height = int (input('Ingresa la altura: '))
    area = (base * height) / 2
    print(f' La area es : {area}')

if __name__ == "__main__":
    print('Area del triangulo')
    area()