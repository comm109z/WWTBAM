import json
from pathlib import Path

p = Path("questions.json")
content = p.read_text()

load_successful = False

questions = json.loads(content)

print(questions)