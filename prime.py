def is_prime(number):
    if number < 2:
        return False
    elif number == 2:
        return True
    elif number > 2 and number % 2 == 0:
        return False
    else:
        for i in range(3, number): #
            if number % i == 0:
                return False
            else:
                return True

def run ():
    number = int(input('Escribe número: '))
    result = is_prime(number)

    if result is True:
        print('El numero es primo')
    else:
        print('El numero no es primo')

if __name__ == '_main_':
    run()