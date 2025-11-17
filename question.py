class Question:

    # {
    #   "difficulty": 100,
    #   "question": "What colour is an emerald?",
    #   "answers": {
    #     "correct": "Green",
    #     "wrong": ["Blue", "Red", "Yellow"]
    #   }
    # },

    def __init__(self, question_dict):
        answers = question_dict['answers']
        self.a = { "text": answers["correct"], "correct": True  } 
        self.b = { "text": answers["correct"], "correct": True  } 
        self.c = { "text": answers["correct"], "correct": True  } 
        self.a = { "text": answers["correct"], "correct": True  } 
        