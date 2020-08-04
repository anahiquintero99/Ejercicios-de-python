import random

IMAGES = ['''

        +---+
        |   |
            |
            |
            |
            |
            =========''', '''
    
        +---+
        |   |
        O   |
            |
            |
            |
            =========''', '''
    
        +---+
        |   |
        O   |
        |   |
            |
            |
            =========''', '''
    
        +---+
        |   |
        O   |
       /|   |
            |
            |
            =========''', '''
        
        +---+
        |   |
        O   |
       /|\  |
            |
            |
            =========''', '''
        
        +---+
        |   |
        O   |
       /|\  |
        |   |
            |
            |
            |
            =========''', '''
        
        +---+
        |   |
        O   |
       /|\  |
        |   |
       /    |
            |
            |
            =========''', '''
        
        +---+
        |   |
        O   |
       /|\  |
        |   |
       / \  |
            |
            |
            =========''', '''
''']

WORDS = [
    'lavadora',
    'secadora',
    'sofa',
    'gobierno',
    'diputado',
    'democracia',
    'computadora',
    'teclado'
]


def random_word():
    # [0, 7] -> 3
    # randint == random integer (inicio, fin) -> (100, 500) => 245
    #idx = random.randint (0, len(WORDS) - 1)
    #return WORDS[idx]
    return random.choice(WORDS)


def display_board(hidden_word, tries):
    print(IMAGES[tries])
    print()
    print(hidden_word)
    print('--- *' * 5)  


def run():
    word = random_word()
    hidden_word = ['-'] * len(word)
    tries = 0

    while True:
        display_board(hidden_word, tries)
        current_letter = str(input('Escoge una letra: '))
    
        letter_indexes = []
        for idx in range (len(word)):
            if word[idx] == current_letter:
                letter_indexes.append(idx)
        
        # [] -> False
        # [1] -> True
        if letter_indexes:
            for idx in letter_indexes:
                hidden_word[idx] = current_letter

            letter_indexes = []

        else: 
            tries += 1
        
            if tries == 7:
                display_board(hidden_word, tries)
                print()
                print(f'¡Perdiste! La palabra corresta es {word}')
                break

        # try:
        #     hidden_word.index('-')
        # except ValueError:
        #     print('')
        #     print(f'¡Felicidades! Ganaste. La palabra es {word}')
        #     break

        if not '-' in hidden_word:
            print()
            print(f'¡Felicidades! Ganaste. La palabra es {word}')
            break

if __name__ == "__main__":
    print('B I E N V E N I D O S  A  A H O R C A D O S')
    run()