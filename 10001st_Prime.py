# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?
import math
from time import time

start = time()
num = 14
prime_numbers = [2, 3, 5, 7, 11, 13]


def is_prime(number: int):
    count = 0
    for i in range(1, math.ceil(math.sqrt(number)) + 1):
        if number % i == 0:
            count += 1
        if count > 1:
            return False
    return True


while len(prime_numbers) != 10001:
    if is_prime(num):
        prime_numbers.append(num)
    num += 1

print(f"The 10,001st prime number is {prime_numbers[-1]}. Found in {time() - start} seconds")
