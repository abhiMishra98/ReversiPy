from enum import Enum

class FieldState(Enum):
        FREE='*'
        PLAYER1='B'
        PLAYER2='W'

class ReversiBoard:
        DIRECTIONS = [
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1),   # Right
        (-1, -1), # Up-left (diagonal)
        (-1, 1),  # Up-right (diagonal)
        (1, -1),  # Down-left (diagonal)
        (1, 1)    # Down-right (diagonal)
        ]

        def __init__(self):
                """Initialize the board contents"""
                self._board = [FieldState.FREE.value] * 64
                self._board[27] = FieldState.PLAYER1.value
                self._board[28] = FieldState.PLAYER2.value
                self._board[35] = FieldState.PLAYER2.value
                self._board[36] = FieldState.PLAYER1.value
        
        def get_index_state(self, row_index:int, column_index:int) -> FieldState:
                """Returns the state of a given board position"""
                index = row_index*8+column_index
                state_str = self._board[index]
                return FieldState(state_str)
        
        def get_board(self):
                """Returns the board as a list of characters."""
                return self._board
        
        def get_count(self):
                """Counts the number of pieces for both the players"""
                p1_coins = self._board.count(FieldState.PLAYER1.value)
                p2_coins = self._board.count(FieldState.PLAYER2.value)
                return [p1_coins,p2_coins]
        
        def checkOppCoinInImmediateCell(self, row_index:int, column_index:int, turn:int):
                currentPlayer = 'B' if (turn%2) == 0 else 'W'
                opponentPlayer = 'W' if (currentPlayer == 'B') else 'B'
                validDirections = []
                for i in range(8):
                        newRow = int(row_index) + self.DIRECTIONS[i][0]
                        newCol = int(column_index) + self.DIRECTIONS[i][1]

                        opponentFound = False

                        while(newRow < 8 and newCol < 8 and newRow>=0 and newCol>=0):
                                cellState = self._board[newRow*8+newCol]
                                if(cellState == '*'):
                                        break
                                elif (cellState == currentPlayer):
                                        if(opponentFound):
                                                validDirections.append(i)
                                        break
                                elif(cellState == opponentPlayer):
                                        opponentFound = True
                                        newRow+=self.DIRECTIONS[i][0]
                                        newCol+=self.DIRECTIONS[i][1]
                return validDirections
        
        def sandwichCoins(self, rowIndex:int, columnIndex:int, turn:int, cellState:int):
                newRow = int(rowIndex) + self.DIRECTIONS[cellState][0]
                newCol = int(columnIndex) + self.DIRECTIONS[cellState][1]

                currentPlayer = 'B' if (turn%2) == 0 else 'W'

                isValidSandwich = True

                while(newRow <8 and newCol < 8 and newRow >= 0 and newCol >= 0):
                        if(self._board[newRow * 8 + newCol] == '*'):
                                break
                        if(self._board[newRow * 8 + newCol] == currentPlayer):
                                isValidSandwich = True
                                break

                        newRow += self.DIRECTIONS[cellState][0]
                        newCol += self.DIRECTIONS[cellState][1]

                if(not isValidSandwich):
                        return -1
                newRow = int(rowIndex) + self.DIRECTIONS[cellState][0]
                newCol = int(columnIndex) + self.DIRECTIONS[cellState][1]

                while(self._board[newRow*8 + newCol] != currentPlayer):
                        self._board[newRow * 8 + newCol] = currentPlayer
                        newRow += self.DIRECTIONS[cellState][0]
                        newCol += self.DIRECTIONS[cellState][1]
                
                return 0
        
        def setIndexState(self, rowIndex:int, columnIndex:int, turn:int):
                validDirections = self.checkOppCoinInImmediateCell(rowIndex,columnIndex,turn)
                currentPlayer = 'B' if (turn%2) == 0 else 'W'
                index = (int(rowIndex) * 8) + int(columnIndex)

                if(validDirections):
                        self._board[index] = currentPlayer
                        for direction in validDirections:
                                self.sandwichCoins(rowIndex, columnIndex, turn, direction)
                else:
                     print("Invalid move: No valid sandwich found")
                     return -1
                return 0

        def canMove(self, player:str):
                for row in range(8):
                        for col in range(8):
                                if(self._board[row*8+col] == '*'):
                                        turn = 0 if (player == 'B') else 1
                                        if(self.checkOppCoinInImmediateCell(row,col,turn)):
                                                return True
                return False