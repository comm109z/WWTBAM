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
        self.answers = {}
        self.answers['a'] = { "text": answers["correct"], "correct": True  } 
        self.answers['b'] = { "text": answers["wrong"][0], "correct": False  } 
        self.answers['c'] = { "text": answers["wrong"][1], "correct": False  } 
        self.answers['d'] = { "text": answers["wrong"][2], "correct": False  } 
        self.fiftyfifty_used = False
    
    def get_correct(self):
        for key in [ "a","b","c","d" ]:
            if self.answers[key]["correct"] == True:
                return key

    def get_wrong(self):
        wrong_ans = []
        for key in [ "a","b","c","d" ]:
            if self.answers[key]["correct"] == False:
                wrong_ans.append(key)
        return wrong_ans


    def __str__(self):
        mystr = ""
        mystr += f"Q. {self.text}\n"
        for key in [ "a", "b", "c", "d" ]:
            text = self.answer[key]['text']
            correct = self.answer[key]['correct']
            mystr += f"{key.upper()}. {text} ({correct})\n"
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

        if self.fiftyfifty_used == True:
            return False

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

        self.fiftyfifty_used = True
        return True
    
    def check_ans(self, user_ans):
        if user_ans == "a":
            # check answer not eliminated
            if self.a['text'] == "":
                return "invalid"
            # check if correct
            elif self.a["correct"]:
                return "correct"
            # otherwise must be wrong
            else:
                return "wrong"
        elif user_ans == "b":
            # check answer not eliminated
            if self.b['text'] == "":
                return "invalid"
            # check if correct
            elif self.b["correct"]:
                return "correct"
            # otherwise must be wrong
            else:
                return "wrong"
        elif user_ans == "c":
            # check answer not eliminated
            if self.c['text'] == "":
                return "invalid"
            # check if correct
            elif self.c["correct"]:
                return "correct"
            # otherwise must be wrong
            else:
                return "wrong"
        elif user_ans == "d":
            # check answer not eliminated
            if self.d['text'] == "":
                return "invalid"
            # check if correct
            elif self.d["correct"]:
                return "correct"
            # otherwise must be wrong
            else:
                return "wrong"
        else:
            return "invalid"