import time
from random import *
from copy import deepcopy
import matplotlib.pyplot as plt
import matplotlib.animation as animation

universe = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
]

universe = [
    [0, 1, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 1, 0],
    [0, 1, 1, 1, 0, 1],
    [0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 1, 0],
]
# universe = [
#     [0, 0, 0, 0, 0],
#     [0, 0, 1, 0, 0],
#     [0, 0, 1, 0, 0],
#     [0, 0, 1, 0, 0],
#     [0, 0, 0, 0, 0],
# ]


def get_neibourgs(x, y):
    is_alive = universe[y][x]
    list_n = []
    for ii in range(-1, 2):
        for j in range(-1, 2):
            try:
                if not (y + ii == y and x + j == x):
                    if y + ii >= 0 and x + j >= 0:
                        cell = universe[y + ii][x + j]
                        list_n.append(cell)
            except:
                pass
    # print(list_n, x, y)
    if is_alive == 1:
        l = len([c for c in list_n if c == 1])
        if l == 2 or l == 3:
            return 1
        else:
            return 0
    else:
        l = len([c for c in list_n if c == 1])
        if l == 3:
            return 1
        else:
            return 0


for i in range(20):
    new_universe = deepcopy(universe)
    for b, y in enumerate(universe):
        for a, x in enumerate(y):
            new_universe[b][a] = get_neibourgs(a, b)

    universe = deepcopy(new_universe)
    plt.imshow(universe, cmap='binary')
    plt.show()
    time.sleep(0.25)