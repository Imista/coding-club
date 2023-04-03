import re

# Escribe una función en Python que reciba una cadena de texto y valide si cumple con los requisitos para ser una contraseña segura


def validate_password(password):
    is_long = len(password) >= 8
    have_upper = bool(re.search("[A-Z]", password))
    have_lower = bool(re.search("[a-z]", password))
    have_number = bool(re.search("[0-9]", password))
    return is_long & have_lower & have_upper & have_number


if __name__ == "__main__":
    password = input("TYPE YOUR PASSWORD:\t")

    if validate_password(password):
        print("VALID PASSWORD.")
    else:
        print("INVALID PASSWORD.")
