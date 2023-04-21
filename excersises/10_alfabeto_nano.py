# Convierte una cadena de texto a alphabeto nano

def convert_to_nano(text):
    text = text.upper()
    words_dictionary = {
        "A": "Alfa",
        "B": "Bravo",
        "C": "Charlie",
        "D": "Delta",
        "E": "Echo",
        "F": "Foxtrot",
        "G": "Golf",
        "H": "Hotel",
        "I": "India",
        "J": "Juliett",
        "K": "Kilo",
        "L": "Lima",
        "M": "Mike",
        "N": "November",
        "O": "Oscar",
        "P": "Papa",
        "Q": "Quebec",
        "R": "Romeo",
        "S": "Sierra",
        "T": "Tango",
        "U": "Uniform",
        "V": "Victor",
        "W": "Whiskey",
        "X": "X-Ray",
        "Y": "Yankee",
        "Z": "Zulu",
        "1": "One",
        "2": "Two",
        "3": "Three",
        "4": "Four",
        "5": "Five",
        "6": "Six",
        "7": "Seven",
        "8": "Eight",
        "9": "Nine",
        "0": "Zero",
        ".": "Decimal"
    }
    aux = [words_dictionary[letter]
           for letter in text if letter in words_dictionary]

    return " ".join(get_frecuency(aux))


def get_frecuency(input_list):
    repetitions_list = [
        "double",
        "triple",
        "quadruple",
        "quintuple",
    ]
    res = []
    cont = 0
    for i in range(len(input_list)):
        if i != len(input_list)-1:
            if (input_list[i] == input_list[i + 1] and cont < 4):
                cont += 1
                continue

        if (cont > 0):
            res.append(repetitions_list[cont - 1])

        res.append(input_list[i])
        cont = 0

    return res


if __name__ == "__main__":
    text = input("TYPE YOUR MESSAGE:\t")
    print(convert_to_nano(text))
