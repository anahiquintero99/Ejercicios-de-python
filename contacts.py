import csv

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class ContactBook:
    def __init__(self):
        self._contacts = []

    def add(self, name, phone, email):
        contact = Contact(name, phone, email)
        self._contacts.append(contact)
        self._save()

    def show_all(self):
        for contact in self._contacts:
            self._print_contact(contact)
    
    def delete(self, name):
        for idx, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                del  self._contacts[idx]
                self._save()
                break

    def search(self, name):
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                self._print_contact(contact)
                break
        else:
            self._not_found()

    def _save(self):
        with open('contacts.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow( ('name', 'phone', 'email') )

            for contact in self._contacts:
                writer.writerow( (contact.name, contact.phone, contact.email) )

    def _print_contact(self, contact):
        print('--- * --- * --- * --- * --- * --- * --- * ---')
        print(f'Nombre: {contact.name}')
        print(f'Telefono: {contact.phone}')
        print(f'Email: {contact.email}')
        print('--- * --- * --- * --- * --- * --- * --- * ---')


    def _not_found(self):
        print('¡No encontrado!')

def run():

    contact_book = ContactBook()

    with open('contacts.csv', 'r') as f:
        reader = csv.reader(f)
        for idx, row in enumerate(reader):
            if idx == 0:
                continue
            try:
                contact_book.add(row[0], row[1], row[2])
            except IndexError:
                pass


    while True:
        command = str(input('''
        
        ¿Que deseas hacer?

        [a] Añadir contacto
        [ac] Actualizar contacto
        [b] Buscar contacto
        [e] Eliminar contecato}
        [l] Lista de contactos
        [s] Salir
        
        '''))

        if command == 'a':
            print('Añadir contacto')
            name = str(input('Nombre del contacto: '))
            phone = str(input('Numero del contacto: '))
            email = str(input('Email de contacto: '))

            contact_book.add(name, phone, email)

        elif command == 'ac':
            print('Actualizar contacto')
            name = str(input('Nombre del contacto: '))

        elif command == 'b':
            print('Buscar contacto')
            name = str(input('Nombre del contacto: '))

            contact_book.search(name)

        elif command == 'e':
            print('Eliminar contacto')
            name = str(input('Nombre del contacto: '))

            contact_book.delete(name)

        elif command == 'l':
            print('Lista de contactos')
            contact_book.show_all()

        elif command == 's':
            break
        else:
            print('Comando no encontrado')

if __name__ == "__main__":
    print('B I E N V E N I D O  A  L A  A G E N D A')
    run()