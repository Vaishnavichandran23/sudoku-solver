 
def solve(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == '.':
                for a in '123456789':
                    if helper(board, i, j, a):
                        board[i][j] = a
                        if solve(board):
                            return True
                        board[i][j] = '.'
                return False
    return True


def helper(board, row, col, c):
    for i in range(9):
        if board[i][col] == c:
            return False
        if board[row][i] == c:
            return False
        if board[3*(row//3) + i//3][3*(col//3) + i%3] == c:
            return False
    return True


# Test board
board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

solve(board)

for row in board:
    print(row)