"""
Author: ZhangJin
Date: 2024-05-13 10:30:02
Email: jinzhang.hit@gmail.com
LastEditTime: 2024-05-13 10:33:37
FilePath: \snippets\dict\sort_dict_by_values.py
"""


def sort_dict_by_value(d, reverse=False):
    """字典值必须为同一类型，否则会引发异常"""
    # 使用 dict.items() 从 d 获取元组对列表
    # 使用 dict() 将排序的元组对列表转换回字典
    return dict(sorted(d.items(), key=lambda x: x[1], reverse=reverse))


d = {"one": 1, "three": 3, "five": 5, "two": 2, "four": 4}
sort_dict_by_value(d)  # {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
sort_dict_by_value(d, True)
# {'five': 5, 'four': 4, 'three': 3, 'two': 2, 'one': 1}
