# Tests a value, x, against a testing function, conditionally applying a function.

def when(predicate, fn):
    return lambda x: fn(x) if predicate(x) else x

double_even_numbers = when(lambda x: x % 2 == 0, lambda x : x * 2)
double_even_numbers(2) # 4
double_even_numbers(1) # 1