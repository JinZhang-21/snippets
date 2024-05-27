def check_duplicates(lst):
    return len(lst) == len(set(lst))

check_duplicates([1, 2, 3, 4, 5, 5])  # False