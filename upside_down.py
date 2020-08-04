def upside_down(word):
    list_word = [word]
    for letter in range(len(word)-1, -1, -1):
        print(word[letter], end=" ")



if __name__ == "__main__":
    print('P A L A B R A S   A L   R E V E S ')
    word = input('Ingresa palabra: ')
    upside_down(word)