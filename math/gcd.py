from functools import reduce
from math import gcd as gcd_

def gcd(numbers):
    return reduce(gcd_, numbers)

gcd([8, 36, 28]) # 4