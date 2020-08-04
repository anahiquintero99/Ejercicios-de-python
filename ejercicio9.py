def positive_or_negative():
    number = int(input('Ingresa numero: '))

    if number == 0:
        print('El numero es cero')
    elif number < 0:
        print('El numero es negativo')
    else:
        print('El numero es positivo')

if __name__ == "__main__":
    print('Ingresa un numero para saber si es cero, positivo o negativo')
    positive_or_negative()