# Un programa que con base en un número de segundos, de como salida las horas, minutos y segundos
# Ejemplo: 125 segundos -> 0 horas, 2 minutos, 5 segundos

def transform_seconds(seconds):
    hours = seconds / 3600
    residue_hours = seconds % 3600
    minutes = residue_hours / 60 
    residue = seconds % 60
    print(f'{seconds} segundos es igual a:\nHoras:{int(hours)}, Minutos:{int(minutes)}, Segundos:{residue}  ')

    # hours, residue_hours = divmod(seconds, 3600)
    # minutes, residue_minutes = divmod(residue_hours, 60)
    # residue_hours, seconds_residue = divmod(seconds, 60)
    # print(f'Horas: {hours}, Minutos: {minutes}, Segundos: {seconds_residue}')

if __name__ == "__main__":
    seconds = int(input('Ingresa el tiempo en segundos: '))
    transform_seconds(seconds)