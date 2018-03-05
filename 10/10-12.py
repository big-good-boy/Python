import json

file = 'number.json'

try:
  with open(file) as obj:
    content = json.load(obj)

except FileNotFoundError:
  number = input("Какое у вас любимое число? ")
  with open(file, 'w') as obj:
    json.dump(number, obj)

else:
  stirng = "Я знаю ваше любимое число! Это " + content
  print(stirng)