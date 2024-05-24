def find_last(lst, fn):
    return next(item for item in lst[::-1] if fn(item))

find_last([1, 2, 3, 4], lambda n: n % 2 == 1) # 3