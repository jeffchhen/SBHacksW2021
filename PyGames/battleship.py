class Board:
    def __init__(self):
        self.board = [["-", "-", "-", "-", "-", "-", "-", "-"],
                      ["-", "-", "-", "-", "-", "-", "-", "-"],
                      ["-", "-", "-", "-", "-", "-", "-", "-"],
                      ["-", "-", "-", "-", "-", "-", "-", "-"],
                      ["-", "-", "-", "-", "-", "-", "-", "-"],
                      ["-", "-", "-", "-", "-", "-", "-", "-"],
                      ["-", "-", "-", "-", "-", "-", "-", "-"],
                      ["-", "-", "-", "-", "-", "-", "-", "-"]]


class Game:
    player1 = Board()
    player2 = Board()
    player1play = Board()
    player2play = Board()


def setup(board, direction, row, column, size):
    if direction == 0:
        for i in range(column - 1, column - 1 + size):
            board[row - 1][i] = '*'
    elif direction == 1:
        for i in range(row - 1, row - 1 + size):
            board[i][column - 1] = '*'
    return board


def move(board, playBoard, row, column):
    if board[row - 1][column - 1] == '*':
        board[row - 1][column - 1] = 'h'
        playBoard[row - 1][column - 1] = 'x'
        print("Hit!")
    elif board[row - 1][column - 1] == '-':
        playBoard[row - 1][column - 1] = 'm'
        print("Miss!")
    else:
        print("You already played that move...")
    return playBoard


def checkWin(board):
    for i in range(8):
        for j in range(8):
            if board[i][j] == '*':
                return False
    return True


def getInput(prompt, lbound, ubound):
    while True:
        try:
            putVar = int(input(prompt))
            if putVar not in range(lbound, ubound + 1):
                print("Sorry, please try again")
            else:
                break
        except ValueError or IndexError:
            print("Sorry, please try again")
    return putVar


def play(board1, board2, board1play, board2play):
    carrierDir1 = getInput(
        "Player 1: Which direction should the 5-space carrier face? Enter 0 for right or 1 for down.\n", 0, 1)
    carrierSR1 = getInput("Player 1: In which row should the carrier start? Enter 1-8.\n", 1, 8)
    carrierSC1 = getInput("Player 1: In which column should the carrier start? Enter 1-8.\n", 1, 8)
    subDir1 = getInput(
        "Player 1: Which direction should the 3-space submarine face? Enter 0 for right or 1 for down.\n", 0, 1)
    subSR1 = getInput("Player 1: In which row should the submarine start? Enter 1-8.\n", 1, 8)
    subSC1 = getInput("Player 1: In which column should the submarine start? Enter 1-8.\n", 1, 8)
    destDir1 = getInput(
        "Player 1: Which direction should the 2-space destroyer face? Enter 0 for right or 1 for down.\n", 0, 1)
    destSR1 = getInput("Player 1: In which row should the destroyer start? Enter 1-8.\n", 1, 8)
    destSC1 = getInput("Player 1: In which column should the destroyer start? Enter 1-8.\n", 1, 8)
    carrierDir2 = getInput(
        "Player 2: Which direction should the 5-space carrier face? Enter 0 for right or 1 for down.\n", 0, 1)
    carrierSR2 = getInput("Player 2: In which row should the carrier start? Enter 1-8.\n", 1, 8)
    carrierSC2 = getInput("Player 2: In which column should the carrier start? Enter 1-8.\n", 1, 8)
    subDir2 = getInput(
        "Player 2: Which direction should the 3-space submarine face? Enter 0 for right or 1 for down.\n", 0, 1)
    subSR2 = getInput("Player 2: In which row should the submarine start? Enter 1-8.\n", 1, 8)
    subSC2 = getInput("Player 2: In which column should the submarine start? Enter 1-8.\n", 1, 8)
    destDir2 = getInput(
        "Player 2: Which direction should the 2-space destroyer face? Enter 0 for right or 1 for down.\n", 0, 1)
    destSR2 = getInput("Player 2: In which row should the destroyer start? Enter 1-8.\n", 1, 8)
    destSC2 = getInput("Player 2: In which column should the destroyer start? Enter 1-8.\n", 1, 8)
    board1 = setup(board1, carrierDir1, carrierSR1, carrierSC1, 5)
    board1 = setup(board1, subDir1, subSR1, subSC1, 3)
    board1 = setup(board1, destDir1, destSR1, destSC1, 2)
    board2 = setup(board2, carrierDir2, carrierSR2, carrierSC2, 5)
    board2 = setup(board2, subDir2, subSR2, subSC2, 3)
    board2 = setup(board2, destDir2, destSR2, destSC2, 2)
    while not checkWin(board1) and not checkWin(board2):
        print('  1 2 3 4 5 6 7 8')
        for i in range(8):
            line = str(i + 1)
            for j in range(8):
                line = line + ' ' + board1play[i][j]
            print(line)
        if checkWin(board1):
            print("Player 2 Wins!")
            break
        a = getInput("Player 1: select a row to attack\n", 1, 8)
        b = getInput("Player 1: select a column to attack\n", 1, 8)
        board2play = move(board2, board2play, a, b)
        print('  1 2 3 4 5 6 7 8')
        for i in range(8):
            line = str(i + 1)
            for j in range(8):
                line = line + ' ' + board2play[i][j]
            print(line)
        a = getInput("Player 2: select a row to attack\n", 1, 8)
        b = getInput("Player 2: select a column to attack\n", 1, 8)
        board1play = move(board1, board1play, a, b)
        if checkWin(board2):
            print("Player 1 Wins!")


game = Game()
play(game.player1.board, game.player2.board, game.player1play.board, game.player2play.board)
