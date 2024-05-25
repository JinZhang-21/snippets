def every(lst, fn=lambda x: x):
    # all(): Return True if bool(x) is True for all values x in the iterable.
    return all(map(fn, lst))

every([4, 2, 3], lambda x: x > 1) # True
every([1, 2, 3]) # True