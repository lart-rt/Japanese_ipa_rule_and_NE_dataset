from difflib import ndiff as nd
import json

with open('word_error.json', 'r') as f:
    we = json.load(f)

for v in we.values():
    v.append(''.join(nd(list(v[0]), list(v[1]))))

with open('word_error_dif.json', 'w') as f:
    json.dump(we, f, ensure_ascii=False, indent=0)