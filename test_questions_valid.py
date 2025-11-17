import json
from pathlib import Path

p = Path("questions.json")
content = p.read_text()
try:
questions = json.loads(content)

print(questions)