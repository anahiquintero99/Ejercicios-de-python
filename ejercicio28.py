#Los alumnos tuenen 5 materias: se desea saber cuantas aprobadas tienen y cuantas no. 

def subject_students():
    while True:
        option = int(input('¿Deseas saber cuntas asignaturas aprobaste?\n 1)Si\n 2)No\n'))

        if option == 1:
            name = str(input('Ingresa nombre: '))
            
            approved = 0
            reprobate = 0
            
            while True:
                option2 = int(input('¿Deseas ingresar calificacion?\n 1)Si\n 2)No\n'))
                    
                if option2 == 1:
                    subject = int(input('Ingresa la calificacion: '))
                    if subject >= 6:
                        approved += 1
                    else:
                        reprobate += 1
                else: 
                    print (f'El alumno {name}:\n Aprobo {approved} asignaturas.\n Reprobo {reprobate} asignaturas')
                    break
        else:
            break

if __name__ == "__main__":
    subject_students()