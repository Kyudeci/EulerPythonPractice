# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

from time import time

start = time()

with open("Fifty_Digit_Numbers.txt") as f:
    number_file = f.read()

numbers = number_file.splitlines()
numbers = [int(number) for number in numbers]
sum_of_numbers = str(sum(numbers))
first_ten = sum_of_numbers[0:10]

print(f"The first ten digits are {first_ten}. Found in {time() - start} seconds")