# What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?

from time import time
import numpy as np
start = time()

with open("20x20_grid.txt") as f:
    grid_file = f.read()

grid = grid_file.splitlines()
grid = [[int(num) for num in row.split()] for row in grid]
grid = np.asarray(grid)

collect_rows = []
for row in grid:
    for i in range(len(row)-4):
        if 0 not in row[i:i + 4]:
            collect_rows.append(row[i:i + 4])

collect_col = []
for col in grid.T:
    for i in range(len(col)-4):
        if 0 not in col[i:i + 4]:
            collect_col.append(col[i:i + 4])

collect_diag = []
for i in range(-19, 20):
    diag_list = np.diagonal(grid, offset=i)
    inv_diag = np.fliplr(grid).diagonal(offset=i)
    if len(diag_list) < 4:
        continue
    for diag in range(len(diag_list)-3):
        if 0 not in diag_list[diag:diag + 4]:
            collect_diag.append(diag_list[diag:diag + 4])
        if 0 not in inv_diag[diag:diag + 4]:
            collect_diag.append(inv_diag[diag:diag + 4])

max_row = max([np.product(x) for x in collect_rows])
max_col = max([np.product(x) for x in collect_col])
max_diag = max([np.product(x) for x in collect_diag])
abs_max = max([max_col,max_row,max_diag])

print(f"The greatest product is {abs_max}. Found in {time() - start}")