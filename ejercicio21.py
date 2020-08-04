#Genera una tabla de equivalencia entre grados fahrenheit y celsious.
#El rango de temperatura es de -10 a 50 grados celsious.

def run():
    gradosc = -10

    while True:
        if gradosc <= 50: 
            gradosf = (gradosc * (9/5)) + 32
            print(f'{gradosc} = {gradosf}')
            gradosc += 1

if __name__ == "__main__":
    run()
    