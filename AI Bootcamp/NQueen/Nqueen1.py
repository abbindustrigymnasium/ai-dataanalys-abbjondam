
N = 2
board = [[0]*N for _ in range(N)]
 
def isLegal(board,col,row):
    for i in range(1,row+1):
        if abs((col - board[row-i].index(1))  / (row - (row-i))) == 1:
            return False
    return True
 
def solver(board,row=0,banned=[]):
    if row >= N:
        return True
    for col in range(N):
        if col not in banned:
            if isLegal(board,col,row):
                board[row][col] = 1
                banned.append(col)
                if solver(board,row+1,banned):
                    return True
                board[row][col] = 0
                banned.remove(col)
    return False




a = solver(board)
print(a)






