import time

SECRET_WORD = 'cctmexico'  # In uppercase because it is a constant
your_word = ''
lives = 5

name = input("¿Como te llamas? ")
print(f"Hola {name}. Es hora de jugar al ahorcado \n")
time.sleep(1)
print("Comienza a adivinar...")
time.sleep(0.5)

# It is not necessary to explicitly check `lives > 0`
# because zero is a falsy value (is evaluated as False) 
# and any other number is evaluated as True
# i.e.  lives = 5 -> True
#       lives = 0 -> False
while lives:
    fails = 0
    for letter in SECRET_WORD:
        if letter in your_word:
            print(letter, end=" ")
        else:
            print("_", end=" ")
            fails += 1

    if fails == 0:
        print("\n\nFelicidades, ganaste")
        break

    your_letter = input("\nIntroduce una letra: ")
    your_word += your_letter  # Concatenate new letter to save it

    if your_letter not in SECRET_WORD:
        lives -= 1
        print("\nTe equivocaste")
        print(f"Tù tienes {lives} vida(s)")

    if lives:
        print("\nGracias por participar")
    else:
        print("\nPerdiste")
        
            