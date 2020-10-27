# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
from time import time

start = time()

def palindrome_check(num):
    num_string = str(num)
    if num_string == num_string[::-1]:
        return True
    else:
        return False

def find_palindrome():
    for i in range(999,100,-1):
        for j in range(999,100,-1):
            prod = i*j
            if palindrome_check(prod):
                yield prod

l_p = max(list(find_palindrome()))
print(f'The largest palindrome is {l_p}. Found in {time()-start} seconds')