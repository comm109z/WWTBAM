class GameBoard:
    def __init__(self):
        self.user = None
        self.board = [] # money levels
        self.level = 0 # index of round in the board
        self.questions = []
        self.n_lifelines = 3
        self.