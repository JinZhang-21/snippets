from math import sqrt

def is_prime(n):
    if n<=1 or (n>2 and n%2==0):
        return False
    return all(n % i for i in range(3, int(sqrt(n))+1, 2))

is_prime(7) # True