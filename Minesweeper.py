import random
import re

class Board:
    def __init__(self,size,numBombs):
        self.size=size
        self.numBombs=numBombs

        #board
        self.board=self.MakeNewBoard()
        self.AssignValuesToBoard()

        #initialize set to keep track of uncovered locations (row,col)
        self.dug=set()

    def MakeNewBoard(self):
        #construct board based on size and numBombs
        #list of lists representation

        board=[[None for _ in range (self.size)] for _ in range(self.size)]
        bombsPlanted=0
        while bombsPlanted < self.numBombs:
            loc = random.randint(0,self.size**2-1)
            row = loc // self.size
            col = loc % self.size

            if board[row][col]== "*":
                #bomb already planted there --> keep going
                continue

            board[row][col]="*"
            bombsPlanted+=1
        return board

    def GetNumNeighbourBombs(self,row,col):
        #have to make sure to stay in bounds

        numNeighbourBombs=0
        for r in range(max(0 , row-1), min(self.size-1 , row+1)+1):
            for c in range(max(0,col-1),min(self.size-1 , col+1) +1):
                if r == row and c == col:
                    continue #original location, dont check
                if self.board[r][c]=="*":
                    numNeighbourBombs+=1
        return numNeighbourBombs

    def AssignValuesToBoard(self):
        #with all bombs planted, assign number 0-8 for all empty spaces,
        #representing the number of bombs nearby
        for r in range(self.size):
            for c in range(self.size):
                if self.board[r][c]=="*": #dont calculate if it s not already a bomb
                    continue
                self.board[r][c]=self.GetNumNeighbourBombs(r,c)

    def Dig(self,row,col):
        #return true if succesful, false if bomb already dug
        self.dug.add((row,col)) #mark dug spot

        if self.board[row][col] == "*":
            return False
        elif self.board[row][col]>0:
            return True

        #self.board[row][col]==0
        for r in range(max(0 , row-1), min(self.size-1 , row+1)+1):
            for c in range(max(0,col-1),min(self.size-1 , col+1) +1):
                if(r,c) in self.dug:
                    continue
                self.Dig(r,c)
        return True

    def __str__(self):
        #function where if u call print on object, it will print out what this function returns
        #use to return string board to player
        visibleBoard=[[None for _ in range(self.size)] for _ in range(self.size)]
        for row in range(self.size):
            for col in range(self.size):
                if (row,col) in self.dug:
                    visibleBoard[row][col]=str(self.board[row][col])
                else:
                    visibleBoard[row][col]=" "
        #put entire board in a string
        return str(visibleBoard)

def Play(size = 10,numBombs = 10):
    # 1. create board and plant bombs
    board=Board(size,numBombs)
    # 2. show the user the board and ask where to dig
    # 3.1 if location == bomb, game over
    # 3.2 if location != bomb, dig recursively until each square is at least next to a bomb
    #4. repeat steps 2 & 3 until there are no more places to dig => victory

    safe=True
    while len(board.dug) < (board.size**2-numBombs):
        print(board)
        #0,0 ; 0,   0, ; 0,    0
        userInput=re.split(",(\\s)*", input("Where would you like to dig? (input as row, col): "))
        row,col=int(userInput[0]), int(userInput[-1])

        if row<0 or row>=board.size or col<0 or col>=board.size:
            print("Invalid location. Try again.")
            continue

        safe=board.Dig(row,col)
        if not safe:
            #game over
            break
    if safe:
        print("You win!")
    else:
        print("Game over. You lost!")
        board.dug=[(r,c) for r in range(board.size) for c in range(board.size)]
        print(board)

if __name__ == "__main__":
    Play()
