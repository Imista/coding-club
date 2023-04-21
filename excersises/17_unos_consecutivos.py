# Escribe una función llamada "find_max_consecutive_ones" que reciba como parámetro una lista de números (0's y 1's) y devuelva el número máximo de unos consecutivos en la list

def find_max_consecutive_ones(num_list):
    text_num_list = "".join([str(num) for num in num_list])
    consecutive_ones_list = text_num_list.split("0")
    count_consecutive_ones = [len(txt) for txt in consecutive_ones_list]
    return max(count_consecutive_ones)


if __name__ == "__main__":
    num_list = [0, 0, 0, 0, 0, 0]
    print(find_max_consecutive_ones(num_list))
