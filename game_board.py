class GameBoard:
    def __init__(self):
        self.user = None
        self.board = [ 0, 100, 200, 300, 500, 1000, 2000, 4000, 8000,] # money levels
        self.level = 0 # index of round in the board
        self.questions = []
        self.n_lifelines = 3
        self.final_answer = False

    def __str__(self):
        mystr = f"Player name {self.user}\n"
        mystr += "\n"
        for idx in range(len(self.board)):
            if idx == self.level:
                row_str = " * "
            else:
                row_str = "   "
            row_str += f"£{self.board[idx]}"
            mystr += row_str