#

def shortest_string_lenght(my_string):
    LIMIT = len(my_string) % 2
    while True:
        current_lenght = len(my_string)

        if current_lenght > LIMIT and my_string[0] != my_string[-1]:
            my_string = my_string[1:current_lenght - 1]
        else:
            return current_lenght


if __name__ == "__main__":
    my_string = "1010110"
    print(shortest_string_lenght(my_string))
