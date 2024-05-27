def intersection(a,b):
    return list(set(a) & set(b))

def union(a,b):
    return list(set(a) | set(b))
    # return list(set(a+b)) 

intersection([1, 2, 3], [1, 2, 4])  # [1, 2]

union([1, 2, 3], [1, 2, 4])  # [1, 2, 3, 4]
