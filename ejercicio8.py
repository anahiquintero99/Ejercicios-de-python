def degrees():
    degreesc = int(input('Ingresa grados celsious: '))
    degreesf = (degreesc * (9/5) ) + 32 
    degreesc = (degreesf - 32 ) * (5/9)
    print(f' {degreesf} farenheit = {degreesc} celsious')

if __name__ == "__main__":
    print('Convierte grados celsious a fahrenheit')
    degrees()
