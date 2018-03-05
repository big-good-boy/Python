import json

number = input("Какое у вас любимое число? ")
file = "number.json"

with open(file, 'w') as obj:
  json.dump(number, obj)