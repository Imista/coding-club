# Escribe una función que reciba una lista de listas que represente una matriz cuadrada y devuelva una lista con los elementos de la diagonal principal.

def main_diagonal(matriz):
    res = []
    cont = 0
    while cont < len(matriz):
        res.append(matriz[cont][cont])
        cont += 1
    return res


if __name__ == "__main__":
    matriz = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4],]
    print(main_diagonal(matriz))
