def get_average(list_notes):
    #sum_of_cal = 0
    #for cal in list_notes:
    #    sum_of_cal += cal
    
    #return sum_of_cal / len(list_notes)
    return sum(list_notes) / len(list_notes)
    
if __name__ == "__main__":

    print('Promedio de Alumnos')
    
    list_notes = []

    for cal in range (1, 6):
        cal = int(input('Ingresa la calificacion: '))
        list_notes.append(cal)

    average = get_average(list_notes)
    print(f'El promedio del alumno es: {average}')