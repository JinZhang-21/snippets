def prime_factors(num):
    factors = []
    factor = 2
    while (num>=2):
        if (num % factor == 0):
            factors.append(factor)
            num = num / factor
        else:
            factor += 1
    return factors

prime_factors(12) # [2,2,3]
prime_factors(42) # [2,3,7]