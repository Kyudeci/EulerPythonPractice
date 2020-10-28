# Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?
from time import time

start = time()

with open("1000_digit_number.txt") as f:
    number_file = f.read()

number = "".join(number_file.splitlines())
greatest_product = 0

def _product(lst):
    prod = 1
    for item in lst:
        prod*=item
    return prod


for i in range(len(number)-13):
    selection = number[i:i+13]

    if '0' in selection:
        continue

    numbers = [int(i) for i in selection]
    product = _product(numbers)

    if product > greatest_product:
        greatest_product = product
print(f"The greatest product is {greatest_product}. Found in {time() - start}")
