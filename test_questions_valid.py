import json
from pathlib import Path

p = Path("questions.json")


load_successful = False

try:
    content = p.read_text()
    questions = json.loads(content)
    load_successful = True
except:
    pass

