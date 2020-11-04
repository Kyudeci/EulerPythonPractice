# The following iterative sequence is defined for the set of positive integers:
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
# Which starting number, under one million, produces the longest chain?

from time import time

start = time()

def count_chain(start_num:int):
    chain = 1
    while start_num != 1:
        if start_num == 1:
            break
        if start_num == 10:
            chain+=7
            break
        if start_num%2 == 0:
            start_num/=2
        else:
            start_num = (3*start_num)+1
        chain+=1
    return chain

highest_chain = (13,10)
num = 13
while num < 1e6:
    current_chain = count_chain(num)
    if current_chain > highest_chain[1]:
        highest_chain = (num,current_chain)
    num+=1

print(f"The number with the longest chain is {highest_chain[0]} with a chain of {highest_chain[1]}. "
      f"Found in {time()-start} seconds.")