def people_ages ():
    women = 0
    men = 0
    for i in range ( 1, 21):
        age = int(input(f'{i}.-Ingresa edad: '))

        if age >= 25:
            
            gender = int(input(f'''\nIngresa el genero:\n 1) Mujer\n 2) Hombre\n\n'''))
                
            if gender == 1:
                women += 1   
        
            elif gender == 2:
                men += 1   
    
    print (f'Son {women} mujeres mayores de 25\n Son {men} hombres mayores de 25\n En total son {woman+men} mujeres y hombres mayores de 25')

    

if __name__ == "__main__":
    print('Ingresa la edad de 20 personas, cuantas son mayores de 25 y  de ahi, cuantos son mujeres y hombres')
    people_ages()
    
