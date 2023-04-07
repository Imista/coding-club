# Escribe una función llamada reverse_words que reciba como parámetro una cadena de texto. La función debe invertir el orden de las palabras en la cadena, dejando el  orden de los caracteres dentro de cada palabra intacto

def reverse_words(text):
    words = text.split()
    res = words[::-1]
    return " ".join(res)


if __name__ == "__main__":
    text = "La lluvia en Sevilla es una maravilla!"
    print(reverse_words(text))
