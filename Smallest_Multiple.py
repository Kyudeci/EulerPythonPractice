# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
from time import time

start = time()
divisors = range(10,21)
NUM = 2520
found = False

while not found:
    for i in divisors:
        if NUM % i != 0:
            NUM+=10
            break
        elif i == 20:
            found = True

print(f'The smallest multiple is {NUM}. Found in {time()-start} seconds')
