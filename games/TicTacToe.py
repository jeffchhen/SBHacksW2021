class Board:
    board = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]
    neededToWin = len(board[0]) - 1

    def printBoard(self):
        print("  0 1 2")
        for rowNum in range(len(self.board)):
            print(str(rowNum) + " ", end='')
            for colNum in range(len(self.board[rowNum])):
                print(self.board[rowNum][colNum] + ' ', end='')
            print("")

    def returnPiece(self, row, col):
        return self.board[row][col]

    def placePiece(self, piece, row, col):
        self.board[row][col] = piece

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
                    if currentWins == self.neededToWin:
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
                    if currentWins == self.neededToWin:
                        return True
                else:
                    pos += 1
                    currentWins = 0
        return False

    def checkRightDiagWin(self):
        if self.board[2][0] != "*" and (self.board[2][0] == self.board[1][1] == self.board[0][2]):
            return True
        else:
            return False

    def checkLeftDiagWin(self):
        if self.board[2][2] != "*" and (self.board[2][2] == self.board[1][1] == self.board[0][0]):
            return True
        else:
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
                    try:
                        board.printBoard()
                        choosePiece = player2.name + ", choose a row to place your piece: "
                        row = int(input(choosePiece))
                        if 3 > row >= 0:
                            break
                        else:
                            print("Oops, that's outside of the board. Please try again. ")
                    except ValueError:
                        print("Oops, that's not valid. Please try again. ")
                while True:
                    try:
                        choosePiece = player2.name + ", choose a column to place your piece: "
                        col = int(input(choosePiece))
                        if 3 > col >= 0:
                            if board.returnPiece(row, col) == "*":
                                board.placePiece(player2.piece, row, col)
                                playerTurn += 1
                                break
                            print("Hmm, that doesn't look like an empty space. Try again. ")
                            break
                        else:
                            print("Oops, that's outside of the board. Please try again. ")
                            break
                    except ValueError:
                        print("Oops, that's not valid. Please try again. ")
            if playerTurn == 0:
                while True:
                    try:
                        board.printBoard()
                        choosePiece = player1.name + ", choose a row to place your piece: "
                        row = int(input(choosePiece))
                        if 3 > row >= 0:
                            break
                        else:
                            print("Oops, that's outside of the board. Please try again. ")
                    except ValueError:
                        print("Oops, that's not valid. Please try again. ")
                while True:
                    try:
                        choosePiece = player1.name + ", choose a column to place your piece: "
                        col = int(input(choosePiece))
                        if 3 > col >= 0:
                            if board.returnPiece(row, col) == "*":
                                board.placePiece(player1.piece, row, col)
                                playerTurn += 1
                                break
                            print("Hmm, that doesn't look like an empty space. Try again. ")
                            break
                        else:
                            print("Oops, that's outside of the board. Please try again. ")
                            break
                    except ValueError:
                        print("Oops, that's not valid. Please try again. ")
                        break
            if board.checkForWins():
                if playerTurn == 1:
                    name = player1.name
                else:
                    name = player2.name
                print("Congrats! " + name + " is the better human being! ")
                break
            playerTurn = playerTurn % 2


game = Game()
