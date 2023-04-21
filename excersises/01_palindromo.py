# Realiza una funcion que reciba como parámetro una palabra y devuelva si es palindroma.

def is_palindrome(word):
    cleanWord = word.replace(" ", "").lower()
    return cleanWord == cleanWord[::-1]


if __name__ == "__main__":
    print('--PALINDROME WORD--')
    word = input('TYPE YOUR WORD: ')
    print(is_palindrome(word))
