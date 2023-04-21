# La función debe aceptar una cadena y un número entero como entrada y devolver la cadena cifrada. El cifrado de César es un cifrado de sustitución en el que cada letra en el texto original se desplaza hacia la derecha en el alfabeto por un número fijo de posiciones.

import string


def cifrado(text, displacements):
    alphabet = string.ascii_lowercase
    key = alphabet[displacements:] + alphabet[:displacements + 1]
    parser = {a: b for a, b in zip(alphabet, key)}

    return "".join(list(map(lambda x: parser[x], text)))


if __name__ == "__main__":
    text, displacements = input("TYPE YOUR TEXT:\t").lower(), int(input(
        "TYPE DISPLACEMENTS NUMBER:\t"))
    res = cifrado(text, displacements)
    print(res)
