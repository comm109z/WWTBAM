from question import Question
from game_board import GameBoard

# question_dict = {  "difficulty": 100,
#                         "question": "What colour is an emerald?",
#                         "answers": {
#                                       "correct": "Green",
#                                       "wrong": ["Blue", "Red", "Yellow"] }  } 
    
# # initialise Question object with this data
# my_question = Question(question_dict)
# print(my_question)
# print(f"a is ... {my_question.check_ans('a')}")
# print(f"b is ... {my_question.check_ans('b')}")
# print(f"b is ... {my_question.check_ans('c')}")
# print(f"b is ... {my_question.check_ans('d')}")
# my_question.fiftyfifty()
# print(my_question)
# print(f"a is ... {my_question.check_ans('a')}")
# print(f"b is ... {my_question.check_ans('b')}")
# print(f"b is ... {my_question.check_ans('c')}")
# print(f"b is ... {my_question.check_ans('d')}")

board = GameBoard()
print(len(board.questions))
# board.get_user_name()

board.load_questions()
print(len(board.questions))
print(board.question)
board.get_next_question()
print(board.question)