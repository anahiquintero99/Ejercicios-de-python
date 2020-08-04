#Recibe 5 numeros e indique cuantos son impares y cuantos son par

def pair_odd():
    pair = 0
    odd = 0
    for number in range (5):
        numbers = int(input('Ingresa numero: '))
        if numbers % 2 == 0:
            pair += 1
        else: 
            odd += 1
    print(f'Pares = {pair}\nImpares = {odd} ')

if __name__ == "__main__":
    pair_odd()