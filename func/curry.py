# Use functools.partial() to return a new partial object which behaves like fn with the given arguments, args, partially applied.
from functools import partial

def curry(fn, *args):
    return partial(fn, *args)

add = lambda x, y: x + y
add10 = curry(add, 10)
add10(20) # 30