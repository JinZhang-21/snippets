from collections import Counter

def is_perm(objs1, objs2):
    return len(objs1) == len(objs2) and Counter(objs1) == Counter(objs2)

is_perm([1, 2, 3], [4, 1, 6]) # False
is_perm([1, 2], [2, 1]) # True

is_perm("dad", "add") # True
is_perm("snack", "track") # False