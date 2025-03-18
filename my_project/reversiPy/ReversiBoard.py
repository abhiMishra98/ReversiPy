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
                return FieldState(self._board[index])
        
        def get_board(self):
                """Returns the board as a list of characters."""
                return self._board
        
        def get_count(self):
                """Counts the number of pieces for both the players"""
                p1_coins = self._board.count(FieldState.PLAYER1.value)
                p2_coins = self._board.count(FieldState.PLAYER2.value)
                return [p1_coins,p2_coins]
        
        def checkOppCoinInImmediateCell(self, row_index:int, column_index:int, turn:int)
                currentPlayer = 'B' if (n%2) == 0 else 'W'
                opponentPlayer = 'W' if (currentPlayer == 'B') else 'B'
                for i in range(8):
                        newRow = row_index + DIRECTIONS[]
                
##CheckoppcoinInImmediatecell, sandwichcoins, canMove, setIndexState, 