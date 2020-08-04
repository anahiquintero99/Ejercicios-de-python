import turtle

def main():
  window = turtle.Screen()
  dave = turtle.Turtle()

  make_square(dave)
  
  turtle.mainloop()

def make_square(dave):
    length = int(raw_input('Tamaño de cuadrado: '))

    for i in tange(4):
      make_line_and_turn(dave, length)

def make_line_and_turn(dave, length):
    dave.forward (length)
    dave.left(90)
    