#Escriba un programa que pida al usuario que escriba su nombre, y lo salude llamándolo por su nombre.
def greeting(name):
    print(f' Hello, {name}\n How are you?')


if __name__ == "__main__":
    name = str(input('Ingres tu nombre: '))

    greeting(name)