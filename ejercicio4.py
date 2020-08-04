def power():
    number = int(input('Ingresa número: '))
    squeare = pow(number, 2)
    cube = pow(number, 3)
    fifth = pow(number, 5)

    print (f'Cuadradon = {squeare}\n Cubo = {cube}\n Quinta = {fifth}')

if __name__ == "__main__":
    print('Calcular el cuadrado , el cubo y la quinta de un numero')
    power()
