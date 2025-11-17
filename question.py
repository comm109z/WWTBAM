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
        self.text = question_dict['question']
        self.difficulty = question_dict['difficulty']
        answers = question_dict['answers']
        self.a = { "text": answers["correct"], "correct": True  } 
        self.b = { "text": answers["wrong"][0], "correct": False  } 
        self.c = { "text": answers["wrong"][1], "correct": False  } 
        self.d = { "text": answers["wrong"][2], "correct": False  } 
    
    def randomise(self):
        options = [ self.a, self.b, self.c, self.d ]
        options.shuffle()
        