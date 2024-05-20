"""
Author: ZhangJin
Date: 2024-05-13 10:33:07
Email: jinzhang.hit@gmail.com
LastEditTime: 2024-05-13 10:33:10
FilePath: \snippets\dict\get_nested_values.py
"""

from functools import reduce
from operator import getitem

def get(d, selectors):
    # reduce: 迭代selectors列表
    # 对 selectors 中的每个键应用 operator.getitem() ，检索要用作下一次迭代的迭代对象的值。
    return reduce(getitem, selectors, d)

users = {
  'freddy': {
    'name': {
      'first': 'fred',
      'last': 'smith'
    },
    'postIds': [1, 2, 3]
  }
}
get(users, ['freddy', 'name', 'last']) # 'smith'
get(users, ['freddy', 'postIds', 1]) # 2