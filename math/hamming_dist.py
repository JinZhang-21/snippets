def hamming_dist(a,b):
    return bin(a^b).count('1')

hamming_dist(2,3) # 1