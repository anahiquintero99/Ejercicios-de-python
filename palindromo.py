
def palindrome2(word):
    reversed_word = word[::-1]

    if reversed_word == word:
        return True

    return False

    
def palindrome(word):
    reversed_letter = []
    
    for letter in word:
        reversed_letter.insert (0, letter)
    
    reversed_word = ''.join(reversed_letter) 

    if reversed_word == word:
        return True

    return False
if __name__ == "__main__":
    word = str(input('Escribe una palabra: '))

    result = palindrome2(word)
    
    if result is True:
        print(f'{word} es un palindromo')
    else: 
        print(f'{word} no es un palindromo')
