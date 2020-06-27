# DESCRIPTION: 
# Find the solution for the given sudoku grid

# INPUT: 
# 9x9 grid with numbers between 0-9 imitating a sudoku grid

# OUTPUT: 
# 9x9 grid with the solution

grid = [[1, 0, 0, 5, 0, 0, 0, 4, 3], 
        [4, 7, 0, 1, 0, 2, 0, 5, 0], 
        [0, 0, 0, 0, 0, 0, 2, 9, 1], 
        [9, 0, 3, 4, 0, 0, 5, 8, 6],
        [6, 0, 0, 0, 0, 5, 0, 2, 0],
        [0, 5, 0, 0, 0, 0, 1, 7, 0], 
        [3, 0, 5, 8, 0, 0, 9, 6, 2], 
        [0, 2, 6, 3, 0, 9, 8, 0, 5],
        [8, 0, 0, 0, 5, 0, 0, 0, 0]] 

class Sudoku:
    def __init__(self, board):
        self.board = board
        self.SIZE = 9
    
    def _isValid(self, value:int, row:int, col:int) -> bool:
        for i in range(self.SIZE):
            if value == self.board[row][i] or value == self.board[i][col]:
                return False
        
        row = (row // 3) * 3
        col = (col // 3) * 3 

        for i in range(3):
            for j in range(3):
                if value == self.board[row + j][col + i]:
                    return False
        return True
    
    def newBoard(self, board):
        self.board = board

    def solve(self):
        nextEmpty = self._getNextEmpty()
        if not nextEmpty:
            return True
        row, col = nextEmpty

        for num in range(1, self.SIZE+1):
            if self._isValid(num, row, col):
                self.board[row][col] = num
                if self.solve():
                    return True
                self.board[row][col] = 0
        return False
             
    def _getNextEmpty(self):
        for row in range(self.SIZE):
            for col in range(self.SIZE):
                if self.board[row][col] == 0:
                    return (row, col)
        return None

    def display(self):
        print()
        for row in range(self.SIZE):
            if row % 3 == 0 and row != 0:
                    print("- - - + - - - + - - -")
            for col in range(self.SIZE):
                if col % 3 == 0 and col != 0:
                    print("| ", end="")
            
                if col == self.SIZE-1:
                    print(self.board[row][col])
                else: 
                    print(self.board[row][col], end=" ")
        print()

s = Sudoku(grid)
s.display()
s.solve()
s.display()