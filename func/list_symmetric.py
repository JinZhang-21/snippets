def symmetric_difference_by(a,b,fn):
    (a_, b_) = (set(map(fn,a)), set(map(fn,b)))
    return [item for item in a if fn(item) not in b_] + [item for item in b if fn(item) not in a_]

from math import floor

print(symmetric_difference_by([2.1, 1.2], [2.3, 3.4], floor)) # [1.2, 3.4]