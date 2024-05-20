from collections import defaultdict
from math import floor

def count_by(lst, fn = lambda x: x):
    counts = defaultdict(int)
    for val in map(fn, lst):
        counts[val] += 1
    return dict(counts)

count_by([6.1, 4.2, 6.3], floor) # {6: 2, 4: 1}
count_by(['one', 'two', 'three'], len) # {3: 2, 5: 1}