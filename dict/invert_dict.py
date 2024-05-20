"""
Author: ZhangJin
Date: 2024-05-12 21:03:24
Email: jinzhang.hit@gmail.com
LastEditTime: 2024-05-12 21:03:43
FilePath: \code\snippets\Invert_dict.py
"""

# 反转具有非唯一可哈希值的字典: 也就是对于特定的值，可能有多个键

from collections import defaultdict
def collect_dictionary(obj):
    inv_obj = defaultdict(list) # 默认不存在的键，返回一个空列表
    for key, value in obj.items():
        inv_obj[value].append(key)
    return inv_obj

# Example
ages = {
    'Peter': 10,
    'Isabel': 10,
    'Anna': 9,
}
collect_dictionary(ages) # {10: ['Peter', 'Isabel'], 9: ['Anna']}