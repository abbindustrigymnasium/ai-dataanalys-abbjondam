import random
import numpy as np 

n = 100
board = [[0]*n for _ in range(n)]

def generateBoard():
    for i in range(n):
        board[i] = i
    random.shuffle(board)
    # print(board)

# def n_Conflict(col,row):
#     conflicts = 0
#     n_row = board.count(row)
#     if n_row == 1 or (board[col] == row and n_row == 2): 
#         conflicts += 1
#     if pDiagonal.count(row-col) > 1:
#         conflicts += 1
#     if nDiagonal.count(row+col) > 1:
#         conflicts += 1
#     return conflicts
def n_Conflict(col,row):
    conflicts = [0] * 6
    for i in range(n):
        rowVal = board[i]
        if i < col:
            if row == rowVal:
                conflicts[0] = 1
            elif (row - rowVal) / (col - i) == 1:
                conflicts[1] = 1
            elif (row - rowVal) / (col - i) == -1:
                conflicts[2] = 1
        elif i > col:
            if row == rowVal:
                conflicts[3] = 1
            elif (row - rowVal) / (col - i) == 1:
                conflicts[4] = 1
            elif (row - rowVal) / (col - i) == -1:
                conflicts[5] = 1
    return sum(conflicts)

# def Nconflicts():
#     conflicts = []
#     for col,row in enumerate(board):
        
#         conflicts.append(isConflict(col,row))
#     return conflicts


def movePiece():
    minConflict = []
    col = random.randint(0,n-1)
    # print(f'col: {col}')
    # print(f'board: {board}')
 
    # print(f'pDiagonal: {pDiagonal}')
    # print(f'nDiagonal: {nDiagonal}')
    for i in range(n):
        minConflict.append(n_Conflict(col,i))
    # print(f'minConflict: {minConflict}')
    m = min(minConflict)
    
    minIndex = [i for i, j in enumerate(minConflict) if j == m]
    # print(f'Index: {minIndex}')
    position = random.choice(minIndex)
    # print(f'position: {position}')
    board[col] = position

# board = [1,6,4,4,5,2,4,0]
# minConflict = []
# for i in range(n):
#     minConflict.append(n_Conflict(3,i))

# print(minConflict)

def isSolution():
    totalConflicts = 0
    for i in board:
        totalConflicts += n_Conflict(i,board[i])
    if totalConflicts == 0:
        return True
    return False


generateBoard()
maxIterations = 10000 
solved = False 
counter = 0 
while solved != True and maxIterations > counter:
    counter += 1 

    movePiece()
    solved = isSolution()
print(counter)



   



# if totalConflicts == 0:
#     print('Solved')
print(board)



