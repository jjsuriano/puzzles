import numpy as np

N = 4

starting_grid = np.zeros((N, N))

# Function to understand the idea of rows, columns
# and diagonals in a matrix
# NOTE: this function is not used in the solution
def queenAttackingDirections(grid, r, c):
    for i in range(N):
        # ROW ----------
        grid[r][i] = 1
        
        # COLUMN -------
        grid[i][c] = 1
        
        # DIAGONALS ----
        # Diagonals have the same row and column distance
        # j is the row distance
        j = abs(r-i)

        # apply the same distance to the column (ignore when out of bounds)
        # +j and -j for diagonals in both sides

        if c+j < N:
            grid[i][c+j] = 1
        
        if c-j >= 0:
            grid[i][c-j] = 1

    return grid
print(queenAttackingDirections(starting_grid, N//2, N//2))

# N QUEENS SOLUTION
