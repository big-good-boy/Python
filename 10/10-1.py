# with open('learning_python.txt') as file:
#   content = file.read()
#   print(content)

# with open('learning_python.txt') as file:
#   for line in file:
#     print(line.rstrip())

# with open('learning_python.txt') as file:
#   lines = file.readlines()

#   string = ''
#   for line in lines:
#     string += line

# print(string)

with open('learning_python.txt') as file:
  for line in file:
    print(line.rstrip().replace('Python', 'C'))