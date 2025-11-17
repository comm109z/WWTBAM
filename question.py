import random

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
    
    def __str__(self):
        mystr = ""
        mystr += f"Q. {self.text}\n"
        mystr += f"A. {self.a['text']} ({self.a['correct']})\n"
        mystr += f"B. {self.b['text']} ({self.b['correct']})\n"
        mystr += f"C. {self.c['text']} ({self.c['correct']})\n"
        mystr += f"D. {self.d['text']} ({self.d['correct']})\n"
        return mystr

    def randomise(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        options = [ a, b, c, d ]
        random.shuffle(options)
        self.a = options[0]
        self.b = options[1]
        self.c = options[2]
        self.d = options[3]
    

    def fiftyfifty(self):
        # get list of wrong options
        wrong_ans = [  ]
        if self.a["correct"] == False:
            wrong_ans.append("a")
        if self.b["correct"] == False:
            wrong_ans.append("b")
        if self.c["correct"] == False:
            wrong_ans.append("c")
        if self.d["correct"] == False:
            wrong_ans.append("d")

        # remove 1 / 3 
        wrong_ans.pop(random.randint(0,2)) 

        # blank remaining 2 / 3
        for item in wrong_ans:
            if item == "a": self.a["text"] = ""
            elif item == "b": self.b["text"] = ""
            elif item == "c": self.c["text"] = ""
            elif item == "d": self.d["text"] = ""

            