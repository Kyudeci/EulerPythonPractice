# What is the value of the first triangle number to have over five hundred divisors?

import math
from time import time

start = time()


def find_divisors(number: int):
    count = 0
    for i in range(1, math.ceil(math.sqrt(number)) + 1):
        if number % i == 0:
            count += 1
    return count*2

found = False
num = 1

while not found:
    tri_num = sum(list(range(1,num)))
    num_of_divisors = find_divisors(tri_num)
    if num_of_divisors > 500:
        found = True
    num+=1

print(f"The triangle number is {tri_num}. Found in {time() - start} seconds")