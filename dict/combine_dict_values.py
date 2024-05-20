"""
Author: ZhangJin
Date: 2024-05-12 21:08:16
Email: jinzhang.hit@gmail.com
LastEditTime: 2024-05-12 21:08:45
FilePath: \code\snippets\combine_dict_values.py
"""

# Combine two or more dictionaries, creating a list of values for each key

from collections import defaultdict
def combine_values(*dicts):
    res = defaultdict(list)
    for d in dicts:
        for key, value in d.items():
            res[key].append(value)
    return dict(res)

d1 = {'a': 1, 'b': 'foo', 'c': 400}
d2 = {'a': 3, 'b': 200, 'd': 400}

combine_values(d1, d2) # {'a': [1, 3], 'b': ['foo', 200], 'c': [400], 'd': [400]}