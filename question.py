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
        self.b = { "text": answers["wrong"][0], "correct": True  } 
        self.c = { "text": answers["wrong"][1], "correct": True  } 
        self.d = { "text": answers["wrong"][2], "correct": True  } 
        