#Escriba un programa que calcule el promedio de 4 notas ingresadas por el usuario:

def average(list_notes):
    return sum(list_notes) / len(list_notes)
    

if __name__ == "__main__":

    list_notes = []

    for notes in range (4):
        notes = int(input('Ingresa la calificacion: '))
        list_notes.append(notes)
    average = average(list_notes)
    
    print(f'El promedio es : average')