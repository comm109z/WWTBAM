import json
from pathlib import Path

p = Path("questions.json")
content = p.read_text()

print(content)