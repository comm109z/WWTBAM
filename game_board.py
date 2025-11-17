

class GameBoard:
    def __init__(self, filename="questions.json"):
        self.user = None
        self.board = [ 0, 100, 200, 300, 500, 1000, 2000, 4000, 8000,
                       16000, 32000, 64000, 125000, 250000, 500000, 1000000 ] # money levels
        self.safe_levels = [ 5, 11 ] 
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
            row_str += f"£{self.board[idx]}\n"
            mystr += row_str
        mystr += f"Lifelines: {self.n_lifelines}\n"
        mystr += f"Answer locked in: {self.final_answer}\n"
        return mystr
    
    def get_user_name(self):
        self.user_name = ""
        while len(self.user_name) < 3:
            self.user_name = input("Enter your name: ").title().strip()

    def load_questions(self, filename="questions.json"):

