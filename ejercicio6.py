def run():
    total = int(input('Total de dulces: '))
    leftovers = int(input('Sobrantes de dulces: '))
    consumption = total - leftovers
    print (f'El consumo fue: {consumption} dulces')
    print (f'El gasto fue: {consumption * 13} pesos')
    
if __name__ == "__main__":
    print('Ingresa el total de dulces y cuantos sobraron para calcular el consumo y su gasto')
    run()