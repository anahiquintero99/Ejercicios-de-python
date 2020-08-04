

KEYS = {
    'a':'w',
    'b':'E',
    'c':'x',
    'd':'l',
    'f':'a',
    'g':'0',
    'h':'C',
    'i':'b',
    'j':'!',
    'k':'z',
    'l':'8',
    'm':'M',
    'n':'I',
    'o':'d',
    'p':'.',
    'q':'U',
    'r':'Y',
    's':'i',
    't':'3',
    'u':',',
    'v':'J',
    'w':'N',
    'x':'f',
    'y':'m',
    'z':'W',
    'A':'G',
    'B':'S',
    'C':'j',
    'D':'n',
    'F':'Q',
    'G':'o',
    'H':'e',
    'I':'u',
    'J':'g',
    'K':'2',
    'L':'9',
    'M':'A',
    'N':'5',
    'O':'4',
    'P':'?',
    'Q':'c',
    'R':'r',
    'S':'O',
    'T':'p',
    'U':'h',
    'V':'6',
    'W':'q',
    'X':'H',
    'Y':'R',
    'Z':'l',
    '0':'k',
    '1':'7',
    '2':'X',
    '3':'L',
    '4':'p',
    '5':'v',
    '6':'T',
    '7':'V',
    '8':'y',
    '9':'K',
    '.':'Z',
    ',':'D',
    '?':'F',
    '!':'B',
    ' ':' ',
}

def cypher(message):
    words = message.split() # 'te amo fer' -> ['te', 'amo', 'fer']
    cypher_message = [] # Aqui se van a guardar todas las palabras cifradas
    # se crea antes, para poder agregarlas

    for word in words: # te
        cypher_word = ''
        for letter in word:
            # t -> X
            # e -> s
            cypher_word += KEYS[letter]
            # 'X'
            # 'Xs'
        
        cypher_message.append(cypher_word) # ['Xs', 'qio', 'zxc']
    
    return ' '.join(cypher_message) # ['Xs', 'qio', 'zxc'] -> 'Xs qio zxc'


def decipher(message):
    # Por defecto, separa por espacio
    words = message.split() # 'Xs qio zxc' -> ['Xs', 'qio', 'zxc']
    decypher_message = []

    for word in words: # 'Xs'
        decipher_word = ''

        for letter in word:
            # 'X' -> 't'
            # 's' -> 'e'
            #                              key value                key  value
            #   ('t', 'X')
            for key, value in KEYS.items(): # { 't': 'X', 'e': 's } -> ( ('t', 'X'), ('e', 's') )
                #  'X' == 'X'
                if value == letter:
                    decipher_word += key # 't'

                    # 't'
                    # 'te'
        
        decypher_message.append(decipher_word) # ['te', 'amo', 'fer']

    return ' '.join(decypher_message) # ['te', 'amo', 'fer'] -> 'te amo fer'

def run():
    while True:
        command = str(input('''--- * --- * --- * --- * --- * --- * --- * ---
                    
            Bienvenido a criptografia. ¿Que deseas hacer?
            
            [c] cifrar mensaje
            [d] decifrar mensaje
            [s] salir 

            '''))

        if command == 'c':
            message = str(input('Escribe tu mensaje: '))
            cypher_message = cypher(message)
            print(cypher_message)

        elif command == 'd':
            message = str (input('Escribe tu mensaje cifrado: '))
            decypher_message = decipher(message)
            print(decypher_message)

        elif command == 's':
            print('Salir')
        else:
            print('¡Comando no encontrado')

if __name__ == "__main__":
    print('M E N S A J E S  C I F R A D O S')
    run()