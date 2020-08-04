 
def operation():
    a = int(input('Valor a: '))
    b = int(input('Valor b: '))

    result = ((a+b)**2)/(3*b)
    print(f'{result}')
    
if __name__ == "__main__":
    print('Ingresa los valores para la formula ((a+b)**2)/(3*b)')
    operation()
