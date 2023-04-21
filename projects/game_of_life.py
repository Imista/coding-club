import time
import numpy as np

TABLE_SIZE = 5


def create_table():
    tab = np.zeros((TABLE_SIZE, TABLE_SIZE), np.int0)
    tab[2][1] = 1
    tab[2][2] = 1
    tab[2][3] = 1
    print(tab)
    return tab


if __name__ == "__main__":
    tab = create_table()
    # Iterate cells
    for i, cell in enumerate(tab.flatten()):
        x = (i) // 5
        y = (i) % 5
        # print(f"CELL {i}: {tab[x][y]}")
        
