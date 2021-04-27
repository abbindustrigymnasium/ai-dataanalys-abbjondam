import copy

class NQueen:

    def __init__(self, n):
        self.n = n
        self.board = [[0]*n for _ in range(n)]
        self.solved = []
        self.uniqueSolved = 0
        self.mirrored = []
        self.uniqueSolutions = []
    
    def printBoard(self, board=None):
        if board == None:
            board = self.board
        print("---"*self.n)
        for i in board:
            print(i)
    
    def printAll(self):
        for solutions in self.uniqueSolutions:
            print("---"*self.n)
            for i in solutions:
                print(i)
        print("---"*self.n)
        print(f'Number of Queens: {self.n}')
        print(f'Number of solutions: {len(self.solved)}')
        print(f'Number of unique solutions: {self.uniqueSolved}')

    def mirror(self,direction,board=None):
        if board == None:
            board = self.board
        mirroredBoard =  [[0]*self.n for _ in range(self.n)]
        for row in range(self.n):
            prevCol = board[row].index(1)
            if direction == "h":
                newRow = row
                newCol = self.n  - 1 - prevCol
            elif direction == "v":
                newCol = prevCol
                newRow = self.n - 1 - row
            mirroredBoard[newRow][newCol] = 1
        return mirroredBoard
    
    def rotate(self,angle=90,board=None):
        if board == None:
            board = self.board
        rotatedBoard =  [[0]*self.n for _ in range(self.n)]
        for row in range(self.n):
            prevCol = board[row].index(1)
            if angle == 90:
                newRow = prevCol
                newCol = self.n  - 1 - row
            elif angle == 180:
                newRow = self.n - 1 -  row
                newCol = self.n  - 1 - prevCol
            elif angle == 270:
                newRow = self.n - 1 - prevCol
                newCol = row
            rotatedBoard[newRow][newCol] = 1
        return rotatedBoard
    
    def addRotMir(self):
        lastSolution = copy.deepcopy(self.board)
        solRotMir = []
        mirrorH = self.mirror("h",lastSolution)
        mirrorV = self.mirror("v",lastSolution)
        solRotMir.append(mirrorH)
        solRotMir.append(mirrorV)
        solRotMir.append(self.rotate(90,mirrorH))
        solRotMir.append(self.rotate(90,mirrorV))
        solRotMir.append(self.rotate(90,lastSolution))
        solRotMir.append(self.rotate(180,lastSolution))
        solRotMir.append(self.rotate(270,lastSolution))
        if self.board not in self.solved:
                self.uniqueSolved += 1
                self.uniqueSolutions.append(copy.deepcopy(self.board))
                self.solved.append(copy.deepcopy(self.board))
        for i in solRotMir:
            if i not in self.solved:
                self.solved.append(i)
            
    def isLegal(self,col,row):
        for i in range(1,row+1):
            if abs((col - self.board[row-i].index(1))  / (row - (row-i))) == 1:
                return False
        return True

    def solverAll(self,row=0,banned=[]):
        if row >= self.n:

            self.addRotMir()


            if len(self.solved) == 1:
                self.mirrored = self.mirror("h",copy.deepcopy(self.board))
                return False
            elif self.board == self.mirrored:
                return True
                
            else:
                return False
                
        for col in range(self.n):
            if col not in banned:
                if self.isLegal(col,row):
                    self.board[row][col] = 1
                    banned.append(col)
                    if self.solverAll(row+1,banned):
                        return True
                    self.board[row][col] = 0
                    banned.remove(col)
        
        return False
    
    def solver(self,row=0,banned=[]):
        if row >= self.n:
            return True
        for col in range(self.n):
            if col not in banned:
                if self.isLegal(col,row):
                    self.board[row][col] = 1
                    banned.append(col)
                    if self.solver(row+1,banned):
                        return True
                    self.board[row][col] = 0
                    banned.remove(col)
        return False


solution = NQueen(10)
solution.solverAll()
solution.printAll()
# solution.solver()
# solution.printBoard()
