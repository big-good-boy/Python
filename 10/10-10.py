book = 'alice.txt'

with open(book, 'r') as file_object:
  contents = file_object.read()
  the = contents.lower().count('the')
  print(the)