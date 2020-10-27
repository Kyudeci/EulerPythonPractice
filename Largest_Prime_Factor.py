# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
import math
from time import time

start = time()
NUM = 600851475143
# NUM = 13195

def half_factors(num:int):
    for i in range(1, math.ceil(math.sqrt(num))):
        if num % i == 0:
            yield i

def all_factors(factors):
    factorized = []
    for factor in factors:
        quotient = NUM // factor
        factorized.append(quotient)
    return factorized+factors[::-1]

def find_prime(list_of_factors:list):
    for factor in list_of_factors:
        h_factors = list(half_factors(factor))
        if factor == 1:
            continue
        if len(h_factors) > 2:
            print(f"{factor} has {h_factors} as factors")
        elif len(all_factors(h_factors)) > 2:
            print(f"{factor} has {h_factors} as factors")
        else:
            yield factor

factors = list(half_factors(NUM))
factors = all_factors(factors)
largest_prime = max(list(find_prime(factors)))
print(f"The largest prime factor of {NUM} is {largest_prime}. Found in {time() - start} seconds")