#Escriba un programa que pregunte al usuario la hora actual t del reloj y un número 
# entero de horas h, que indique qué hora marcará el reloj dentro de h horas:

def future_time(current_number, number_hours):
    number_total = current_number + number_hours
    return number_total % 24


if __name__ == "__main__":
    print('H O R A  F U T U R A')
    while True:
        option = int(input('''
        
        Ingresar hora:
        1)Si
        2)No

        '''))
        if option == 1:
            current_number = int(input('Ingresa hora actual: '))
            number_hours = int(input('Ingresa la cantidad de horas: '))
            answer = future_time(current_number, number_hours)
            print(f'En {number_hours} horas, el reloj marcara las {answer}:00')
        else:
            break