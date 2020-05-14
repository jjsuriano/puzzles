# NAME: 
# Sudoku Solver

# DESCRIPTION: 
# Find the solution for the given sudoku grid

# INPUT: 
# 9x9 grid with numbers between 0-9 imitating a sudoku grid

# OUTPUT: 
# 9x9 grid with the solution

import numpy as np

grid = np.array(
    [[1, 0, 0, 5, 0, 0, 0, 4, 3], 
     [4, 7, 0, 1, 0, 2, 0, 5, 0], 
     [0, 0, 0, 0, 0, 0, 2, 9, 1], 
     [9, 0, 3, 4, 0, 0, 5, 8, 6],
     [6, 0, 0, 0, 0, 5, 0, 2, 0],
     [0, 5, 0, 0, 0, 0, 1, 7, 0], 
     [3, 0, 5, 8, 0, 0, 9, 6, 2], 
     [0, 2, 6, 3, 0, 9, 8, 0, 5],
     [8, 0, 0, 0, 5, 0, 0, 0, 0]
     ] 
)

# helper function if number placement is valid
def isValid(value, r, c, grid):
    # check the row and the column the value is in
    for i in range(9):
        if value == grid[r][i] or value == grid[i][c]:
            return False
    
    # check in the 3x3 grid the value is in
    r = (r//3)*3 # calculate the row index of the top left corner of that 3x3 grid
    c = (c//3)*3 # calculate the column index of the top left corner of that 3x3 grid

    # 0,0    0,3    0,6
    # 3,0    3,3    3,6
    # 6,0    6,3    6,6

    for i in range(3):
        for j in range(3):
            if value == grid[r+i][c+j]:
                return False
        
    return True