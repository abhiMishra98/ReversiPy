from reversiPy.ReversiBoard import ReversiBoard
from reversiPy.ReversiConsole import ReversiConsoleView

gameBoard = ReversiBoard()
printGameBoard = ReversiConsoleView(gameBoard)

print("Allocated board of dimension x = 8, y=8")

printGameBoard.print_board()

posX = 0
posY = 0
turn = 0
currentPlayer = ''
posXAscii = ''
indexState = 0
player1CanMove = gameBoard.canMove('B')
player2CanMove = gameBoard.canMove('W')

playerCount = []

while(True):
    currentPlayer = 'B' if (turn %2 == 0) else 'W'
    print("Player"+currentPlayer+": Please enter a position (x,y):")
    posX = input()
    posY = input()
    posXAscii = ord(posX)
    posYAscii = ord(posY)

    if(posXAscii <= 47 or posXAscii >= 56 or posYAscii <= 47 or posYAscii >= 56):
        print("Invalid position. Please enter values between 0 and 7.\n")
        continue
    occupied = gameBoard.get_index_state(int(posX),int(posY))
    if(occupied.value != '*'):
        print("\n Index occupied by player" + occupied + ". Please enter a new position\n")
        continue
    else:
        indexState = gameBoard.setIndexState(posX,posY,turn)
        if(indexState == -1):
            continue
    
    if(not player1CanMove and not player2CanMove):
        print("No valid moves for both players. Game over.\n")
        break
    turn = turn +1
    print("\n")
    printGameBoard.print_board(gameBoard)

    playerCount = gameBoard.get_count()
    print("Player1 = " + playerCount[0] +"\n"+"Player2 = "+ playerCount[1] + "\n")
    if(not player1CanMove or not player2CanMove):
        break
    else:
        continue


