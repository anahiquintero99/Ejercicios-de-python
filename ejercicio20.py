#Imprimir 10 veces la palabra HOLA.

def run():
    x = 0

    while True:
        if x < 10:
            x += 1
            print (f'{x}.- Hola')


if __name__ == "__main__":
    run()
