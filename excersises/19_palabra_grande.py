# Escribe una función en Python que reciba como parámetro una cadena de texto y devuelva la palabra más larga de la cadena, junto con su longitud. Si hay varias palabras con la misma longitud máxima, devolver la primera que aparece en la cadena.

from functools import reduce
import re


def longest_word(txt):
    longest = reduce(lambda a, b: a if len(a) >= len(b)
                     else b, re.findall(r'\w+', txt))
    return longest, len(longest)


if __name__ == "__main__":
    txt = "La mayoría de las personas no planean fracasar, fracasan por no planear"
    print(longest_word(txt))
