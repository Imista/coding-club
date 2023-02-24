# Generar una función que reciba un frase y la devuelva con la primer letra de cada palabra en mayusculas

def run():
    text = input("INGRESA UNA CADENA:\t")
    res = " ".join(text.split()).title()
    print("Su cadena es:\t", res)


if __name__ == "__main__":
    run()
