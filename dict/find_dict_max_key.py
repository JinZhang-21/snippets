def key_of_max(d):
    return max(d, key=d.get)

def key_of_min(d):
    return min(d, key=d.get)

key_of_min({'a':4, 'b':0, 'c':13}) # b
key_of_max({'a':4, 'b':0, 'c':13}) # c