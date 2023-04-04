# Escribe una función que reciba una lista de palabras y devuelva un diccionario con cada palabra como clave y el número de veces que aparece en la lista como valor.


def count_repeat_words(words_list):
    res = {}
    for word in set(words_list):
        res[word] = words_list.count(word)

    return res


if __name__ == "__main__":
    text = "python es un lenguaje de programación y es muy popular"
    print(count_repeat_words(text.split()))
