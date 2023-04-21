# Dado una cadena de caracteres s, encuentra la longitud de la subcadena más larga  que no contenga caracteres repetidos.

def longest_substring(text):
    counts = []
    substring = ""
    count = 0
    for x in text:
        if x not in substring:
            count += 1
            substring += x
        else:
            counts.append(count)
            substring = ""
            count = 0

    counts.append(count)
    return max(counts)


if __name__ == "__main__":
    text = "pwwkew"
    print(longest_substring(text))
