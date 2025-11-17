from pathlib import Path
import json
from question import Question
import random

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
        self.question = None

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
        self.user = ""
        while len(self.user) < 3:
            self.user = input("Enter your name: ").title().strip()

    def load_questions(self, filename="questions.json"):
        questions_loaded = False
        file_to_load = filename
        while questions_loaded == False:
            try:
                print(f"Loading text from: {file_to_load}")
                content = Path(file_to_load).read_text()
                print("Loaded text from file")
                loaded_object = json.loads(content)
                print("Extracted object")
                questions_json = loaded_object['questions']
                for item in questions_json:
                    self.questions.append( Question(item) )
                questions_loaded = True
            except:
                print("Could not load questions!")
                file_to_load = input("Enter the question file: ").strip()

    def get_next_question(self):
        money_amount = self.board[self.level + 1]
        poss_questions = []
        for item in self.questions:
            if item.difficulty == money_amount:
                poss_questions.append(item)
        self.question = random.choice(poss_questions)

    def play_round(self):
        self.question.g
        self.question.display_to_user()
        while self.final_answer == False:
            print("Enter and option A B C or D or L to use a lifeline:")
            user_ans = input("> ").lower()
            if user_ans == "l" and self.n_lifeline > 0:
                self.question.fiftyfifty()
            elif self.question.check_ans(user_ans) != "invalid":
                print("Final answer?... (Y/N)")
                final_ans = input("> ")
                if final_ans.lower() == "y":
                    self.final_answer == True
        print(f"You selected: {user_ans.upper()}")
        if self.question.check_ans(user_ans) == "correct":
            print("Correct!")
            return True
        else:
            print("Incorrect!")
            return False



