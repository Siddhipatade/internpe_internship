import random

print("Welcome to Connect Four")
print("-----------------------")

possibleLetters = ["A", "B", "C", "D", "E", "F", "G"]
gameBoard = [["", "", "", "", "", "", ""],
             ["", "", "", "", "", "", ""],
             ["", "", "", "", "", "", ""],
             ["", "", "", "", "", "", ""],
             ["", "", "", "", "", "", ""],
             ["", "", "", "", "", "", ""]]
rows = 6
cols = 7

def printGameBoard():
    print("\n     A    B    C    D    E    F    G  ", end = "")
    for x in range(rows):
        print("\n   +----+----+----+----+----+----+----+")
        print(x, " |", end = "")
        for y in range(cols):
            if(gameBoard[x][y] == "🔵"):
                print("", gameBoard[x][y], end=  " |")
            elif(gameBoard[x][y] == "🔴"):
                print("", gameBoard[x][y], end=  " |")
            else:
                print(" ", gameBoard[x][y], end=  "  |")
    print("\n   +----+----+----+----+----+----+----+")
    
printGameBoard()

def modifyTurn(spacePicked, turn):
    gameBoard[spacePicked[0]][spacePicked[1]] = turn

def checkForWinner():
    # Check rows for four in a row
    for row in gameBoard:
        for i in range(cols - 3):
            if row[i] == row[i + 1] == row[i + 2] == row[i + 3] != "":
                return True

    # Check columns for four in a row
    for i in range(cols):
        for j in range(rows - 3):
            if gameBoard[j][i] == gameBoard[j + 1][i] == gameBoard[j + 2][i] == gameBoard[j + 3][i] != "":
                return True

    # Check diagonals (top-left to bottom-right)
    for i in range(rows - 3):
        for j in range(cols - 3):
            if gameBoard[i][j] == gameBoard[i + 1][j + 1] == gameBoard[i + 2][j + 2] == gameBoard[i + 3][j + 3] != "":
                return True

    # Check diagonals (bottom-left to top-right)
    for i in range(rows - 1, rows - 4, -1):
        for j in range(cols - 3):
            if gameBoard[i][j] == gameBoard[i - 1][j + 1] == gameBoard[i - 2][j + 2] == gameBoard[i - 3][j + 3] != "":
                return True

    return False

printGameBoard()

turnCount = 0
while True:
    if turnCount % 2 == 0:
        player = "🔴"
    else:
        player = "🔵"

    col = input(f"\nPlayer {player}, choose a column (A-G): ").upper()
    if col not in possibleLetters:
        print("Invalid input! Choose a column from A to G.")
        continue

    colIndex = possibleLetters.index(col)
    if all(gameBoard[i][colIndex] != "" for i in range(rows)):
        print("Column is full! Choose another column.")
        continue

    for i in range(rows - 1, -1, -1):
        if gameBoard[i][colIndex] == "":
            modifyTurn((i, colIndex), player)
            break

    printGameBoard()
    # Check for a winner after each move
    if checkForWinner():
        print(f"\nPlayer {player} wins!")
        break

    turnCount += 1
    if turnCount == rows * cols:
        print("\nThe game is a tie!")
        break
