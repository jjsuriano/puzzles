import numpy as np

X = 4

starting_grid = np.zeros((X, X))

# Function to understand the idea of rows, columns
# and diagonals in a matrix
# NOTE: this function is not used in the solution
def queenAttackingDirections(grid, r, c):
    for i in range(X):
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

        if c+j < X:
            grid[i][c+j] = 1
        
        if c-j >= 0:
            grid[i][c-j] = 1

    return grid
#print(queenAttackingDirections(starting_grid, X//2, X//2))

# N QUEENS SOLUTION
def isValid(N, grid, r, c):
    for i in range(N):
        if grid[i][c] == 1 or grid[r][i] == 1:
            return False
        
        diff = abs(r-i)

        left_diagonal = c - diff
        right_diagonal = c + diff

        if left_diagonal in range(N):
            if grid[i][left_diagonal] == 1:
                return False
        if right_diagonal in range(N):
            if grid[i][right_diagonal] == 1:
                return False
    return True

def placeQueen(N, grid, r, s):
    # Missing collecting the different solutions
    if r == N: return False
    for i in range(N):
        print('test: {}, {}'.format(r, i))
        if isValid(N, grid, r, i):
            grid[r][i] = 1
            print('push: {}, {}\n'.format(r, i))
            #print(grid)
            #print()
            placeQueen(N, grid, r+1, s)
            print('pop: {}, {}\n'.format(r, i))
            if r == N-1:
                print('HERE!')
                s += 1
                print(grid)
            grid[r][i] = 0

def solve(N):
    grid = np.zeros((N,N))
    solutions = 0
    if placeQueen(N, grid, 0, solutions):
        print('I found a solution!')
    else: 
        print('I did not find a solution!')
    return solutions

print(solve(4))