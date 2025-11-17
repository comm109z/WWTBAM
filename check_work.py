from question import Question

question_dict = {  "difficulty": 100,
                        "question": "What colour is an emerald?",
                        "answers": {
                                      "correct": "Green",
                                      "wrong": ["Blue", "Red", "Yellow"] }  } 
    
# initialise Question object with this data
my_question = Question(question_dict)
print(f"a is ... {my_question.check_ans('a')}
print(f"b is ... {my_question.check_ans('b')}


my_question.fiftyfifty()
my_question.fiftyfifty()
print(my_question)