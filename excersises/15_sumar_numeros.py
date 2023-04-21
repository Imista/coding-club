# Escribe una función llamada sum_reverse_numbers que recibe dos listas de números como parámetros. Los elementos de cada lista representan un número en orden inverso, es decir, el primer elemento es el dígito menos significativo y el último es el más significativo. La función debe sumar ambos números y devolver el resultado como una lista en orden inverso

def sum_reverse_numbers(num_a_list, num_b_list):
    num_a = int("".join(map(str, reversed(num_a_list))))
    num_b = int("".join(map(str, reversed(num_b_list))))

    num_result = num_a + num_b
    return list(map(int, reversed(str(num_result))))


if __name__ == "__main__":
    num_a_list = [9, 9, 9]
    num_b_list = [1, 0, 0, 0]
    print(sum_reverse_numbers(num_a_list, num_b_list))
