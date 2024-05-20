# What is the difference between list.sort() and sorted() in Python?
# list.sort is built-in method in list
# sorted() is a built-in func

"""
1.
    list.sort() changes the list inplace and returns None
    sorted() returns a new list and does not change the original list
2.
    sorted() accepts any iterable and returns a list
    list.sort() is a list method and only works on lists
"""


nums = [2, 3, 1, 5, 6, 4, 0]

print(sorted(nums))   # [0, 1, 2, 3, 4, 5, 6]
print(nums)           # [2, 3, 1, 5, 6, 4, 0]

print(nums.sort())    # None
print(nums)           # [0, 1, 2, 3, 4, 5, 6]