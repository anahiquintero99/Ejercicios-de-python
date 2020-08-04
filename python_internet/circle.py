#Escriba un programa que reciba como entrada el radio de un círculo y entregue como salida su perímetro y su área:

def circle(radio_circle):
    area = 3.1416 * (radio_circle**2)
    perimeter = (2 * 3.1416) * radio_circle
    print(f' Area = {area}\n Perimetro = {perimeter}')


if __name__ == "__main__":
    radio_circle = float(input('ingresa el radio: '))

    circle(radio_circle)