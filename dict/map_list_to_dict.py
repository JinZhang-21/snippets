"""
Author: ZhangJin
Date: 2024-05-13 10:39:50
Email: jinzhang.hit@gmail.com
LastEditTime: 2024-05-13 10:39:54
FilePath: \snippets\dict\map_list_to_dict.py
"""

def map_dictionary(itr, fn):
    """[]列表是一个可迭代对象, map返回一个迭代器, 包含了应用fn的结果
    使用 zip(itr, map(fn, itr)) 将原始迭代器 itr 中的每个元素与应用函数后的结果配对，生成一个包含成对元素的迭代器
    """
    # Use map() to apply fn to each value of the list.
    # Use zip() to pair original values to the values produced by fn.
    # Use dict() to return an appropriate dictionary.
    return dict(zip(itr, map(fn, itr)))

map_dictionary([1, 2, 3], lambda x: x * x) # { 1: 1, 2: 4, 3: 9 }