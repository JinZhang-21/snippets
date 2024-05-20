"""
Author: ZhangJin
Date: 2024-05-12 21:25:45
Email: jinzhang.hit@gmail.com
LastEditTime: 2024-05-12 21:29:47
FilePath: \code\snippets\list\group_list_elements.py
"""

from collections import defaultdict
from math import floor

def group_by(lst, fn):
    d = defaultdict(list)
    for el in lst:
        d[fn(el)].append(el)
    return dict(d)

group_by([6.1, 4.2, 6.3], floor) # {4: [4.2], 6: [6.1, 6.3]}
group_by(['one', 'two', 'three'], len) # {3: ['one', 'two'], 5: ['three']}