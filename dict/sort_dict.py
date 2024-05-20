"""
Author: ZhangJin
Date: 2024-05-15 10:41:27
Email: jinzhang.hit@gmail.com
LastEditTime: 2024-05-15 10:41:29
FilePath: \snippets\dict\sort_dict.py
"""

def sort_dict_by_key(d, reverse= False):
    # Use dict() to convert the sorted list back to a dictionary.
    return dict(sorted(d.items(), reverse=reverse))

d = {'one': 1, 'three': 3, 'five': 5, 'two': 2, 'four': 4}
sort_dict_by_key(d) # {'five': 5, 'four': 4, 'one': 1, 'three': 3, 'two': 2}
sort_dict_by_key(d, True)
# {'two': 2, 'three': 3, 'one': 1, 'four': 4, 'five': 5}