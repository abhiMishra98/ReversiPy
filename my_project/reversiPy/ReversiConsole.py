from reversiPy.ReversiBoard import ReversiBoard
class ReversiConsoleView:
    def __init__(self, board: ReversiBoard):
        self.pt_board = board

    def print_board(self):
        counter = 0
        for j in range(64):
            counter = counter +1
            print(self.pt_board.get_board()[j], end = " ")
            if(counter % 8 == 0):
                print("\n")

