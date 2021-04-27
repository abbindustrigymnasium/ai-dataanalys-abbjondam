n = 8
board = [[0]*n for i in range(n)]
blocked = []

def checkValid(col,row):
    if row != 0:
        for rows in board:
            prevRow = board.index(rows)
            if 1 in rows and prevRow != row:
                prevCol = board[prevRow].index(1)
                if abs((col - prevCol)/(row - prevRow)) == 1:
                    return False
    return True



def solver(row=0):
    if row < n:
        for col in range(n):
            if col not in blocked:
                if 1 in board[row]:
                    blocked.remove(board[row].index(1))
                    board[row] = [0]*n 
                board[row][col] = 1
                if checkValid(col,row):
                    blocked.append(col)
                    solver(row+1)
                else:
                    board[row][col] = 0
        if 1 not in board[row] and board[row-1].index(1) == n-1:
            blocked.remove(board[row-1].index(1))
            board[row-1] = [0]*n
    return board

solver()


for row in board:
    print(row)


    