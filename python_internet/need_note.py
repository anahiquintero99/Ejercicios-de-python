#Un alumno desea saber que nota necesita en el tercer certamen para aprobar un ramo.
# El promedio del ramo se calcula con la siguiente formula.
# NC=(C1+C2+C3)3
# NF=NC⋅0.7+NL⋅0.3
# Donde NC es el promedio de certámenes, NL el promedio de laboratorio y NF la nota final.
# Escriba un programa que pregunte al usuario las notas de los dos primeros certamen y la 
# de laboratorio, y muestre la nota que necesita el alumno para aprobar el ramo con nota 
# final 60.

def need_note(c1, c2, nl):
    nc = (60 - (nl * 0.3))/0.7
    return (nc*3)-(c1+c2)

if __name__ == "__main__":
    c1 = float(input('Ingrese nota certamen 1: '))
    c2 = float(input('Ingrese nota certamen 2: '))
    nl = float(input('Ingrese nota laboratorio: '))
    answer = need_note(c1, c2, nl)
    print(answer)