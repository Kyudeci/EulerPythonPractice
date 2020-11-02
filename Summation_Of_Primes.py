# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
import math
from time import time

start = time()
num = 8
prime_numbers = [2, 3, 5, 7]


def is_prime(number: int):
    count = 0
    for i in range(1, math.ceil(math.sqrt(number)) + 1):
        if number % i == 0:
            count += 1
        if count > 1:
            return False
    return True


while num != 2e6:
    if is_prime(num):
        prime_numbers.append(num)
    num += 1

prime_sum = sum(prime_numbers)

print(f"The sum of prime numbers under 2 million is {prime_sum}. Found in {time() - start} seconds")