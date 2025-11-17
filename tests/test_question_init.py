from question import Question

def test_question_class():
    # create sample question data
    # matching json storage format
    question_dict = {  "difficulty": 100,
                        "question": "What colour is an emerald?",
                        "answers": {
                          "correct": "Green",
                          "wrong": ["Blue", "Red", "Yellow"] }
                        } 
    # initialise Question object with this data
    my_question = Question(question_dict)
    
    # check it loads correctly 
    assert my_question.text == question_dict["question"]