def find_index_of_all(lst, fn):
    return [i for i, item in enumerate(lst) if fn(item)]

find_index_of_all([1, 2, 3, 4], lambda n: n % 2 == 1) # [0, 2]