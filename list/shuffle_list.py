from copy import deepcopy
from random import randint

def shuffle(lst):
    temp_list = deepcopy(lst)
    m = len(temp_list)
    while (m):
        m -= 1
        i = randint(0, m)
        temp_list[m], temp_list[i] = temp_list[i], temp_list[m]
    return temp_list

foo = [1, 2, 3]
shuffle(foo) # [2, 3, 1], foo = [1, 2, 3]
from random import shuffle
shuffle(foo) # [3, 1, 2], foo = [3, 1, 2]
