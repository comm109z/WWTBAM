import json
from pathlib import Path

def test_json_questions():
    p = Path("questions.json")

    load_successful = False

    try:
        content = p.read_text()
        questions = json.loads(content)
        load_successful = True
    except:
        pass

    assert load_successful == True

from question import Question

def test_question_class():
    question_dict = {
      "difficulty": 100,
      "question": "What colour is an emerald?",
      "answers": {
        "correct": "Green",
        "wrong": ["Blue", "Red", "Yellow"]
      }
    }
    my_question = Question(question_dict)
    assert my_question.text == question_dict["question"]