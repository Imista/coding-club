# Los tres lados a, b y c de un triángulo deben satisfacer la desigualdad triangular: cada uno de los lados no puede ser más largo que la suma de los otros dos.
# Escriba un programa que reciba como entrada los tres lados de un triángulo e indique si el triángulo es inválido.

def is_valid_triangle(a, b, c):
    return ((a < b + c) & (b < a + c) & (c < a + b))


if __name__ == "__main__":
    print('--VALID TRIANGLE--')
    side_a, side_b, side_c = input('TYPE SIDE "A": '), input(
        'TYPE SIDE "B": '), input('TYPE SIDE "C": ')
    print(is_valid_triangle(side_a, side_b, side_c))
