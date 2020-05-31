# NAME: 
# Rooks are Safe

# DESCRIPTION: 
# Given a n by n grid with 1s representing rooks positions, determine if they are
# safe or not where they are located. 

# EXAMPLE:
# board = [[1,0,0,0], -> False
#         [0,0,1,0],  
#         [0,0,1,0],
#         [0,0,0,1]]

# INPUT: 
# A nxn matrix where n >= 1 with 1s and 0s. 
# 1s indicate a rook is in that square of the grid
# 0s mean there are no rooks in that square of the grid

# OUTPUT: 
# True or False

board = [[1,0,0,0],
        [0,0,1,0],
        [0,0,1,0],
        [0,0,0,1]]

print()

# METHOD 1 - - - - -
print('METHOD 1')

# LOGIC: 
# Count the number of each rook at each column and each row, check if the count
# is more than 1 then return False

result = True

for i in range(len(board)):
    sumRow = 0
    sumCol = 0
    for j in range(len(board)):
        sumRow += board[i][j]
        sumCol += board[j][i]
    if sumRow > 1 or sumCol > 1:
        result = False

print(result)
print()