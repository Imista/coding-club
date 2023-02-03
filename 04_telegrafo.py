import string
import functools

# Se debe calcular el costo de un mensaje para enviarlo por telégrafo. Para esto se sabe que cada letra cuesta $1, los caracteres especiales que no sean letras cuestan $3 y los dígitos tienen un valor de $2 cada uno. Los espacios no tienen valor y las letras del castellano (ñ, á, é, í, ó, ú) se consideran caracteres especiales.


def calculate_cost(x: str):
    if (x.isspace()):
        return 0
    elif (x in string.ascii_letters):
        return 1
    elif (x in string.digits):
        return 2
    else:
        return 3


if __name__ == "__main__":
    message = input('TYPE YOUR MESSAGE: ')
    value = functools.reduce(lambda acum, x: acum +
                             calculate_cost(x), message, 0)

    print(f"Your message cost: ${value}")
