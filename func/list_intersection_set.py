def intersection_by(a, b, fn):
    b_ = set(map(fn, b))
    return [item for item in a if fn(item) in b_]

from math import floor

from math import floor

intersection_by([2.1, 1.2], [2.3, 3.4], floor) # [2.1]