"""
Author: ZhangJin
Date: 2024-05-15 10:34:25
Email: jinzhang.hit@gmail.com
LastEditTime: 2024-05-15 10:34:27
FilePath: \snippets\dict\merge_dicts.py
"""

def merge_dictionaries(*dicts):
    res = {}
    for d in dicts:
        res.update(d)
    return res

ages_one = {
  'Peter': 10,
  'Isabel': 11,
}
ages_two = {
  'Anna': 9
}
merge_dictionaries(ages_one, ages_two)
# { 'Peter': 10, 'Isabel': 11, 'Anna': 9 }