#Calcule el sueldo nuevo de 5 empleados, considerado como reglas que si:
#El empleado gana mas de 6.000 pesos, su incremento sera de 50%, si ganad menos , el incremento es del 100%

def prom_salary():
     while True:
        answer = str(input('¿Deseas calcular sueldo de emplead?\n Si\n No\n'))
        if answer == 'si':
            salary = float(input('Salario del empleado: '))
            if salary > 6000:
                new_salary = salary * 1.5 
                print(f'El sueldo nuevo es: {new_salary}')
            else: 
                new_salary = salary * 2
                print(f'El sueldo nuevo es: {new_salary}')
        else:
            break

if __name__ == "__main__":
    prom_salary()