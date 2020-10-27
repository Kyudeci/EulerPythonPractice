# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
from time import time

start = time()

sum_of_squares = sum([i**2 for i in range(1,101)])
square_of_sum = sum(list(range(1,101)))**2

difference = square_of_sum - sum_of_squares
print(f"The difference is {difference}. Found in {time()-start} seconds")