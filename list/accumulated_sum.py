from itertools import accumulate

def partial_sum(iterable):
    return list(accumulate(iterable))

partial_sum(range(0, 15, 3)) # [0, 3, 9, 18, 30]