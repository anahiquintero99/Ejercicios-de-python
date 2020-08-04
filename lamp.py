

class Lamp:
    _LAMPS = ['''

    \     |     /
     \  , - ,  /
     — (     ) —
        \   /
         |=|
        |   |
    ’’’,
    ’’’
        , - ,
       (     )
        \   /
         |=|
        |   |
    ''']

def __init__(self, is_turned_on):
    self._is_turned_on = is_turned_on

def turned_on(self):
    self._is_turned_on = True
    self._display_image()

def turn_off(self):
    self._is_turned_on = False
    self._display_image()

def _display_image(self):
    if self._is_turned_on:
        print(self._LAMPS[0])
    else:
        print(self._LAMPS[1])


def run():
    lamp = Lamp(_is_turned_on = False)

    while True:
        command = input('''
        
        ¿Que deseas hacer?

            [p] Prender
            [a] Apagar
            [s] Salir

        ''')

        if command == 'p':
            lamp.turned_on()
        elif command == 'a':
            lamp.turn_off()
        else:
            break


if __name__ == "__main__":
    run()