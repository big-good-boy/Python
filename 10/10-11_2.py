import json

file = 'number.json'

with open(file) as obj:
  content = json.load(obj)

stirng = "Я знаю ваше любимое число! Это " + content
print(stirng)