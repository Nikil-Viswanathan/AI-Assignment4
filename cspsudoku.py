#Sudoku Solver using CSP 

N = 9

def print_board(board):
    print("-" * 25)
    for i in range(9):
        for j in range(9):
            if j % 3 == 0:
                print("| ", end="")

            if board[i][j] == 0:
                print(". ", end="") 
            else:
                print(board[i][j], end=" ")

        print("|")

        if (i + 1) % 3 == 0:
            print("-" * 25)

def find_empty(board):
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                return (i, j)
    return None

def is_valid(board, row, col, num):
    
    for j in range(N):
        if board[row][j] == num:
            return False

    for i in range(N):
        if board[i][col] == num:
            return False

    start_row = (row // 3) * 3
    start_col = (col // 3) * 3

    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def solve_sudoku(board):
    
    empty = find_empty(board)
    
    if not empty:
        return True  
    
    row, col = empty

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = 0  

    return False

board = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

print("Original Sudoku:\n")
print_board(board)

if solve_sudoku(board):
    print("\nSolved Sudoku:\n")
    print_board(board)
else:
    print("No solution exists")