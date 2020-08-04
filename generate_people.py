# Importamos las librerías
import unidecode
from faker import Faker

# Inicializamos una instancia de la librería
fake = Faker('es_MX')

# Abre un nuevo archivo y lo deja listo para escribir en él
# La 'w' indica que vamos a escribir (write)
# my_file es la variable con el archivo
with open('cheques.txt', 'w') as my_file:
  for _ in range(50):
    while True:
      name = f'{fake.first_name()} {fake.last_name()} {fake.last_name()}'
      # 'split' divide el string por espacios (holi mundi -> [holi, mundi])
      #'len' nos da el total de elementos
      # El ciclo se rompe cuando el nombre solo tiene 3 partes
      if len(name.split()) == 3: break
      
    unaccented_name = unidecode.unidecode(name) # Quitamos acentos
    date = fake.date()
    quantity = fake.numerify('%#')
    invoice = fake.numerify('%#')
    person = f'{date} {unaccented_name} {quantity} {invoice}\n'
    my_file.write(person)
