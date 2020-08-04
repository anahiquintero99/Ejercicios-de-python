#Calcular el numero mayor de una serie de numeros

def bigger_number(list_numbers):
    print(list_numbers)
    list_numbers.sort()
    print(list_numbers)
    print(','.join(list_numbers))


    # 1. print(list_numbers[5])
    print(f'El numero mayor es: {list_numbers[-1]}') #the best
    # 3. list_numbers[len(list_numbers) - 1]
    # 4. list_numbers.pop()

    # bigger_number  = max(list_numbers)
    # print(f'El numero mas granbde es: {bigger_number}')
    

if __name__ == "__main__":
    list_numbers = []
    for number in range(5):
        numbers = input('Ingresa numero: ')
        list_numbers.append(numbers)
    
    bigger_number(list_numbers)