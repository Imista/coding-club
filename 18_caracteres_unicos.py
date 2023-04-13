# Escribe una función llamada "get_unique_chars" que reciba como parámetro una cadena de texto y devuelva una lista de todos los caracteres únicos que aparecen en la cadena

def get_unique_chars(text):
    return sorted(set(text) - set(" "))


if __name__ == "__main__":
    text = "hola mundo"
    print(get_unique_chars(text))
