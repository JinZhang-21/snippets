from itertools import chain, combinations

"""chain(*iterables) 将多个可迭代对象连接成单一的迭代器
Example: chain([1, 2], "abc") -> 1, 2, 'a', 'b', 'c', list(chain([1, 2], "abc")) -> [1, 2, 'a', 'b', 'c']
"""

"""Summary: combinations(iterable, r) returns all possible r-length tuples of elements in the iterable
Example: conbinations("Hey", 2) -> ('H', 'e'), ('H', 'y'), ('e', 'y')
    """


def powerset(iterable):
    s = list(iterable)
    return list(
        # chain.from_iterable() flattens the list of tuples into a single list
        chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
    )

powerset([1, 2]) # [(), (1,), (2,), (1, 2)]