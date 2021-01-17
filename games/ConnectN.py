class Board:
    def __init__(self):
        while True:
            self.size = int(input("How big should the board be? (X by X): "))
            if self.size <= 2:
                print("Board is too small you're smarter than that :(")
            else:
                break
        while True:
            self.neededToWin = int(input("How many pieces in a row to win?: "))
            if self.neededToWin >= self.size:
                print("You need to be able to win...")
            else:
                break
        self.board = []
        for row in range(self.size):
            self.board.append([])
            for col in range(self.size):
                self.board[row].append("*")

    def printBoard(self):
        for num in range(self.size):
            print(str(num) + ' ', end='')
        print("")
        for rowNum in range(len(self.board)):
            for colNum in range(len(self.board[rowNum])):
                print(self.board[rowNum][colNum] + ' ', end='')
            print("")

    def returnPiece(self, row, col):
        return self.board[row][col]

    def findFirstEmptySpot(self, col):
        rowNum = self.size
        for x in range(1, rowNum + 1):
            if self.board[rowNum - x][col] == "*":
                return rowNum - x
        return -1

    def placePiece(self, piece, col):
        emptySpot = self.findFirstEmptySpot(col)
        if emptySpot == -1:
            print("full")
            return False
        self.board[emptySpot][col] = piece
        return True

    def checkRowWin(self):  # check right after player puts the piece, so it is current player's victory
        for rowNum in range(len(self.board)):
            pos = 0
            currentWins = 0
            while pos < len(self.board[0]) - 1:
                if self.board[rowNum][pos] == "*":
                    pos += 1
                    continue
                elif self.board[rowNum][pos] == self.board[rowNum][pos + 1]:
                    currentWins += 1
                    pos += 1
                    if currentWins == self.neededToWin - 1:
                        return True
                else:  # need in a row wins
                    pos += 1
                    currentWins = 0
        return False

    def checkColWin(self):
        for colNum in range(len(self.board)):
            pos = 0
            currentWins = 0
            while pos < len(self.board[0]) - 1:
                if self.board[pos][colNum] == "*":
                    pos += 1
                    continue
                elif self.board[pos][colNum] == self.board[pos + 1][colNum]:
                    currentWins += 1
                    pos += 1
                    if currentWins == self.neededToWin - 1:
                        return True
                else:
                    pos += 1
                    currentWins = 0
        return False

    def check1RightDiagWin(self, row, col):  # row, col are the starting points
        tempRow = row  # **X
        tempCol = col  # *X*
        currentWins = 0# X**
        while (self.size - 1 >= tempRow > 0) and (self.size - 1 > tempCol >= 0):
            if (self.board[tempRow][tempCol] != "*") and (
                    self.board[tempRow][tempCol] == self.board[tempRow - 1][tempCol + 1]):
                currentWins += 1
                if currentWins == self.neededToWin - 1:
                    return True
                tempRow -= 1
                tempCol += 1
                continue
            else:
                currentWins = 0
                tempRow -= 1
                tempCol += 1
        return False

    def checkRightDiagWin(self):
        for numRow in range(self.size):
            if self.check1RightDiagWin(self.size - 1 - numRow, 0):
                return True
        for numCol in range(self.size):
            if self.check1RightDiagWin(self.size - 1, numCol):
                return True
        return False

    def check1LeftDiagWin(self, row, col):
        tempRow = row  # X**
        tempCol = col  # *X*
        currentWins = 0# **X
        while (self.size - 1 > tempRow >= 0) and (self.size - 1 > tempCol >= 0):
            if (self.board[tempRow][tempCol] != "*") and (
                    self.board[tempRow][tempCol] == self.board[tempRow + 1][tempCol + 1]):
                currentWins += 1
                if currentWins == self.neededToWin - 1:
                    return True
                tempRow += 1
                tempCol += 1
                continue
            else:
                currentWins = 0
                tempRow += 1
                tempCol += 1

    def checkLeftDiagWin(self):
        for numRow in range(self.size):
            if self.check1LeftDiagWin(numRow, 0):
                return True
        for numCol in range(self.size):
            if self.check1LeftDiagWin(0, numCol):
                return True
        return False

    def checkForWins(self):
        return self.checkRowWin() or self.checkColWin() or self.checkRightDiagWin() or self.checkLeftDiagWin()


class Player:
    def __init__(self):
        self.name = input("What is your name?: ")
        while True:
            playerPieceInfo = "Okay " + self.name + ',' + " what piece do you want?: "
            self.piece = input(playerPieceInfo)
            if self.piece != "*" and len(self.piece) == 1:
                break
            else:
                print("Sorry, it can't be '*' and it needs to be 1 character :( ")


class Game:
    def __init__(self):
        print("Let the game begin!")
        player1 = Player()
        player2 = Player()
        while player1.piece == player2.piece:
            print("Can't have the same piece >:( ")
            player1 = Player()
            player2 = Player()
        playerTurn = 0
        board = Board()
        while True:
            if playerTurn == 1:
                while True:
                    board.printBoard()
                    try:
                        choosePiece = player2.name + ", choose a column to place your piece: "
                        col = int(input(choosePiece))
                        if (board.size - 1) >= col >= 0:
                            if board.placePiece(player2.piece, col):
                                playerTurn += 1
                                break
                            print("Hmm, seems like that column is full. Try again. ")
                        else:
                            print("Oops, that's outside of the board. Please try again. ")
                    except ValueError:
                        print("Oops, that's not valid. Please try again. ")
            if playerTurn == 0:
                while True:
                    board.printBoard()
                    try:
                        choosePiece = player1.name + ", choose a column to place your piece: "
                        col = int(input(choosePiece))
                        if (board.size - 1) >= col >= 0:
                            if board.placePiece(player1.piece, col):
                                playerTurn += 1
                                break
                            print("Hmm, seems like that column is full. Try again. ")
                        else:
                            print("Oops, that's outside of the board. Please try again. ")
                    except ValueError:
                        print("Oops, that's not valid. Please try again. ")
            if board.checkForWins():
                if playerTurn == 1:
                    name = player1.name
                else:
                    name = player2.name
                board.printBoard()
                print("Congrats! " + name + " is the better human being! ")
                break
            playerTurn = playerTurn % 2


game = Game()
