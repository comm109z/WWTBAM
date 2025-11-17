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
        # Retrieve the next question for this round
        self.get_next_question()

        # Display the question and answer choices to the user
        self.question.display_to_user()

        # set the answer variables
        user_ans = ""
        self.final_answer = False

        # Continue looping until the player locks in a final answer
        while self.final_answer == False:
            print("Enter an option A B C or D or L to use a lifeline:")
            user_ans = input("> ").lower()  # Read input and convert to lowercase

            # If the user chooses a lifeline (L) and still has lifelines available
            if user_ans == "l" and self.n_lifelines > 0:
                result = self.question.fiftyfifty()  # Apply 50:50 lifeline, removing two incorrect options

                # If 50:50 was successfully applied, redisplay the updated options
                if result == True:
                    self.question.display_to_user()
                    # decrease available lifelines
                    self.n_lifelines = self.n_lifelines - 1

            # If the user entered a valid answer choice (A, B, C, or D)
            elif self.question.check_ans(user_ans) != "invalid":
                print(f"You are playing for £{self.question.difficulty}")
                print(f"If you are wriong you will walk away with £{winnings}")
                print("Final answer?... (Y/N)")
                final_ans = input("> ")

                # If the user confirms their choice, exit the loop
                if final_ans.lower() == "y":
                    self.final_answer = True

        # When user locks in, show what answer they chose
        print(f"You selected: {user_ans.upper()}")

        # Evaluate the final answer and report the result
        if self.question.check_ans(user_ans) == "correct":
            print("Correct!")
            return True
        else:
            print("Incorrect!")
            return False

    def play_game(self):
        # Ask the player for their name before starting the game
        self.get_user_name()

        ended = False  # Controls the main game loop

        # Keep playing rounds until the game ends
        while ended == False:

            # Print the game state or welcome message (depends on __str__)
            print(self)

            result = self.play_round()  # Play one question round and get True/False

            if result == True:
                # Player answered correctly → move up one level
                self.level += 1

                # If the player is past the final level, end the game
                if self.level >= len(self.board):
                    ended = True

            else:
                # Player answered incorrectly → game ends immediately
                ended = True

                # Determine the fallback guaranteed prize level
                # Level 11 typically corresponds to £32,000, level 5 to £1,000
                if self.level > 11:
                    self.level = 11   # Player reached the second safety net
                elif self.level > 5:
                    self.level = 5    # Player reached only the first safety net
                else:
                    self.level = 0    # Player did not reach any guaranteed level

        # After exiting the loop, the game has ended
        print("That's the end of the game!")
        print("You walk away with a check for...")

        # Display the prize amount based on the final level
        print(f"£{self.board[self.level]}")

            



