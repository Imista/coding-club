# Desarrolla una función que reciba un array y un numero objetivo y regrese un arreglo con los índices de los dos primeros números que sumen el numero objetivo

def run(numbers, target):
    prev_numbers = {}
    for i, number in enumerate(numbers):
        sub = target - number
        if (sub in prev_numbers):
            print("true")
            return [prev_numbers[sub], i]
        else:
            prev_numbers[number] = i

    print(prev_numbers)

    return


if __name__ == "__main__":
    arr = [2, 7, 11, 15]
    res = run(arr, 18)
    print(res)
