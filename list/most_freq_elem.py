def most_frequent(lst):
    return max(set(lst), key=lst.count) # ,count 是一个函数，返回元素在列表中出现的次数

most_frequent([1, 2, 1, 2, 3, 2, 1, 4, 2]) #2